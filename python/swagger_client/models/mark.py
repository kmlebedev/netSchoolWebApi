# coding: utf-8

"""
    NetSchool

    The API for the NetSchool irTech project  # noqa: E501

    OpenAPI spec version: 5.10.63221
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Mark(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'assignment_id': 'int',
        'student_id': 'int',
        'mark': 'int',
        'duty_mark': 'bool'
    }

    attribute_map = {
        'assignment_id': 'assignmentId',
        'student_id': 'studentId',
        'mark': 'mark',
        'duty_mark': 'dutyMark'
    }

    def __init__(self, assignment_id=None, student_id=None, mark=None, duty_mark=None):  # noqa: E501
        """Mark - a model defined in Swagger"""  # noqa: E501
        self._assignment_id = None
        self._student_id = None
        self._mark = None
        self._duty_mark = None
        self.discriminator = None
        if assignment_id is not None:
            self.assignment_id = assignment_id
        if student_id is not None:
            self.student_id = student_id
        if mark is not None:
            self.mark = mark
        if duty_mark is not None:
            self.duty_mark = duty_mark

    @property
    def assignment_id(self):
        """Gets the assignment_id of this Mark.  # noqa: E501


        :return: The assignment_id of this Mark.  # noqa: E501
        :rtype: int
        """
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        """Sets the assignment_id of this Mark.


        :param assignment_id: The assignment_id of this Mark.  # noqa: E501
        :type: int
        """

        self._assignment_id = assignment_id

    @property
    def student_id(self):
        """Gets the student_id of this Mark.  # noqa: E501


        :return: The student_id of this Mark.  # noqa: E501
        :rtype: int
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        """Sets the student_id of this Mark.


        :param student_id: The student_id of this Mark.  # noqa: E501
        :type: int
        """

        self._student_id = student_id

    @property
    def mark(self):
        """Gets the mark of this Mark.  # noqa: E501


        :return: The mark of this Mark.  # noqa: E501
        :rtype: int
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        """Sets the mark of this Mark.


        :param mark: The mark of this Mark.  # noqa: E501
        :type: int
        """

        self._mark = mark

    @property
    def duty_mark(self):
        """Gets the duty_mark of this Mark.  # noqa: E501


        :return: The duty_mark of this Mark.  # noqa: E501
        :rtype: bool
        """
        return self._duty_mark

    @duty_mark.setter
    def duty_mark(self, duty_mark):
        """Sets the duty_mark of this Mark.


        :param duty_mark: The duty_mark of this Mark.  # noqa: E501
        :type: bool
        """

        self._duty_mark = duty_mark

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Mark, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Mark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
