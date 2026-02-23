// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from weedbot_interfaces:msg/WeedArray.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "weedbot_interfaces/msg/weed_array.hpp"


#ifndef WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_HPP_
#define WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_HPP_

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
// Member 'detections'
#include "weedbot_interfaces/msg/detail/weed_detection__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__weedbot_interfaces__msg__WeedArray __attribute__((deprecated))
#else
# define DEPRECATED__weedbot_interfaces__msg__WeedArray __declspec(deprecated)
#endif

namespace weedbot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WeedArray_
{
  using Type = WeedArray_<ContainerAllocator>;

  explicit WeedArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->total_weeds = 0l;
      this->inference_time_ms = 0.0;
    }
  }

  explicit WeedArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->total_weeds = 0l;
      this->inference_time_ms = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _detections_type =
    std::vector<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>>;
  _detections_type detections;
  using _total_weeds_type =
    int32_t;
  _total_weeds_type total_weeds;
  using _inference_time_ms_type =
    double;
  _inference_time_ms_type inference_time_ms;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__detections(
    const std::vector<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<weedbot_interfaces::msg::WeedDetection_<ContainerAllocator>>> & _arg)
  {
    this->detections = _arg;
    return *this;
  }
  Type & set__total_weeds(
    const int32_t & _arg)
  {
    this->total_weeds = _arg;
    return *this;
  }
  Type & set__inference_time_ms(
    const double & _arg)
  {
    this->inference_time_ms = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    weedbot_interfaces::msg::WeedArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const weedbot_interfaces::msg::WeedArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      weedbot_interfaces::msg::WeedArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      weedbot_interfaces::msg::WeedArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__weedbot_interfaces__msg__WeedArray
    std::shared_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__weedbot_interfaces__msg__WeedArray
    std::shared_ptr<weedbot_interfaces::msg::WeedArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WeedArray_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->detections != other.detections) {
      return false;
    }
    if (this->total_weeds != other.total_weeds) {
      return false;
    }
    if (this->inference_time_ms != other.inference_time_ms) {
      return false;
    }
    return true;
  }
  bool operator!=(const WeedArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WeedArray_

// alias to use template instance with default allocator
using WeedArray =
  weedbot_interfaces::msg::WeedArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace weedbot_interfaces

#endif  // WEEDBOT_INTERFACES__MSG__DETAIL__WEED_ARRAY__STRUCT_HPP_
