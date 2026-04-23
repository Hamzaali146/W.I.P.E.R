// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_detection.h"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_H_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_H_

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
// Member 'bbox_x'
// Member 'bbox_y'
// Member 'bbox_w'
// Member 'bbox_h'
// Member 'confidences'
// Member 'class_ids'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'mask'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in msg/WeedDetection in the package weedbot_interfaces.
typedef struct weedbot_interfaces__msg__WeedDetection
{
  std_msgs__msg__Header header;
  /// Pixel coordinates (normalized 0-1)
  /// Bounding box x coordinates
  rosidl_runtime_c__float__Sequence bbox_x;
  /// Bounding box y coordinates
  rosidl_runtime_c__float__Sequence bbox_y;
  /// Bounding box widths
  rosidl_runtime_c__float__Sequence bbox_w;
  /// Bounding box heights
  rosidl_runtime_c__float__Sequence bbox_h;
  /// Detection confidences
  rosidl_runtime_c__float__Sequence confidences;
  /// Class IDs (if multiple weed types)
  rosidl_runtime_c__int32__Sequence class_ids;
  /// NEW: Real-world coordinates (meters, relative to camera center on ground)
  /// X position in meters (+ = right, - = left)
  float real_world_x;
  /// Y position in meters (+ = forward, - = backward)
  float real_world_y;
  /// Z position in meters (0 = ground plane)
  float real_world_z;
  /// Optional segmentation mask
  sensor_msgs__msg__Image mask;
} weedbot_interfaces__msg__WeedDetection;

// Struct for a sequence of weedbot_interfaces__msg__WeedDetection.
typedef struct weedbot_interfaces__msg__WeedDetection__Sequence
{
  weedbot_interfaces__msg__WeedDetection * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} weedbot_interfaces__msg__WeedDetection__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_H_
