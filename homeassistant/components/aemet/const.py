"""Constant values for the AEMET OpenData component."""
from __future__ import annotations

from aemet_opendata.const import (
    AOD_COND_CLEAR_NIGHT,
    AOD_COND_CLOUDY,
    AOD_COND_FOG,
    AOD_COND_LIGHTNING,
    AOD_COND_LIGHTNING_RAINY,
    AOD_COND_PARTLY_CLODUY,
    AOD_COND_POURING,
    AOD_COND_RAINY,
    AOD_COND_SNOWY,
    AOD_COND_SUNNY,
    AOD_CONDITION,
    AOD_FORECAST_DAILY,
    AOD_FORECAST_HOURLY,
    AOD_PRECIPITATION,
    AOD_PRECIPITATION_PROBABILITY,
    AOD_TEMP,
    AOD_TEMP_MAX,
    AOD_TEMP_MIN,
    AOD_TIMESTAMP_UTC,
    AOD_WIND_DIRECTION,
    AOD_WIND_SPEED,
    AOD_WIND_SPEED_MAX,
)

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SUNNY,
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_NATIVE_PRECIPITATION,
    ATTR_FORECAST_NATIVE_TEMP,
    ATTR_FORECAST_NATIVE_TEMP_LOW,
    ATTR_FORECAST_NATIVE_WIND_GUST_SPEED,
    ATTR_FORECAST_NATIVE_WIND_SPEED,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
)
from homeassistant.const import Platform

ATTRIBUTION = "Powered by AEMET OpenData"
CONF_STATION_UPDATES = "station_updates"
PLATFORMS = [Platform.SENSOR, Platform.WEATHER]
DEFAULT_NAME = "AEMET"
DOMAIN = "aemet"
ENTRY_NAME = "name"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"

ATTR_API_CONDITION = "condition"
ATTR_API_FORECAST_CONDITION = "condition"
ATTR_API_FORECAST_PRECIPITATION = "precipitation"
ATTR_API_FORECAST_PRECIPITATION_PROBABILITY = "precipitation_probability"
ATTR_API_FORECAST_TEMP = "temperature"
ATTR_API_FORECAST_TEMP_LOW = "templow"
ATTR_API_FORECAST_TIME = "datetime"
ATTR_API_FORECAST_WIND_BEARING = "wind_bearing"
ATTR_API_FORECAST_WIND_MAX_SPEED = "wind_max_speed"
ATTR_API_FORECAST_WIND_SPEED = "wind_speed"
ATTR_API_HUMIDITY = "humidity"
ATTR_API_PRESSURE = "pressure"
ATTR_API_RAIN = "rain"
ATTR_API_RAIN_PROB = "rain-probability"
ATTR_API_SNOW = "snow"
ATTR_API_SNOW_PROB = "snow-probability"
ATTR_API_STATION_ID = "station-id"
ATTR_API_STATION_NAME = "station-name"
ATTR_API_STATION_TIMESTAMP = "station-timestamp"
ATTR_API_STORM_PROB = "storm-probability"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_TEMPERATURE_FEELING = "temperature-feeling"
ATTR_API_TOWN_ID = "town-id"
ATTR_API_TOWN_NAME = "town-name"
ATTR_API_TOWN_TIMESTAMP = "town-timestamp"
ATTR_API_WIND_BEARING = "wind-bearing"
ATTR_API_WIND_MAX_SPEED = "wind-max-speed"
ATTR_API_WIND_SPEED = "wind-speed"

CONDITIONS_MAP = {
    AOD_COND_CLEAR_NIGHT: ATTR_CONDITION_CLEAR_NIGHT,
    AOD_COND_CLOUDY: ATTR_CONDITION_CLOUDY,
    AOD_COND_FOG: ATTR_CONDITION_FOG,
    AOD_COND_LIGHTNING: ATTR_CONDITION_LIGHTNING,
    AOD_COND_LIGHTNING_RAINY: ATTR_CONDITION_LIGHTNING_RAINY,
    AOD_COND_PARTLY_CLODUY: ATTR_CONDITION_PARTLYCLOUDY,
    AOD_COND_POURING: ATTR_CONDITION_POURING,
    AOD_COND_RAINY: ATTR_CONDITION_RAINY,
    AOD_COND_SNOWY: ATTR_CONDITION_SNOWY,
    AOD_COND_SUNNY: ATTR_CONDITION_SUNNY,
}

FORECAST_MAP = {
    AOD_FORECAST_DAILY: {
        AOD_CONDITION: ATTR_FORECAST_CONDITION,
        AOD_PRECIPITATION_PROBABILITY: ATTR_FORECAST_PRECIPITATION_PROBABILITY,
        AOD_TEMP_MAX: ATTR_FORECAST_NATIVE_TEMP,
        AOD_TEMP_MIN: ATTR_FORECAST_NATIVE_TEMP_LOW,
        AOD_TIMESTAMP_UTC: ATTR_FORECAST_TIME,
        AOD_WIND_DIRECTION: ATTR_FORECAST_WIND_BEARING,
        AOD_WIND_SPEED: ATTR_FORECAST_NATIVE_WIND_SPEED,
    },
    AOD_FORECAST_HOURLY: {
        AOD_CONDITION: ATTR_FORECAST_CONDITION,
        AOD_PRECIPITATION_PROBABILITY: ATTR_FORECAST_PRECIPITATION_PROBABILITY,
        AOD_PRECIPITATION: ATTR_FORECAST_NATIVE_PRECIPITATION,
        AOD_TEMP: ATTR_FORECAST_NATIVE_TEMP,
        AOD_TIMESTAMP_UTC: ATTR_FORECAST_TIME,
        AOD_WIND_DIRECTION: ATTR_FORECAST_WIND_BEARING,
        AOD_WIND_SPEED_MAX: ATTR_FORECAST_NATIVE_WIND_GUST_SPEED,
        AOD_WIND_SPEED: ATTR_FORECAST_NATIVE_WIND_SPEED,
    },
}
