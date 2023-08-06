from collections import defaultdict
from itertools import repeat

from wxkit.services import WxService
from wxkit.models import ErrorModel, Wind, Temperature, Station, WeatherPoint
from wxkit.utils.http_request import retry_request, compose_url_path, HTTP_METHOD
from wxkit.utils.convertor import kph_to_mps

ACCU_WEATHER_BASE_URL = "http://dataservice.accuweather.com"
ACCU_WEATHER_CURRENT_WEATHER = ("weather",)
ACCU_WEATHER_FORECAST_3_HOURLY = ("forecast",)
ACCU_WEATHER_FORECAST_HOURLY = ("forecast", "hourly")
ACCU_WEATHER_FORECAST_PERIOD = (1, 3, 24)


class AccuweatherWxService(WxService):
    def __init__(self, credential):
        super().__init__(credential)
        self.LOCATION_CACHE = defaultdict(dict)

    def auth_params(self, **params):
        p = dict(apikey=self.credential.apikey)
        p.update(params)
        return p

    def as_station(self, data):
        coord = data.get("GeoPosition", {})
        return Station(
            lat=coord.get("Latitude", 0),
            lon=coord.get("Longitude", 0),
            name=data.get("EnglishName", ""),
        )

    def _modelize(self, data, location):
        location_data = self.get_location(location)
        temp = data.get("Temperature", {}).get("Metric", {}).get(
            "Value", 0
        ) or data.get("Temperature", {}).get("Value", 0)
        temperature = Temperature(temp_avg=temp)
        speed = data.get("Wind", {}).get("Speed", {}).get("Metric", {}).get(
            "Value", 0
        ) or data.get("Wind", {}).get("Speed", {}).get("Value", 0)
        wind = Wind(
            speed=round(kph_to_mps(speed), 2),
            degree=data.get("Wind", {}).get("Direction", {}).get("Degrees", 0),
        )
        try:
            status = data.get("WeatherText", "") or data.get("IconPhrase", "")
            description = data.get("WeatherText", "") or data.get("IconPhrase", "")
            icon = data.get("WeatherIcon", "")
        except Exception:
            status = ""
            description = ""
            icon = ""

        pressure = data.get("Pressure", {}).get("Metric", {}).get("Value", 0)
        humidity = data.get("RelativeHumidity", 0)
        rain = data.get("PrecipitationProbability", 0)
        snow = data.get("SnowProbability", 0)
        clouds = data.get("CloudCover", 0)
        time = data.get("EpochTime", 0) or data.get("EpochDateTime", 0)
        weather_point = WeatherPoint(
            station=self.as_station(location_data),
            status=status,
            description=description,
            icon=icon,
            temp=temperature,
            pressure=pressure,
            humidity=humidity,
            rain=rain,
            wind=wind,
            clouds=clouds,
            snow=snow,
            time=time,
            raw_data=data,
        )
        return weather_point

    def get_location(self, location):
        if self.LOCATION_CACHE[location]:
            return self.LOCATION_CACHE[location]

        url = compose_url_path(
            ACCU_WEATHER_BASE_URL,
            "locations",
            "v1",
            "cities",
            "geoposition",
            "search",
        )
        params = self.auth_params(q=f"{location.lat},{location.lon}")
        try:
            resp_data = retry_request(HTTP_METHOD.GET, url, params=params)
            self.LOCATION_CACHE[location] = resp_data
        except Exception as e:
            return self.handle_error(e)

        return resp_data

    def get_current_weather_by_location(self, location):
        location_data = self.get_location(location)
        if isinstance(location_data, ErrorModel):
            return location_data

        url = compose_url_path(
            ACCU_WEATHER_BASE_URL,
            "currentconditions",
            "v1",
            location_data.get("Key", ""),
        )
        params = self.auth_params(details=True)
        try:
            resp_data = retry_request(HTTP_METHOD.GET, url, params=params)
        except Exception as e:
            return self.handle_error(e)
        wxs = list(map(self._modelize, resp_data, repeat(location)))
        return wxs[0]

    def get_forecast_weather_by_location(self, location, period=1, samples=12):
        if period == 24:
            predict_type = "daily"
            predict_unit = "day"
        else:
            predict_type = "hourly"
            predict_unit = "hour"

        location_data = self.get_location(location)
        if isinstance(location_data, ErrorModel):
            return location_data

        url = compose_url_path(
            ACCU_WEATHER_BASE_URL,
            "forecasts",
            "v1",
            predict_type,
            f"{period * samples}{predict_unit}",
            location_data.get("Key", ""),
        )
        params = self.auth_params(details=True, metric=True)
        try:
            resp_data = retry_request(HTTP_METHOD.GET, url, params=params)
        except Exception as e:
            return self.handle_error(e)

        wxs = list(map(self._modelize, resp_data, repeat(location)))
        return wxs

    def handle_error(self, exception):
        error = ErrorModel()
        if getattr(exception, "response", None) is not None:
            try:
                # Get error context from HTTP error if response.
                response = exception.response.json()
                error.code = response["cod"]
                error.message = response["message"]
                error.raw_data = response
            except Exception:
                error.code = exception.response.status_code
                error.message = exception.response.text
        else:
            error.message = str(exception)

        return error
