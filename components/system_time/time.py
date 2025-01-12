from esphome import automation
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
    CONF_DATETIME
)

CONF_START_DATETIME = "start_datetime"

systemTime_ns = cg.esphome_ns.namespace("system_time")
SystemTimeComponent = systemTime_ns.class_("SystemTimeComponent", time.RealTimeClock)

SystemTimeSetStartDateTimeAction = systemTime_ns.class_("SystemTimeSetStartDateTimeAction", automation.Action)
SystemTimeSetCurrentDateTimeAction = systemTime_ns.class_("SystemTimeSetCurrentDateTimeAction", automation.Action)

CONFIG_SCHEMA = time.TIME_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(SystemTimeComponent),
        cv.Optional(CONF_START_DATETIME, default="2019-01-01 00:00:00"): cv.date_time(date=True, time=True),
    }
).extend(cv.COMPONENT_SCHEMA)

def datetimeConfigToCode(datetime_config):
    return cg.StructInitializer(
        cg.ESPTime,
        ("second", datetime_config[CONF_SECOND]),
        ("minute", datetime_config[CONF_MINUTE]),
        ("hour", datetime_config[CONF_HOUR]),
        ("day_of_month", datetime_config[CONF_DAY]),
        ("month", datetime_config[CONF_MONTH]),
        ("year", datetime_config[CONF_YEAR]),
    )


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    
    if (config[CONF_START_DATETIME] is not None):
        datetime_struct = datetimeConfigToCode(config[CONF_START_DATETIME])
        cg.add(var.set_start_datetime(datetime_struct))
    
    await cg.register_component(var, config)
    await time.register_time(var, config)


SET_DATETIME_SCHEMA = cv.maybe_simple_value(
    {
        cv.GenerateID(): cv.use_id(SystemTimeComponent),
        cv.Required(CONF_DATETIME): cv.templatable(cv.date_time(date= True, time=True)),
    },
    key=CONF_DATETIME,
)


@automation.register_action(
    "system_time.start_datetime_set",
    SystemTimeSetStartDateTimeAction,
    SET_DATETIME_SCHEMA,
)
async def datetime_datetime_set_to_code(config, action_id, template_arg, args):
    action_var = cg.new_Pvariable(action_id, template_arg)
    await cg.register_parented(action_var, config[CONF_ID])

    datetime_config = config[CONF_DATETIME]
    if cg.is_template(datetime_config):
        template_ = await cg.templatable(datetime_config, args, cg.ESPTime)
        cg.add(action_var.set_start_datetime(template_))
    else:
        datetime_struct = datetimeConfigToCode(config[CONF_DATETIME])
        cg.add(action_var.set_start_datetime(datetime_struct))
    return action_var


@automation.register_action(
    "system_time.current_datetime_set",
    SystemTimeSetCurrentDateTimeAction,
    SET_DATETIME_SCHEMA,
)
async def datetime_datetime_set_to_code(config, action_id, template_arg, args):
    action_var = cg.new_Pvariable(action_id, template_arg)
    await cg.register_parented(action_var, config[CONF_ID])

    datetime_config = config[CONF_DATETIME]
    if cg.is_template(datetime_config):
        template_ = await cg.templatable(datetime_config, args, cg.ESPTime)
        cg.add(action_var.set_current_datetime(template_))
    else:
        datetime_struct = datetimeConfigToCode(config[CONF_DATETIME])
        cg.add(action_var.set_current_datetime(datetime_struct))
    return action_var