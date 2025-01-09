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
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    
    await cg.register_component(var, config)
    await time.register_time(var, config)