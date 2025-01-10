import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import time
from esphome.const import (
    CONF_ID,
    CONF_SECOND,
    CONF_MINUTE,
    CONF_HOUR,
    CONF_DAY,
    CONF_MONTH,
    CONF_YEAR,
)

CONF_START_DATETIME = "start_datetime"

systemTime_ns = cg.esphome_ns.namespace("system_time")
SystemTimeComponent = systemTime_ns.class_("SystemTimeComponent", time.RealTimeClock)

CONFIG_SCHEMA = time.TIME_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(SystemTimeComponent),
        cv.Optional(CONF_START_DATETIME, default="2019-01-01 00:00:00"): cv.date_time(date=True, time=True),
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    
    if (config[CONF_START_DATETIME] is not None):
        datetime_config = config[CONF_START_DATETIME]
        datetime_struct = cg.StructInitializer(
            cg.ESPTime,
            ("second", datetime_config[CONF_SECOND]),
            ("minute", datetime_config[CONF_MINUTE]),
            ("hour", datetime_config[CONF_HOUR]),
            ("day_of_month", datetime_config[CONF_DAY]),
            ("month", datetime_config[CONF_MONTH]),
            ("year", datetime_config[CONF_YEAR]),
        )
        cg.add(var.set_start_datetime(datetime_struct))
    
    await cg.register_component(var, config)
    await time.register_time(var, config)