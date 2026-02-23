// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include <cstddef>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "weedbot_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "weedbot_interfaces/msg/detail/weed_detection__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace weedbot_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
cdr_serialize(
  const weedbot_interfaces::msg::WeedDetection & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  weedbot_interfaces::msg::WeedDetection & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
get_serialized_size(
  const weedbot_interfaces::msg::WeedDetection & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
max_serialized_size_WeedDetection(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
cdr_serialize_key(
  const weedbot_interfaces::msg::WeedDetection & ros_message,
  eprosima::fastcdr::Cdr &);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
get_serialized_size_key(
  const weedbot_interfaces::msg::WeedDetection & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
max_serialized_size_key_WeedDetection(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace weedbot_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_weedbot_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, weedbot_interfaces, msg, WeedDetection)();

#ifdef __cplusplus
}
#endif

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
