// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice
#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "weedbot_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "weedbot_interfaces/msg/detail/weed_detection__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
bool cdr_serialize_weedbot_interfaces__msg__WeedDetection(
  const weedbot_interfaces__msg__WeedDetection * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
bool cdr_deserialize_weedbot_interfaces__msg__WeedDetection(
  eprosima::fastcdr::Cdr &,
  weedbot_interfaces__msg__WeedDetection * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
size_t get_serialized_size_weedbot_interfaces__msg__WeedDetection(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
size_t max_serialized_size_weedbot_interfaces__msg__WeedDetection(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
bool cdr_serialize_key_weedbot_interfaces__msg__WeedDetection(
  const weedbot_interfaces__msg__WeedDetection * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
size_t get_serialized_size_key_weedbot_interfaces__msg__WeedDetection(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
size_t max_serialized_size_key_weedbot_interfaces__msg__WeedDetection(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_weedbot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, weedbot_interfaces, msg, WeedDetection)();

#ifdef __cplusplus
}
#endif

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
