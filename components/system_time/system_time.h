#pragma once

#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace system_time {

class SystemTimeComponent : public time::RealTimeClock {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;

  void set_start_datetime(ESPTime);
 protected:
  uint32_t start_datetime_;
};
}  // namespace system_time
}  // namespace esphome