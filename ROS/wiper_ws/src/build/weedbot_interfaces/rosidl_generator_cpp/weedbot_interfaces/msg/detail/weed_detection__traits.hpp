// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_detection.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__TRAITS_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "weedbot_interfaces/msg/detail/weed_detection__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'mask'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace weedbot_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const WeedDetection & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: bbox_x
  {
    if (msg.bbox_x.size() == 0) {
      out << "bbox_x: []";
    } else {
      out << "bbox_x: [";
      size_t pending_items = msg.bbox_x.size();
      for (auto item : msg.bbox_x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: bbox_y
  {
    if (msg.bbox_y.size() == 0) {
      out << "bbox_y: []";
    } else {
      out << "bbox_y: [";
      size_t pending_items = msg.bbox_y.size();
      for (auto item : msg.bbox_y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: bbox_w
  {
    if (msg.bbox_w.size() == 0) {
      out << "bbox_w: []";
    } else {
      out << "bbox_w: [";
      size_t pending_items = msg.bbox_w.size();
      for (auto item : msg.bbox_w) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: bbox_h
  {
    if (msg.bbox_h.size() == 0) {
      out << "bbox_h: []";
    } else {
      out << "bbox_h: [";
      size_t pending_items = msg.bbox_h.size();
      for (auto item : msg.bbox_h) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: confidences
  {
    if (msg.confidences.size() == 0) {
      out << "confidences: []";
    } else {
      out << "confidences: [";
      size_t pending_items = msg.confidences.size();
      for (auto item : msg.confidences) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: class_ids
  {
    if (msg.class_ids.size() == 0) {
      out << "class_ids: []";
    } else {
      out << "class_ids: [";
      size_t pending_items = msg.class_ids.size();
      for (auto item : msg.class_ids) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: real_world_x
  {
    out << "real_world_x: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_x, out);
    out << ", ";
  }

  // member: real_world_y
  {
    out << "real_world_y: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_y, out);
    out << ", ";
  }

  // member: real_world_z
  {
    out << "real_world_z: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_z, out);
    out << ", ";
  }

  // member: mask
  {
    out << "mask: ";
    to_flow_style_yaml(msg.mask, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WeedDetection & msg,
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

  // member: bbox_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bbox_x.size() == 0) {
      out << "bbox_x: []\n";
    } else {
      out << "bbox_x:\n";
      for (auto item : msg.bbox_x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: bbox_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bbox_y.size() == 0) {
      out << "bbox_y: []\n";
    } else {
      out << "bbox_y:\n";
      for (auto item : msg.bbox_y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: bbox_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bbox_w.size() == 0) {
      out << "bbox_w: []\n";
    } else {
      out << "bbox_w:\n";
      for (auto item : msg.bbox_w) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: bbox_h
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bbox_h.size() == 0) {
      out << "bbox_h: []\n";
    } else {
      out << "bbox_h:\n";
      for (auto item : msg.bbox_h) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: confidences
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.confidences.size() == 0) {
      out << "confidences: []\n";
    } else {
      out << "confidences:\n";
      for (auto item : msg.confidences) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: class_ids
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.class_ids.size() == 0) {
      out << "class_ids: []\n";
    } else {
      out << "class_ids:\n";
      for (auto item : msg.class_ids) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: real_world_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "real_world_x: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_x, out);
    out << "\n";
  }

  // member: real_world_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "real_world_y: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_y, out);
    out << "\n";
  }

  // member: real_world_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "real_world_z: ";
    rosidl_generator_traits::value_to_yaml(msg.real_world_z, out);
    out << "\n";
  }

  // member: mask
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mask:\n";
    to_block_style_yaml(msg.mask, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WeedDetection & msg, bool use_flow_style = false)
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
  const weedbot_interfaces::msg::WeedDetection & msg,
  std::ostream & out, size_t indentation = 0)
{
  weedbot_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use weedbot_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const weedbot_interfaces::msg::WeedDetection & msg)
{
  return weedbot_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<weedbot_interfaces::msg::WeedDetection>()
{
  return "weedbot_interfaces::msg::WeedDetection";
}

template<>
inline const char * name<weedbot_interfaces::msg::WeedDetection>()
{
  return "weedbot_interfaces/msg/WeedDetection";
}

template<>
struct has_fixed_size<weedbot_interfaces::msg::WeedDetection>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<weedbot_interfaces::msg::WeedDetection>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<weedbot_interfaces::msg::WeedDetection>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__TRAITS_HPP_
