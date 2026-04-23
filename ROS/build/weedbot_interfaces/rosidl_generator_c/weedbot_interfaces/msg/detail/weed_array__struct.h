// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_array.h"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_H_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'detections'
#include "weedbot_interfaces/msg/detail/weed_detection__struct.h"

/// Struct defined in msg/WeedArray in the package weedbot_interfaces.
typedef struct weedbot_interfaces__msg__WeedArray
{
  std_msgs__msg__Header header;
  weedbot_interfaces__msg__WeedDetection__Sequence detections;
  int32_t total_weeds;
  double inference_time_ms;
} weedbot_interfaces__msg__WeedArray;

// Struct for a sequence of weedbot_interfaces__msg__WeedArray.
typedef struct weedbot_interfaces__msg__WeedArray__Sequence
{
  weedbot_interfaces__msg__WeedArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} weedbot_interfaces__msg__WeedArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_H_
