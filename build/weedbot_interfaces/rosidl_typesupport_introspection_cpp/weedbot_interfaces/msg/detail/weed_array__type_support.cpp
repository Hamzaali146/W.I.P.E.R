// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "weedbot_interfaces/msg/detail/weed_array__functions.h"
#include "weedbot_interfaces/msg/detail/weed_array__struct.hpp"
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

void WeedArray_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) weedbot_interfaces::msg::WeedArray(_init);
}

void WeedArray_fini_function(void * message_memory)
{
  auto typed_message = static_cast<weedbot_interfaces::msg::WeedArray *>(message_memory);
  typed_message->~WeedArray();
}

size_t size_function__WeedArray__detections(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<weedbot_interfaces::msg::WeedDetection> *>(untyped_member);
  return member->size();
}

const void * get_const_function__WeedArray__detections(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<weedbot_interfaces::msg::WeedDetection> *>(untyped_member);
  return &member[index];
}

void * get_function__WeedArray__detections(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<weedbot_interfaces::msg::WeedDetection> *>(untyped_member);
  return &member[index];
}

void fetch_function__WeedArray__detections(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const weedbot_interfaces::msg::WeedDetection *>(
    get_const_function__WeedArray__detections(untyped_member, index));
  auto & value = *reinterpret_cast<weedbot_interfaces::msg::WeedDetection *>(untyped_value);
  value = item;
}

void assign_function__WeedArray__detections(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<weedbot_interfaces::msg::WeedDetection *>(
    get_function__WeedArray__detections(untyped_member, index));
  const auto & value = *reinterpret_cast<const weedbot_interfaces::msg::WeedDetection *>(untyped_value);
  item = value;
}

void resize_function__WeedArray__detections(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<weedbot_interfaces::msg::WeedDetection> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember WeedArray_message_member_array[4] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedArray, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "detections",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<weedbot_interfaces::msg::WeedDetection>(),  // members of sub message
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedArray, detections),  // bytes offset in struct
    nullptr,  // default value
    size_function__WeedArray__detections,  // size() function pointer
    get_const_function__WeedArray__detections,  // get_const(index) function pointer
    get_function__WeedArray__detections,  // get(index) function pointer
    fetch_function__WeedArray__detections,  // fetch(index, &value) function pointer
    assign_function__WeedArray__detections,  // assign(index, value) function pointer
    resize_function__WeedArray__detections  // resize(index) function pointer
  },
  {
    "total_weeds",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedArray, total_weeds),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "inference_time_ms",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(weedbot_interfaces::msg::WeedArray, inference_time_ms),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers WeedArray_message_members = {
  "weedbot_interfaces::msg",  // message namespace
  "WeedArray",  // message name
  4,  // number of fields
  sizeof(weedbot_interfaces::msg::WeedArray),
  false,  // has_any_key_member_
  WeedArray_message_member_array,  // message members
  WeedArray_init_function,  // function to initialize message memory (memory has to be allocated)
  WeedArray_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t WeedArray_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &WeedArray_message_members,
  get_message_typesupport_handle_function,
  &weedbot_interfaces__msg__WeedArray__get_type_hash,
  &weedbot_interfaces__msg__WeedArray__get_type_description,
  &weedbot_interfaces__msg__WeedArray__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace weedbot_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<weedbot_interfaces::msg::WeedArray>()
{
  return &::weedbot_interfaces::msg::rosidl_typesupport_introspection_cpp::WeedArray_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, weedbot_interfaces, msg, WeedArray)() {
  return &::weedbot_interfaces::msg::rosidl_typesupport_introspection_cpp::WeedArray_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
