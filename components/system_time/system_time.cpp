#include "system_time.h"
#include "esphome/core/log.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace system_time {

static const char *TAG = "system_time";
static constexpr uint32_t START_TIMESTAMP = 1546300800;  // 01/01/2019 00:00:00

void SystemTimeComponent::setup() {}

void SystemTimeComponent::update() {
  uint32_t time = this->start_datetime_ + (millis() / 1000);
  time::RealTimeClock::synchronize_epoch_(time);
}

void SystemTimeComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "System Time:");
  ESP_LOGCONFIG(TAG, "  Timezone: '%s'", this->timezone_.c_str());
  ESP_LOGCONFIG(TAG, "  Start Datetime: %s",
                ESPTime::from_epoch_utc(this->start_datetime_).strftime("%Y-%m-%d %H:%M:%S").c_str());
}

void SystemTimeComponent::set_start_datetime(ESPTime datetime) {
  datetime.day_of_week = 1;
  datetime.day_of_year = 1;
  datetime.recalc_timestamp_utc(false);

  if (datetime.timestamp < START_TIMESTAMP) {
    this->start_datetime_ = START_TIMESTAMP;
    ESP_LOGW(TAG, "trying to set an invalid start date time %s", datetime.strftime("%Y-%m-%d %H:%M:%S").c_str());
    this->update();
    return;
  }

  this->start_datetime_ = datetime.timestamp;
  ESP_LOGD(TAG, "set start datetime %s => %d", datetime.strftime("%Y-%m-%d %H:%M:%S").c_str(), datetime.timestamp);
  this->update();
}

void SystemTimeComponent::set_current_datetime(ESPTime datetime) {
  datetime.day_of_week = 1;
  datetime.day_of_year = 1;
  datetime.recalc_timestamp_utc(false);

  if (datetime.timestamp < START_TIMESTAMP) {
    this->start_datetime_ = START_TIMESTAMP;
    ESP_LOGW(TAG, "trying to set an invalid time %s", datetime.strftime("%Y-%m-%d %H:%M:%S").c_str());
    this->update();
    return;
  }

  this->start_datetime_ = datetime.timestamp - (millis() / 1000);
  ESP_LOGD(TAG, "set current datetime %s => %d", datetime.strftime("%Y-%m-%d %H:%M:%S").c_str(), datetime.timestamp);
  this->update();
}

}  // namespace system_time
}  // namespace esphome