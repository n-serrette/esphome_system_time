# esphome_system_time
An ersatz of time component based on the micro controller time

## Config

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

* **start_datetime** : (Optional, string, datetime parts): The value starting value of the clock.

## Note

The clock start on the **2019-01-01 00:00:00** which is the first valid timestamp for ESPHome