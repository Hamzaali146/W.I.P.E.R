#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to weedbot_interfaces__msg__WeedDetection

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WeedDetection {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// Pixel coordinates (normalized 0-1)
    /// Bounding box x coordinates
    pub bbox_x: Vec<f32>,

    /// Bounding box y coordinates
    pub bbox_y: Vec<f32>,

    /// Bounding box widths
    pub bbox_w: Vec<f32>,

    /// Bounding box heights
    pub bbox_h: Vec<f32>,

    /// Detection confidences
    pub confidences: Vec<f32>,

    /// Class IDs (if multiple weed types)
    pub class_ids: Vec<i32>,

    /// NEW: Real-world coordinates (meters, relative to camera center on ground)
    /// X position in meters (+ = right, - = left)
    pub real_world_x: f32,

    /// Y position in meters (+ = forward, - = backward)
    pub real_world_y: f32,

    /// Z position in meters (0 = ground plane)
    pub real_world_z: f32,

    /// Optional segmentation mask
    pub mask: sensor_msgs::msg::Image,

}



impl Default for WeedDetection {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::WeedDetection::default())
  }
}

impl rosidl_runtime_rs::Message for WeedDetection {
  type RmwMsg = super::msg::rmw::WeedDetection;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        bbox_x: msg.bbox_x.into(),
        bbox_y: msg.bbox_y.into(),
        bbox_w: msg.bbox_w.into(),
        bbox_h: msg.bbox_h.into(),
        confidences: msg.confidences.into(),
        class_ids: msg.class_ids.into(),
        real_world_x: msg.real_world_x,
        real_world_y: msg.real_world_y,
        real_world_z: msg.real_world_z,
        mask: sensor_msgs::msg::Image::into_rmw_message(std::borrow::Cow::Owned(msg.mask)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        bbox_x: msg.bbox_x.as_slice().into(),
        bbox_y: msg.bbox_y.as_slice().into(),
        bbox_w: msg.bbox_w.as_slice().into(),
        bbox_h: msg.bbox_h.as_slice().into(),
        confidences: msg.confidences.as_slice().into(),
        class_ids: msg.class_ids.as_slice().into(),
      real_world_x: msg.real_world_x,
      real_world_y: msg.real_world_y,
      real_world_z: msg.real_world_z,
        mask: sensor_msgs::msg::Image::into_rmw_message(std::borrow::Cow::Borrowed(&msg.mask)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      bbox_x: msg.bbox_x
          .into_iter()
          .collect(),
      bbox_y: msg.bbox_y
          .into_iter()
          .collect(),
      bbox_w: msg.bbox_w
          .into_iter()
          .collect(),
      bbox_h: msg.bbox_h
          .into_iter()
          .collect(),
      confidences: msg.confidences
          .into_iter()
          .collect(),
      class_ids: msg.class_ids
          .into_iter()
          .collect(),
      real_world_x: msg.real_world_x,
      real_world_y: msg.real_world_y,
      real_world_z: msg.real_world_z,
      mask: sensor_msgs::msg::Image::from_rmw_message(msg.mask),
    }
  }
}


// Corresponds to weedbot_interfaces__msg__WeedArray

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WeedArray {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub detections: Vec<super::msg::WeedDetection>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub total_weeds: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub inference_time_ms: f64,

}



impl Default for WeedArray {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::WeedArray::default())
  }
}

impl rosidl_runtime_rs::Message for WeedArray {
  type RmwMsg = super::msg::rmw::WeedArray;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        detections: msg.detections
          .into_iter()
          .map(|elem| super::msg::WeedDetection::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        total_weeds: msg.total_weeds,
        inference_time_ms: msg.inference_time_ms,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        detections: msg.detections
          .iter()
          .map(|elem| super::msg::WeedDetection::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      total_weeds: msg.total_weeds,
      inference_time_ms: msg.inference_time_ms,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      detections: msg.detections
          .into_iter()
          .map(super::msg::WeedDetection::from_rmw_message)
          .collect(),
      total_weeds: msg.total_weeds,
      inference_time_ms: msg.inference_time_ms,
    }
  }
}


