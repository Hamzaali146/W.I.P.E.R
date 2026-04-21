// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "weedbot_interfaces/msg/detail/weed_detection__functions.h"
#include "weedbot_interfaces/msg/detail/weed_detection__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace weedbot_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void WeedDetection_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) weedbot_interfaces::msg::WeedDetection(_init);
}

void WeedDetection_fini_function(void * message_memory)
{
  auto typed_message = static_cast<weedbot_interfaces::msg::WeedDetection *>(message_memory);
  typed_message->~WeedDetection();
}

size_t size_function__WeedDetection__bbox_x(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__bbox_x(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__bbox_x(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__bbox_x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__WeedDetection__bbox_x(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__bbox_x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__WeedDetection__bbox_x(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__bbox_x(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__WeedDetection__bbox_y(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__bbox_y(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__bbox_y(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__bbox_y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__WeedDetection__bbox_y(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__bbox_y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__WeedDetection__bbox_y(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__bbox_y(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__WeedDetection__bbox_w(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__bbox_w(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__bbox_w(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__bbox_w(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__WeedDetection__bbox_w(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__bbox_w(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__WeedDetection__bbox_w(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__bbox_w(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__WeedDetection__bbox_h(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__bbox_h(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__bbox_h(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__bbox_h(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__WeedDetection__bbox_h(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__bbox_h(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__WeedDetection__bbox_h(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__bbox_h(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__WeedDetection__confidences(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__confidences(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__confidences(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__confidences(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__WeedDetection__confidences(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__confidences(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__WeedDetection__confidences(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__confidences(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__WeedDetection__class_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedDetection__class_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedDetection__class_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedDetection__class_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__WeedDetection__class_ids(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__WeedDetection__class_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__WeedDetection__class_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__WeedDetection__class_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember WeedDetection_message_member_array[11] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "bbox_x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, bbox_x),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__bbox_x,  // size() function pointer
    get_const_function__WeedDetection__bbox_x,  // get_const(index) function pointer
    get_function__WeedDetection__bbox_x,  // get(index) function pointer
    fetch_function__WeedDetection__bbox_x,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__bbox_x,  // assign(index, value) function pointer
    resize_function__WeedDetection__bbox_x  // resize(index) function pointer
  },
  {
    "bbox_y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, bbox_y),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__bbox_y,  // size() function pointer
    get_const_function__WeedDetection__bbox_y,  // get_const(index) function pointer
    get_function__WeedDetection__bbox_y,  // get(index) function pointer
    fetch_function__WeedDetection__bbox_y,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__bbox_y,  // assign(index, value) function pointer
    resize_function__WeedDetection__bbox_y  // resize(index) function pointer
  },
  {
    "bbox_w",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, bbox_w),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__bbox_w,  // size() function pointer
    get_const_function__WeedDetection__bbox_w,  // get_const(index) function pointer
    get_function__WeedDetection__bbox_w,  // get(index) function pointer
    fetch_function__WeedDetection__bbox_w,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__bbox_w,  // assign(index, value) function pointer
    resize_function__WeedDetection__bbox_w  // resize(index) function pointer
  },
  {
    "bbox_h",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, bbox_h),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__bbox_h,  // size() function pointer
    get_const_function__WeedDetection__bbox_h,  // get_const(index) function pointer
    get_function__WeedDetection__bbox_h,  // get(index) function pointer
    fetch_function__WeedDetection__bbox_h,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__bbox_h,  // assign(index, value) function pointer
    resize_function__WeedDetection__bbox_h  // resize(index) function pointer
  },
  {
    "confidences",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, confidences),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__confidences,  // size() function pointer
    get_const_function__WeedDetection__confidences,  // get_const(index) function pointer
    get_function__WeedDetection__confidences,  // get(index) function pointer
    fetch_function__WeedDetection__confidences,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__confidences,  // assign(index, value) function pointer
    resize_function__WeedDetection__confidences  // resize(index) function pointer
  },
  {
    "class_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, class_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedDetection__class_ids,  // size() function pointer
    get_const_function__WeedDetection__class_ids,  // get_const(index) function pointer
    get_function__WeedDetection__class_ids,  // get(index) function pointer
    fetch_function__WeedDetection__class_ids,  // fetch(index, &value) function pointer
    assign_function__WeedDetection__class_ids,  // assign(index, value) function pointer
    resize_function__WeedDetection__class_ids  // resize(index) function pointer
  },
  {
    "real_world_x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, real_world_x),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "real_world_y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, real_world_y),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "real_world_z",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, real_world_z),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "mask",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sensor_msgs::msg::Image>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedDetection, mask),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers WeedDetection_message_members = {
  "weedbot_interfaces::msg",  // message namespace
  "WeedDetection",  // message name
  11,  // number of fields
  sizeof(weedbot_interfaces::msg::WeedDetection),
  false,  // has_any_key_member_
  WeedDetection_message_member_array,  // message members
  WeedDetection_init_function,  // function to initialize message memory (memory has to be allocated)
  WeedDetection_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t WeedDetection_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &WeedDetection_message_members,
  get_message_typesupport_handle_function,
  &weedbot_interfaces__msg__WeedDetection__get_type_hash,
  &weedbot_interfaces__msg__WeedDetection__get_type_description,
  &weedbot_interfaces__msg__WeedDetection__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace weedbot_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<weedbot_interfaces::msg::WeedDetection>()
{
  return &::weedbot_interfaces::msg::rosidl_typesupport_introspection_cpp::WeedDetection_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, weedbot_interfaces, msg, WeedDetection)() {
  return &::weedbot_interfaces::msg::rosidl_typesupport_introspection_cpp::WeedDetection_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
