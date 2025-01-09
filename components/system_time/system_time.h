#pragma once

#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace system_time {

class SystemTimeComponent : public time::RealTimeClock {
 public:
  void setup() override;
  void update() override;
  void dump_config() override;

};
}  // namespace system_time
}  // namespace esphome