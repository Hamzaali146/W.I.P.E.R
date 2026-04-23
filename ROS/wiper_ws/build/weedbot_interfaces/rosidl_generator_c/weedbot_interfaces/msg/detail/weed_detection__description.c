// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from weedbot_interfaces:msg/WeedDetection.idl
// generated code does not contain a copyright notice

#include "weedbot_interfaces/msg/detail/weed_detection__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_weedbot_interfaces
const rosidl_type_hash_t *
weedbot_interfaces__msg__WeedDetection__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x1a, 0x5e, 0x80, 0xb6, 0xa1, 0x06, 0x55, 0x5e,
      0x5a, 0xd0, 0x8b, 0x95, 0x79, 0x9f, 0xc3, 0x7f,
      0x91, 0xc5, 0x79, 0xfe, 0x78, 0x4b, 0x7c, 0x37,
      0xf4, 0x14, 0x1b, 0xa1, 0x64, 0xc3, 0x44, 0x28,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "sensor_msgs/msg/detail/image__functions.h"
#include "std_msgs/msg/detail/header__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t sensor_msgs__msg__Image__EXPECTED_HASH = {1, {
    0xd3, 0x1d, 0x41, 0xa9, 0xa4, 0xc4, 0xbc, 0x8e,
    0xae, 0x9b, 0xe7, 0x57, 0xb0, 0xbe, 0xed, 0x30,
    0x65, 0x64, 0xf7, 0x52, 0x6c, 0x88, 0xea, 0x6a,
    0x45, 0x88, 0xfb, 0x95, 0x82, 0x52, 0x7d, 0x47,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char weedbot_interfaces__msg__WeedDetection__TYPE_NAME[] = "weedbot_interfaces/msg/WeedDetection";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char sensor_msgs__msg__Image__TYPE_NAME[] = "sensor_msgs/msg/Image";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__header[] = "header";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_x[] = "bbox_x";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_y[] = "bbox_y";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_w[] = "bbox_w";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_h[] = "bbox_h";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__confidences[] = "confidences";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__class_ids[] = "class_ids";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_x[] = "real_world_x";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_y[] = "real_world_y";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_z[] = "real_world_z";
static char weedbot_interfaces__msg__WeedDetection__FIELD_NAME__mask[] = "mask";

static rosidl_runtime_c__type_description__Field weedbot_interfaces__msg__WeedDetection__FIELDS[] = {
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__header, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_x, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_y, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_w, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__bbox_h, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__confidences, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__class_ids, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32_UNBOUNDED_SEQUENCE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_x, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_y, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__real_world_z, 12, 12},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {weedbot_interfaces__msg__WeedDetection__FIELD_NAME__mask, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription weedbot_interfaces__msg__WeedDetection__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
weedbot_interfaces__msg__WeedDetection__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {weedbot_interfaces__msg__WeedDetection__TYPE_NAME, 36, 36},
      {weedbot_interfaces__msg__WeedDetection__FIELDS, 11, 11},
    },
    {weedbot_interfaces__msg__WeedDetection__REFERENCED_TYPE_DESCRIPTIONS, 3, 3},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&sensor_msgs__msg__Image__EXPECTED_HASH, sensor_msgs__msg__Image__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = sensor_msgs__msg__Image__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "std_msgs/Header header\n"
  "\n"
  "# Pixel coordinates (normalized 0-1)\n"
  "float32[] bbox_x  # Bounding box x coordinates\n"
  "float32[] bbox_y  # Bounding box y coordinates\n"
  "float32[] bbox_w  # Bounding box widths\n"
  "float32[] bbox_h  # Bounding box heights\n"
  "float32[] confidences  # Detection confidences\n"
  "int32[] class_ids  # Class IDs (if multiple weed types)\n"
  "\n"
  "# NEW: Real-world coordinates (meters, relative to camera center on ground)\n"
  "float32 real_world_x  # X position in meters (+ = right, - = left)\n"
  "float32 real_world_y  # Y position in meters (+ = forward, - = backward)\n"
  "float32 real_world_z  # Z position in meters (0 = ground plane)\n"
  "\n"
  "# Optional segmentation mask\n"
  "sensor_msgs/Image mask";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
weedbot_interfaces__msg__WeedDetection__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {weedbot_interfaces__msg__WeedDetection__TYPE_NAME, 36, 36},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 672, 672},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
weedbot_interfaces__msg__WeedDetection__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[4];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 4, 4};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *weedbot_interfaces__msg__WeedDetection__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *sensor_msgs__msg__Image__get_individual_type_description_source(NULL);
    sources[3] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
