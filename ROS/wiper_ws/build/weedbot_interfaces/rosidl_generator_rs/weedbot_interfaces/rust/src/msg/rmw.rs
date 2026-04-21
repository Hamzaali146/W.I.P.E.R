#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "weedbot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__weedbot_interfaces__msg__WeedDetection() -> *const std::ffi::c_void;
}

#[link(name = "weedbot_interfaces__rosidl_generator_c")]
extern "C" {
    fn weedbot_interfaces__msg__WeedDetection__init(msg: *mut WeedDetection) -> bool;
    fn weedbot_interfaces__msg__WeedDetection__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<WeedDetection>, size: usize) -> bool;
    fn weedbot_interfaces__msg__WeedDetection__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<WeedDetection>);
    fn weedbot_interfaces__msg__WeedDetection__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<WeedDetection>, out_seq: *mut rosidl_runtime_rs::Sequence<WeedDetection>) -> bool;
}

// Corresponds to weedbot_interfaces__msg__WeedDetection
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WeedDetection {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,

    /// Pixel coordinates (normalized 0-1)
    /// Bounding box x coordinates
    pub bbox_x: rosidl_runtime_rs::Sequence<f32>,

    /// Bounding box y coordinates
    pub bbox_y: rosidl_runtime_rs::Sequence<f32>,

    /// Bounding box widths
    pub bbox_w: rosidl_runtime_rs::Sequence<f32>,

    /// Bounding box heights
    pub bbox_h: rosidl_runtime_rs::Sequence<f32>,

    /// Detection confidences
    pub confidences: rosidl_runtime_rs::Sequence<f32>,

    /// Class IDs (if multiple weed types)
    pub class_ids: rosidl_runtime_rs::Sequence<i32>,

    /// NEW: Real-world coordinates (meters, relative to camera center on ground)
    /// X position in meters (+ = right, - = left)
    pub real_world_x: f32,

    /// Y position in meters (+ = forward, - = backward)
    pub real_world_y: f32,

    /// Z position in meters (0 = ground plane)
    pub real_world_z: f32,

    /// Optional segmentation mask
    pub mask: sensor_msgs::msg::rmw::Image,

}



impl Default for WeedDetection {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !weedbot_interfaces__msg__WeedDetection__init(&mut msg as *mut _) {
        panic!("Call to weedbot_interfaces__msg__WeedDetection__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for WeedDetection {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedDetection__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedDetection__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedDetection__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for WeedDetection {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for WeedDetection where Self: Sized {
  const TYPE_NAME: &'static str = "weedbot_interfaces/msg/WeedDetection";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__weedbot_interfaces__msg__WeedDetection() }
  }
}


#[link(name = "weedbot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__weedbot_interfaces__msg__WeedArray() -> *const std::ffi::c_void;
}

#[link(name = "weedbot_interfaces__rosidl_generator_c")]
extern "C" {
    fn weedbot_interfaces__msg__WeedArray__init(msg: *mut WeedArray) -> bool;
    fn weedbot_interfaces__msg__WeedArray__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<WeedArray>, size: usize) -> bool;
    fn weedbot_interfaces__msg__WeedArray__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<WeedArray>);
    fn weedbot_interfaces__msg__WeedArray__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<WeedArray>, out_seq: *mut rosidl_runtime_rs::Sequence<WeedArray>) -> bool;
}

// Corresponds to weedbot_interfaces__msg__WeedArray
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WeedArray {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub detections: rosidl_runtime_rs::Sequence<super::super::msg::rmw::WeedDetection>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub total_weeds: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub inference_time_ms: f64,

}



impl Default for WeedArray {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !weedbot_interfaces__msg__WeedArray__init(&mut msg as *mut _) {
        panic!("Call to weedbot_interfaces__msg__WeedArray__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for WeedArray {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedArray__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedArray__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { weedbot_interfaces__msg__WeedArray__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for WeedArray {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for WeedArray where Self: Sized {
  const TYPE_NAME: &'static str = "weedbot_interfaces/msg/WeedArray";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__weedbot_interfaces__msg__WeedArray() }
  }
}


