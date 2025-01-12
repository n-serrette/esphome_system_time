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
  void set_current_datetime(ESPTime);

 protected:
  uint32_t start_datetime_;
};

template<typename... Ts>
class SystemTimeSetStartDateTimeAction : public Action<Ts...>, public Parented<SystemTimeComponent> {
 public:
  TEMPLATABLE_VALUE(ESPTime, start_datetime)

  void play(Ts... x) override {
    if (!this->start_datetime_.has_value())
      return;
    this->parent_->set_start_datetime(this->start_datetime_.value(x...));
  }
};

template<typename... Ts>
class SystemTimeSetCurrentDateTimeAction : public Action<Ts...>, public Parented<SystemTimeComponent> {
 public:
  TEMPLATABLE_VALUE(ESPTime, current_datetime)

  void play(Ts... x) override {
    if (!this->current_datetime_.has_value())
      return;
    this->parent_->set_start_datetime(this->current_datetime_.value(x...));
  }
};

}  // namespace system_time
}  // namespace esphome