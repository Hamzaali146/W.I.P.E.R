# generated from rosidl_generator_py/resource/_idl.py.em
# with input from weedbot_interfaces:msg/WeedDetection.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

# Member 'bbox_x'
# Member 'bbox_y'
# Member 'bbox_w'
# Member 'bbox_h'
# Member 'confidences'
# Member 'class_ids'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_WeedDetection(type):
    """Metaclass of message 'WeedDetection'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('weedbot_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'weedbot_interfaces.msg.WeedDetection')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__weed_detection
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__weed_detection
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__weed_detection
            cls._TYPE_SUPPORT = module.type_support_msg__msg__weed_detection
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__weed_detection

            from sensor_msgs.msg import Image
            if Image.__class__._TYPE_SUPPORT is None:
                Image.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class WeedDetection(metaclass=Metaclass_WeedDetection):
    """Message class 'WeedDetection'."""

    __slots__ = [
        '_header',
        '_bbox_x',
        '_bbox_y',
        '_bbox_w',
        '_bbox_h',
        '_confidences',
        '_class_ids',
        '_real_world_x',
        '_real_world_y',
        '_real_world_z',
        '_mask',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'bbox_x': 'sequence<float>',
        'bbox_y': 'sequence<float>',
        'bbox_w': 'sequence<float>',
        'bbox_h': 'sequence<float>',
        'confidences': 'sequence<float>',
        'class_ids': 'sequence<int32>',
        'real_world_x': 'float',
        'real_world_y': 'float',
        'real_world_z': 'float',
        'mask': 'sensor_msgs/Image',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'Image'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.bbox_x = array.array('f', kwargs.get('bbox_x', []))
        self.bbox_y = array.array('f', kwargs.get('bbox_y', []))
        self.bbox_w = array.array('f', kwargs.get('bbox_w', []))
        self.bbox_h = array.array('f', kwargs.get('bbox_h', []))
        self.confidences = array.array('f', kwargs.get('confidences', []))
        self.class_ids = array.array('i', kwargs.get('class_ids', []))
        self.real_world_x = kwargs.get('real_world_x', float())
        self.real_world_y = kwargs.get('real_world_y', float())
        self.real_world_z = kwargs.get('real_world_z', float())
        from sensor_msgs.msg import Image
        self.mask = kwargs.get('mask', Image())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.bbox_x != other.bbox_x:
            return False
        if self.bbox_y != other.bbox_y:
            return False
        if self.bbox_w != other.bbox_w:
            return False
        if self.bbox_h != other.bbox_h:
            return False
        if self.confidences != other.confidences:
            return False
        if self.class_ids != other.class_ids:
            return False
        if self.real_world_x != other.real_world_x:
            return False
        if self.real_world_y != other.real_world_y:
            return False
        if self.real_world_z != other.real_world_z:
            return False
        if self.mask != other.mask:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if self._check_fields:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def bbox_x(self):
        """Message field 'bbox_x'."""
        return self._bbox_x

    @bbox_x.setter
    def bbox_x(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'bbox_x' array.array() must have the type code of 'f'"
                self._bbox_x = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bbox_x' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bbox_x = array.array('f', value)

    @builtins.property
    def bbox_y(self):
        """Message field 'bbox_y'."""
        return self._bbox_y

    @bbox_y.setter
    def bbox_y(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'bbox_y' array.array() must have the type code of 'f'"
                self._bbox_y = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bbox_y' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bbox_y = array.array('f', value)

    @builtins.property
    def bbox_w(self):
        """Message field 'bbox_w'."""
        return self._bbox_w

    @bbox_w.setter
    def bbox_w(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'bbox_w' array.array() must have the type code of 'f'"
                self._bbox_w = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bbox_w' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bbox_w = array.array('f', value)

    @builtins.property
    def bbox_h(self):
        """Message field 'bbox_h'."""
        return self._bbox_h

    @bbox_h.setter
    def bbox_h(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'bbox_h' array.array() must have the type code of 'f'"
                self._bbox_h = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bbox_h' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bbox_h = array.array('f', value)

    @builtins.property
    def confidences(self):
        """Message field 'confidences'."""
        return self._confidences

    @confidences.setter
    def confidences(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'f', \
                    "The 'confidences' array.array() must have the type code of 'f'"
                self._confidences = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'confidences' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._confidences = array.array('f', value)

    @builtins.property
    def class_ids(self):
        """Message field 'class_ids'."""
        return self._class_ids

    @class_ids.setter
    def class_ids(self, value):
        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'i', \
                    "The 'class_ids' array.array() must have the type code of 'i'"
                self._class_ids = value
                return
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'class_ids' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._class_ids = array.array('i', value)

    @builtins.property
    def real_world_x(self):
        """Message field 'real_world_x'."""
        return self._real_world_x

    @real_world_x.setter
    def real_world_x(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'real_world_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'real_world_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._real_world_x = value

    @builtins.property
    def real_world_y(self):
        """Message field 'real_world_y'."""
        return self._real_world_y

    @real_world_y.setter
    def real_world_y(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'real_world_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'real_world_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._real_world_y = value

    @builtins.property
    def real_world_z(self):
        """Message field 'real_world_z'."""
        return self._real_world_z

    @real_world_z.setter
    def real_world_z(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'real_world_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'real_world_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._real_world_z = value

    @builtins.property
    def mask(self):
        """Message field 'mask'."""
        return self._mask

    @mask.setter
    def mask(self, value):
        if self._check_fields:
            from sensor_msgs.msg import Image
            assert \
                isinstance(value, Image), \
                "The 'mask' field must be a sub message of type 'Image'"
        self._mask = value
