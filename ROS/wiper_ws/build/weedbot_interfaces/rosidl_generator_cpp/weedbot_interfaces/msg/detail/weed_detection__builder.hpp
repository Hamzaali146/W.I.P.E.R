// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_detection.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__BUILDER_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "weedbot_interfaces/msg/detail/weed_detection__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace weedbot_interfaces
{

namespace msg
{

namespace builder
{

class Init_WeedDetection_mask
{
public:
  explicit Init_WeedDetection_mask(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  ::weedbot_interfaces::msg::WeedDetection mask(::weedbot_interfaces::msg::WeedDetection::_mask_type arg)
  {
    msg_.mask = std::move(arg);
    return std::move(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_real_world_z
{
public:
  explicit Init_WeedDetection_real_world_z(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_mask real_world_z(::weedbot_interfaces::msg::WeedDetection::_real_world_z_type arg)
  {
    msg_.real_world_z = std::move(arg);
    return Init_WeedDetection_mask(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_real_world_y
{
public:
  explicit Init_WeedDetection_real_world_y(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_real_world_z real_world_y(::weedbot_interfaces::msg::WeedDetection::_real_world_y_type arg)
  {
    msg_.real_world_y = std::move(arg);
    return Init_WeedDetection_real_world_z(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_real_world_x
{
public:
  explicit Init_WeedDetection_real_world_x(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_real_world_y real_world_x(::weedbot_interfaces::msg::WeedDetection::_real_world_x_type arg)
  {
    msg_.real_world_x = std::move(arg);
    return Init_WeedDetection_real_world_y(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_class_ids
{
public:
  explicit Init_WeedDetection_class_ids(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_real_world_x class_ids(::weedbot_interfaces::msg::WeedDetection::_class_ids_type arg)
  {
    msg_.class_ids = std::move(arg);
    return Init_WeedDetection_real_world_x(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_confidences
{
public:
  explicit Init_WeedDetection_confidences(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_class_ids confidences(::weedbot_interfaces::msg::WeedDetection::_confidences_type arg)
  {
    msg_.confidences = std::move(arg);
    return Init_WeedDetection_class_ids(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_bbox_h
{
public:
  explicit Init_WeedDetection_bbox_h(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_confidences bbox_h(::weedbot_interfaces::msg::WeedDetection::_bbox_h_type arg)
  {
    msg_.bbox_h = std::move(arg);
    return Init_WeedDetection_confidences(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_bbox_w
{
public:
  explicit Init_WeedDetection_bbox_w(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_bbox_h bbox_w(::weedbot_interfaces::msg::WeedDetection::_bbox_w_type arg)
  {
    msg_.bbox_w = std::move(arg);
    return Init_WeedDetection_bbox_h(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_bbox_y
{
public:
  explicit Init_WeedDetection_bbox_y(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_bbox_w bbox_y(::weedbot_interfaces::msg::WeedDetection::_bbox_y_type arg)
  {
    msg_.bbox_y = std::move(arg);
    return Init_WeedDetection_bbox_w(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_bbox_x
{
public:
  explicit Init_WeedDetection_bbox_x(::weedbot_interfaces::msg::WeedDetection & msg)
  : msg_(msg)
  {}
  Init_WeedDetection_bbox_y bbox_x(::weedbot_interfaces::msg::WeedDetection::_bbox_x_type arg)
  {
    msg_.bbox_x = std::move(arg);
    return Init_WeedDetection_bbox_y(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

class Init_WeedDetection_header
{
public:
  Init_WeedDetection_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WeedDetection_bbox_x header(::weedbot_interfaces::msg::WeedDetection::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WeedDetection_bbox_x(msg_);
  }

private:
  ::weedbot_interfaces::msg::WeedDetection msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::weedbot_interfaces::msg::WeedDetection>()
{
  return weedbot_interfaces::msg::builder::Init_WeedDetection_header();
}

}  // namespace weedbot_interfaces

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__BUILDER_HPP_
