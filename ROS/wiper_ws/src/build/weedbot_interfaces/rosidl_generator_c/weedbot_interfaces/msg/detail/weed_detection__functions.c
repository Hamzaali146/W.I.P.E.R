// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice
#include "weedbot_interfaces/msg/detail/weed_detection__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `bbox_x`
// Member `bbox_y`
// Member `bbox_w`
// Member `bbox_h`
// Member `confidences`
// Member `class_ids`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `mask`
#include "sensor_msgs/msg/detail/image__functions.h"

bool
weedbot_interfaces__msg__WeedDetection__init(weedbot_interfaces__msg__WeedDetection * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // bbox_x
  if (!rosidl_runtime_c__float__Sequence__init(&msg->bbox_x, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // bbox_y
  if (!rosidl_runtime_c__float__Sequence__init(&msg->bbox_y, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // bbox_w
  if (!rosidl_runtime_c__float__Sequence__init(&msg->bbox_w, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // bbox_h
  if (!rosidl_runtime_c__float__Sequence__init(&msg->bbox_h, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // confidences
  if (!rosidl_runtime_c__float__Sequence__init(&msg->confidences, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // class_ids
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->class_ids, 0)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  // real_world_x
  // real_world_y
  // real_world_z
  // mask
  if (!sensor_msgs__msg__Image__init(&msg->mask)) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
    return false;
  }
  return true;
}

void
weedbot_interfaces__msg__WeedDetection__fini(weedbot_interfaces__msg__WeedDetection * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // bbox_x
  rosidl_runtime_c__float__Sequence__fini(&msg->bbox_x);
  // bbox_y
  rosidl_runtime_c__float__Sequence__fini(&msg->bbox_y);
  // bbox_w
  rosidl_runtime_c__float__Sequence__fini(&msg->bbox_w);
  // bbox_h
  rosidl_runtime_c__float__Sequence__fini(&msg->bbox_h);
  // confidences
  rosidl_runtime_c__float__Sequence__fini(&msg->confidences);
  // class_ids
  rosidl_runtime_c__int32__Sequence__fini(&msg->class_ids);
  // real_world_x
  // real_world_y
  // real_world_z
  // mask
  sensor_msgs__msg__Image__fini(&msg->mask);
}

bool
weedbot_interfaces__msg__WeedDetection__are_equal(const weedbot_interfaces__msg__WeedDetection * lhs, const weedbot_interfaces__msg__WeedDetection * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // bbox_x
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->bbox_x), &(rhs->bbox_x)))
  {
    return false;
  }
  // bbox_y
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->bbox_y), &(rhs->bbox_y)))
  {
    return false;
  }
  // bbox_w
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->bbox_w), &(rhs->bbox_w)))
  {
    return false;
  }
  // bbox_h
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->bbox_h), &(rhs->bbox_h)))
  {
    return false;
  }
  // confidences
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->confidences), &(rhs->confidences)))
  {
    return false;
  }
  // class_ids
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->class_ids), &(rhs->class_ids)))
  {
    return false;
  }
  // real_world_x
  if (lhs->real_world_x != rhs->real_world_x) {
    return false;
  }
  // real_world_y
  if (lhs->real_world_y != rhs->real_world_y) {
    return false;
  }
  // real_world_z
  if (lhs->real_world_z != rhs->real_world_z) {
    return false;
  }
  // mask
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->mask), &(rhs->mask)))
  {
    return false;
  }
  return true;
}

bool
weedbot_interfaces__msg__WeedDetection__copy(
  const weedbot_interfaces__msg__WeedDetection * input,
  weedbot_interfaces__msg__WeedDetection * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // bbox_x
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->bbox_x), &(output->bbox_x)))
  {
    return false;
  }
  // bbox_y
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->bbox_y), &(output->bbox_y)))
  {
    return false;
  }
  // bbox_w
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->bbox_w), &(output->bbox_w)))
  {
    return false;
  }
  // bbox_h
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->bbox_h), &(output->bbox_h)))
  {
    return false;
  }
  // confidences
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->confidences), &(output->confidences)))
  {
    return false;
  }
  // class_ids
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->class_ids), &(output->class_ids)))
  {
    return false;
  }
  // real_world_x
  output->real_world_x = input->real_world_x;
  // real_world_y
  output->real_world_y = input->real_world_y;
  // real_world_z
  output->real_world_z = input->real_world_z;
  // mask
  if (!sensor_msgs__msg__Image__copy(
      &(input->mask), &(output->mask)))
  {
    return false;
  }
  return true;
}

weedbot_interfaces__msg__WeedDetection *
weedbot_interfaces__msg__WeedDetection__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedDetection * msg = (weedbot_interfaces__msg__WeedDetection *)allocator.allocate(sizeof(weedbot_interfaces__msg__WeedDetection), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(weedbot_interfaces__msg__WeedDetection));
  bool success = weedbot_interfaces__msg__WeedDetection__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
weedbot_interfaces__msg__WeedDetection__destroy(weedbot_interfaces__msg__WeedDetection * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    weedbot_interfaces__msg__WeedDetection__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
weedbot_interfaces__msg__WeedDetection__Sequence__init(weedbot_interfaces__msg__WeedDetection__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedDetection * data = NULL;

  if (size) {
    data = (weedbot_interfaces__msg__WeedDetection *)allocator.zero_allocate(size, sizeof(weedbot_interfaces__msg__WeedDetection), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = weedbot_interfaces__msg__WeedDetection__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        weedbot_interfaces__msg__WeedDetection__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
weedbot_interfaces__msg__WeedDetection__Sequence__fini(weedbot_interfaces__msg__WeedDetection__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      weedbot_interfaces__msg__WeedDetection__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

weedbot_interfaces__msg__WeedDetection__Sequence *
weedbot_interfaces__msg__WeedDetection__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedDetection__Sequence * array = (weedbot_interfaces__msg__WeedDetection__Sequence *)allocator.allocate(sizeof(weedbot_interfaces__msg__WeedDetection__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = weedbot_interfaces__msg__WeedDetection__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
weedbot_interfaces__msg__WeedDetection__Sequence__destroy(weedbot_interfaces__msg__WeedDetection__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    weedbot_interfaces__msg__WeedDetection__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
weedbot_interfaces__msg__WeedDetection__Sequence__are_equal(const weedbot_interfaces__msg__WeedDetection__Sequence * lhs, const weedbot_interfaces__msg__WeedDetection__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!weedbot_interfaces__msg__WeedDetection__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
weedbot_interfaces__msg__WeedDetection__Sequence__copy(
  const weedbot_interfaces__msg__WeedDetection__Sequence * input,
  weedbot_interfaces__msg__WeedDetection__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(weedbot_interfaces__msg__WeedDetection);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    weedbot_interfaces__msg__WeedDetection * data =
      (weedbot_interfaces__msg__WeedDetection *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!weedbot_interfaces__msg__WeedDetection__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          weedbot_interfaces__msg__WeedDetection__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!weedbot_interfaces__msg__WeedDetection__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
