// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_array.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__TRAITS_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "weedbot_interfaces/msg/detail/weed_array__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'detections'
#include "weedbot_interfaces/msg/detail/weed_detection__traits.hpp"

namespace weedbot_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const WeedArray & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: detections
  {
    if (msg.detections.size() == 0) {
      out << "detections: []";
    } else {
      out << "detections: [";
      size_t pending_items = msg.detections.size();
      for (auto item : msg.detections) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: total_weeds
  {
    out << "total_weeds: ";
    rosidl_generator_traits::value_to_yaml(msg.total_weeds, out);
    out << ", ";
  }

  // member: inference_time_ms
  {
    out << "inference_time_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.inference_time_ms, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WeedArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: detections
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.detections.size() == 0) {
      out << "detections: []\n";
    } else {
      out << "detections:\n";
      for (auto item : msg.detections) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: total_weeds
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "total_weeds: ";
    rosidl_generator_traits::value_to_yaml(msg.total_weeds, out);
    out << "\n";
  }

  // member: inference_time_ms
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "inference_time_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.inference_time_ms, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WeedArray & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace weedbot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use weedbot_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const weedbot_interfaces::msg::WeedArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  weedbot_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use weedbot_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const weedbot_interfaces::msg::WeedArray & msg)
{
  return weedbot_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<weedbot_interfaces::msg::WeedArray>()
{
  return "weedbot_interfaces::msg::WeedArray";
}

template<>
inline const char * name<weedbot_interfaces::msg::WeedArray>()
{
  return "weedbot_interfaces/msg/WeedArray";
}

template<>
struct has_fixed_size<weedbot_interfaces::msg::WeedArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<weedbot_interfaces::msg::WeedArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<weedbot_interfaces::msg::WeedArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__TRAITS_HPP_
