// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "weedbot_interfaces/msg/detail/weed_detection__rosidl_typesupport_introspection_c.h"
#include "weedbot_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "weedbot_interfaces/msg/detail/weed_detection__functions.h"
#include "weedbot_interfaces/msg/detail/weed_detection__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `bbox_x`
// Member `bbox_y`
// Member `bbox_w`
// Member `bbox_h`
// Member `confidences`
// Member `class_ids`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `mask`
#include "sensor_msgs/msg/image.h"
// Member `mask`
#include "sensor_msgs/msg/detail/image__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  weedbot_interfaces__msg__WeedDetection__init(message_memory);
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_fini_function(void * message_memory)
{
  weedbot_interfaces__msg__WeedDetection__fini(message_memory);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_x(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_x(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_x(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_y(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_y(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_y(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_w(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_w(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_w(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_w(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_w(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_w(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_w(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_w(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_h(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_h(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_h(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_h(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_h(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_h(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_h(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_h(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__confidences(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__confidences(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__confidences(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__confidences(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__confidences(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__confidences(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__confidences(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__confidences(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__class_ids(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__class_ids(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__class_ids(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__class_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__class_ids(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__class_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__class_ids(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__class_ids(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_member_array[11] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "bbox_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, bbox_x),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_x,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_x,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_x,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_x,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_x,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_x  // resize(index) function pointer
  },
  {
    "bbox_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, bbox_y),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_y,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_y,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_y,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_y,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_y,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_y  // resize(index) function pointer
  },
  {
    "bbox_w",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, bbox_w),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_w,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_w,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_w,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_w,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_w,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_w  // resize(index) function pointer
  },
  {
    "bbox_h",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, bbox_h),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__bbox_h,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__bbox_h,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__bbox_h,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__bbox_h,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__bbox_h,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__bbox_h  // resize(index) function pointer
  },
  {
    "confidences",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, confidences),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__confidences,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__confidences,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__confidences,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__confidences,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__confidences,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__confidences  // resize(index) function pointer
  },
  {
    "class_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, class_ids),  // bytes offset in struct
    NULL,  // default value
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__size_function__WeedDetection__class_ids,  // size() function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_const_function__WeedDetection__class_ids,  // get_const(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__get_function__WeedDetection__class_ids,  // get(index) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__fetch_function__WeedDetection__class_ids,  // fetch(index, &value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__assign_function__WeedDetection__class_ids,  // assign(index, value) function pointer
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__resize_function__WeedDetection__class_ids  // resize(index) function pointer
  },
  {
    "real_world_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, real_world_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "real_world_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, real_world_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "real_world_z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, real_world_z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "mask",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces__msg__WeedDetection, mask),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_members = {
  "weedbot_interfaces__msg",  // message namespace
  "WeedDetection",  // message name
  11,  // number of fields
  sizeof(weedbot_interfaces__msg__WeedDetection),
  false,  // has_any_key_member_
  weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_member_array,  // message members
  weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_init_function,  // function to initialize message memory (memory has to be allocated)
  weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_type_support_handle = {
  0,
  &weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_members,
  get_message_typesupport_handle_function,
  &weedbot_interfaces__msg__WeedDetection__get_type_hash,
  &weedbot_interfaces__msg__WeedDetection__get_type_description,
  &weedbot_interfaces__msg__WeedDetection__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_weedbot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, weedbot_interfaces, msg, WeedDetection)() {
  weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_member_array[10].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sensor_msgs, msg, Image)();
  if (!weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_type_support_handle.typesupport_identifier) {
    weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &weedbot_interfaces__msg__WeedDetection__rosidl_typesupport_introspection_c__WeedDetection_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
