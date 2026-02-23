// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_detection.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'mask'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__weedbot_interfaces__msg__WeedDetection __attribute__((deprecated))
#else
# define DEPRECATED__weedbot_interfaces__msg__WeedDetection __declspec(deprecated)
#endif

namespace weedbot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WeedDetection_
{
  using Type = WeedDetection_<ContainerAllocator>;

  explicit WeedDetection_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    mask(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->real_world_x = 0.0f;
      this->real_world_y = 0.0f;
      this->real_world_z = 0.0f;
    }
  }

  explicit WeedDetection_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    mask(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->real_world_x = 0.0f;
      this->real_world_y = 0.0f;
      this->real_world_z = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _bbox_x_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bbox_x_type bbox_x;
  using _bbox_y_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bbox_y_type bbox_y;
  using _bbox_w_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bbox_w_type bbox_w;
  using _bbox_h_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _bbox_h_type bbox_h;
  using _confidences_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _confidences_type confidences;
  using _class_ids_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _class_ids_type class_ids;
  using _real_world_x_type =
    float;
  _real_world_x_type real_world_x;
  using _real_world_y_type =
    float;
  _real_world_y_type real_world_y;
  using _real_world_z_type =
    float;
  _real_world_z_type real_world_z;
  using _mask_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _mask_type mask;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__bbox_x(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bbox_x = _arg;
    return *this;
  }
  Type & set__bbox_y(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bbox_y = _arg;
    return *this;
  }
  Type & set__bbox_w(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bbox_w = _arg;
    return *this;
  }
  Type & set__bbox_h(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->bbox_h = _arg;
    return *this;
  }
  Type & set__confidences(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->confidences = _arg;
    return *this;
  }
  Type & set__class_ids(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->class_ids = _arg;
    return *this;
  }
  Type & set__real_world_x(
    const float & _arg)
  {
    this->real_world_x = _arg;
    return *this;
  }
  Type & set__real_world_y(
    const float & _arg)
  {
    this->real_world_y = _arg;
    return *this;
  }
  Type & set__real_world_z(
    const float & _arg)
  {
    this->real_world_z = _arg;
    return *this;
  }
  Type & set__mask(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->mask = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> *;
  using ConstRawPtr =
    const weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__weedbot_interfaces__msg__WeedDetection
    std::shared_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__weedbot_interfaces__msg__WeedDetection
    std::shared_ptr<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WeedDetection_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->bbox_x != other.bbox_x) {
      return false;
    }
    if (this->bbox_y != other.bbox_y) {
      return false;
    }
    if (this->bbox_w != other.bbox_w) {
      return false;
    }
    if (this->bbox_h != other.bbox_h) {
      return false;
    }
    if (this->confidences != other.confidences) {
      return false;
    }
    if (this->class_ids != other.class_ids) {
      return false;
    }
    if (this->real_world_x != other.real_world_x) {
      return false;
    }
    if (this->real_world_y != other.real_world_y) {
      return false;
    }
    if (this->real_world_z != other.real_world_z) {
      return false;
    }
    if (this->mask != other.mask) {
      return false;
    }
    return true;
  }
  bool operator!=(const WeedDetection_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WeedDetection_

// alias to use template instance with default allocator
using WeedDetection =
  weedbot_interfaces::msg::WeedDetection_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace weedbot_interfaces

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_DETECTION__STRUCT_HPP_
