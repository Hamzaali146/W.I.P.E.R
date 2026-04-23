// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice
#include "weedbot_interfaces/msg/detail/weed_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `detections`
#include "weedbot_interfaces/msg/detail/weed_detection__functions.h"

bool
weedbot_interfaces__msg__WeedArray__init(weedbot_interfaces__msg__WeedArray * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    weedbot_interfaces__msg__WeedArray__fini(msg);
    return false;
  }
  // detections
  if (!weedbot_interfaces__msg__WeedDetection__Sequence__init(&msg->detections, 0)) {
    weedbot_interfaces__msg__WeedArray__fini(msg);
    return false;
  }
  // total_weeds
  // inference_time_ms
  return true;
}

void
weedbot_interfaces__msg__WeedArray__fini(weedbot_interfaces__msg__WeedArray * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // detections
  weedbot_interfaces__msg__WeedDetection__Sequence__fini(&msg->detections);
  // total_weeds
  // inference_time_ms
}

bool
weedbot_interfaces__msg__WeedArray__are_equal(const weedbot_interfaces__msg__WeedArray * lhs, const weedbot_interfaces__msg__WeedArray * rhs)
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
  // detections
  if (!weedbot_interfaces__msg__WeedDetection__Sequence__are_equal(
      &(lhs->detections), &(rhs->detections)))
  {
    return false;
  }
  // total_weeds
  if (lhs->total_weeds != rhs->total_weeds) {
    return false;
  }
  // inference_time_ms
  if (lhs->inference_time_ms != rhs->inference_time_ms) {
    return false;
  }
  return true;
}

bool
weedbot_interfaces__msg__WeedArray__copy(
  const weedbot_interfaces__msg__WeedArray * input,
  weedbot_interfaces__msg__WeedArray * output)
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
  // detections
  if (!weedbot_interfaces__msg__WeedDetection__Sequence__copy(
      &(input->detections), &(output->detections)))
  {
    return false;
  }
  // total_weeds
  output->total_weeds = input->total_weeds;
  // inference_time_ms
  output->inference_time_ms = input->inference_time_ms;
  return true;
}

weedbot_interfaces__msg__WeedArray *
weedbot_interfaces__msg__WeedArray__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedArray * msg = (weedbot_interfaces__msg__WeedArray *)allocator.allocate(sizeof(weedbot_interfaces__msg__WeedArray), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(weedbot_interfaces__msg__WeedArray));
  bool success = weedbot_interfaces__msg__WeedArray__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
weedbot_interfaces__msg__WeedArray__destroy(weedbot_interfaces__msg__WeedArray * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    weedbot_interfaces__msg__WeedArray__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
weedbot_interfaces__msg__WeedArray__Sequence__init(weedbot_interfaces__msg__WeedArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedArray * data = NULL;

  if (size) {
    data = (weedbot_interfaces__msg__WeedArray *)allocator.zero_allocate(size, sizeof(weedbot_interfaces__msg__WeedArray), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = weedbot_interfaces__msg__WeedArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        weedbot_interfaces__msg__WeedArray__fini(&data[i - 1]);
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
weedbot_interfaces__msg__WeedArray__Sequence__fini(weedbot_interfaces__msg__WeedArray__Sequence * array)
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
      weedbot_interfaces__msg__WeedArray__fini(&array->data[i]);
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

weedbot_interfaces__msg__WeedArray__Sequence *
weedbot_interfaces__msg__WeedArray__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  weedbot_interfaces__msg__WeedArray__Sequence * array = (weedbot_interfaces__msg__WeedArray__Sequence *)allocator.allocate(sizeof(weedbot_interfaces__msg__WeedArray__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = weedbot_interfaces__msg__WeedArray__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
weedbot_interfaces__msg__WeedArray__Sequence__destroy(weedbot_interfaces__msg__WeedArray__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    weedbot_interfaces__msg__WeedArray__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
weedbot_interfaces__msg__WeedArray__Sequence__are_equal(const weedbot_interfaces__msg__WeedArray__Sequence * lhs, const weedbot_interfaces__msg__WeedArray__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!weedbot_interfaces__msg__WeedArray__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
weedbot_interfaces__msg__WeedArray__Sequence__copy(
  const weedbot_interfaces__msg__WeedArray__Sequence * input,
  weedbot_interfaces__msg__WeedArray__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(weedbot_interfaces__msg__WeedArray);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    weedbot_interfaces__msg__WeedArray * data =
      (weedbot_interfaces__msg__WeedArray *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!weedbot_interfaces__msg__WeedArray__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          weedbot_interfaces__msg__WeedArray__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!weedbot_interfaces__msg__WeedArray__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
