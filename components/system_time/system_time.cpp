#include "system_time.h"
#include "esphome/core/log.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace system_time {

static const char *TAG = "system_time";
static constexpr uint32_t START_TIMESTAMP = 1546300800;  // 01/01/2019 00:00:00

void SystemTimeComponent::setup() {}

void SystemTimeComponent::update() {
  uint32_t time = START_TIMESTAMP + (millis() / 1000);
  time::RealTimeClock::synchronize_epoch_(time);
}

void SystemTimeComponent::dump_config() {
  ESP_LOGCONFIG(TAG, "System Time:");
  ESP_LOGCONFIG(TAG, "  Timezone: '%s'", this->timezone_.c_str());
}
}  // namespace system_time
}  // namespace esphome