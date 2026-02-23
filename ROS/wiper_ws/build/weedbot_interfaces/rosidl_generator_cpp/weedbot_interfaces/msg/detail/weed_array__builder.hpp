// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_array.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__BUILDER_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "weedbot_interfaces/msg/detail/weed_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace weedbot_interfaces
{

namespace msg
{

namespace builder
{

class Init_WeedArray_inference_time_ms
{
public:
  explicit Init_WeedArray_inference_time_ms(::weedbot_interfaces::msg::WeedArray & msg)
  : msg_(msg)
  {}
  ::weedbot_interfaces::msg::WeedArray inference_time_ms(::weedbot_interfaces::msg::WeedArray::_inference_time_ms_type arg)
  {
    msg_.inference_time_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedArray msg_;
};

class Init_WeedArray_total_weeds
{
public:
  explicit Init_WeedArray_total_weeds(::weedbot_interfaces::msg::WeedArray & msg)
  : msg_(msg)
  {}
  Init_WeedArray_inference_time_ms total_weeds(::weedbot_interfaces::msg::WeedArray::_total_weeds_type arg)
  {
    msg_.total_weeds = std::move(arg);
    return Init_WeedArray_inference_time_ms(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedArray msg_;
};

class Init_WeedArray_detections
{
public:
  explicit Init_WeedArray_detections(::weedbot_interfaces::msg::WeedArray & msg)
  : msg_(msg)
  {}
  Init_WeedArray_total_weeds detections(::weedbot_interfaces::msg::WeedArray::_detections_type arg)
  {
    msg_.detections = std::move(arg);
    return Init_WeedArray_total_weeds(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedArray msg_;
};

class Init_WeedArray_header
{
public:
  Init_WeedArray_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WeedArray_detections header(::weedbot_interfaces::msg::WeedArray::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WeedArray_detections(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::weedbot_interfaces::msg::WeedArray>()
{
  return weedbot_interfaces::msg::builder::Init_WeedArray_header();
}

}  // namespace weedbot_interfaces

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__BUILDER_HPP_
