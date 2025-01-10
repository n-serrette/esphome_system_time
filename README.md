# esphome_system_time
An ersatz of time component based on the micro controller time

## Config

### Component

```yaml
time:
  - platform: system_time
  # with string
  - start_datetime: "2024-12-31 12:34:56"
  # Individual datetime parts
  - start_datetime:
      year: 2024
      month: 12
      day: 31
      hour: 12
      minute: 34
      second: 56

```
Configuration variables:

* **start_datetime** : (Optional, string, datetime parts): The value starting value of the clock.

### Action

```yaml
# with string
system_time.start_datetime_set:
  id: sys_time
  start_datetime: "2024-12-31 12:34:56"

# Individual datetime parts
system_time.start_datetime_set:
  id: sys_time
  start_datetime:
    year: 2024
    month: 12
    day: 31
    hour: 12
    minute: 34
    second: 56

# Using a lambda
system_time.start_datetime_set:
  id: sys_time
  start_datetime: !lambda |-
    // Return an ESPTime struct
    return {.second = 56, .minute = 34, .hour = 12, .day_of_month = 31, .month = 12, .year = 2024 };
```

Configuration variables:

* **id** (Required, ID): The ID of the datetime to set.
* **start_datetime** (Required, string, datetime parts, templatable): The value to set the start datetime to.

## Note

The clock start on the **2019-01-01 00:00:00** which is the first valid timestamp for ESPHome