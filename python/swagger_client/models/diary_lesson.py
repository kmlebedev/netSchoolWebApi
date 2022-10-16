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

class DiaryLesson(object):
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
        'classmeeting_id': 'str',
        'day': 'date',
        'number': 'int',
        'room': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'subject_name': 'str',
        'assignments': 'list[DiaryAssignment]'
    }

    attribute_map = {
        'classmeeting_id': 'classmeetingId',
        'day': 'day',
        'number': 'number',
        'room': 'room',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'subject_name': 'subjectName',
        'assignments': 'assignments'
    }

    def __init__(self, classmeeting_id=None, day=None, number=None, room=None, start_time=None, end_time=None, subject_name=None, assignments=None):  # noqa: E501
        """DiaryLesson - a model defined in Swagger"""  # noqa: E501
        self._classmeeting_id = None
        self._day = None
        self._number = None
        self._room = None
        self._start_time = None
        self._end_time = None
        self._subject_name = None
        self._assignments = None
        self.discriminator = None
        if classmeeting_id is not None:
            self.classmeeting_id = classmeeting_id
        if day is not None:
            self.day = day
        if number is not None:
            self.number = number
        if room is not None:
            self.room = room
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if subject_name is not None:
            self.subject_name = subject_name
        if assignments is not None:
            self.assignments = assignments

    @property
    def classmeeting_id(self):
        """Gets the classmeeting_id of this DiaryLesson.  # noqa: E501


        :return: The classmeeting_id of this DiaryLesson.  # noqa: E501
        :rtype: str
        """
        return self._classmeeting_id

    @classmeeting_id.setter
    def classmeeting_id(self, classmeeting_id):
        """Sets the classmeeting_id of this DiaryLesson.


        :param classmeeting_id: The classmeeting_id of this DiaryLesson.  # noqa: E501
        :type: str
        """

        self._classmeeting_id = classmeeting_id

    @property
    def day(self):
        """Gets the day of this DiaryLesson.  # noqa: E501


        :return: The day of this DiaryLesson.  # noqa: E501
        :rtype: date
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this DiaryLesson.


        :param day: The day of this DiaryLesson.  # noqa: E501
        :type: date
        """

        self._day = day

    @property
    def number(self):
        """Gets the number of this DiaryLesson.  # noqa: E501


        :return: The number of this DiaryLesson.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this DiaryLesson.


        :param number: The number of this DiaryLesson.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def room(self):
        """Gets the room of this DiaryLesson.  # noqa: E501


        :return: The room of this DiaryLesson.  # noqa: E501
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room):
        """Sets the room of this DiaryLesson.


        :param room: The room of this DiaryLesson.  # noqa: E501
        :type: str
        """

        self._room = room

    @property
    def start_time(self):
        """Gets the start_time of this DiaryLesson.  # noqa: E501


        :return: The start_time of this DiaryLesson.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DiaryLesson.


        :param start_time: The start_time of this DiaryLesson.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DiaryLesson.  # noqa: E501


        :return: The end_time of this DiaryLesson.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DiaryLesson.


        :param end_time: The end_time of this DiaryLesson.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def subject_name(self):
        """Gets the subject_name of this DiaryLesson.  # noqa: E501


        :return: The subject_name of this DiaryLesson.  # noqa: E501
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this DiaryLesson.


        :param subject_name: The subject_name of this DiaryLesson.  # noqa: E501
        :type: str
        """

        self._subject_name = subject_name

    @property
    def assignments(self):
        """Gets the assignments of this DiaryLesson.  # noqa: E501


        :return: The assignments of this DiaryLesson.  # noqa: E501
        :rtype: list[DiaryAssignment]
        """
        return self._assignments

    @assignments.setter
    def assignments(self, assignments):
        """Sets the assignments of this DiaryLesson.


        :param assignments: The assignments of this DiaryLesson.  # noqa: E501
        :type: list[DiaryAssignment]
        """

        self._assignments = assignments

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
        if issubclass(DiaryLesson, dict):
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
        if not isinstance(other, DiaryLesson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
