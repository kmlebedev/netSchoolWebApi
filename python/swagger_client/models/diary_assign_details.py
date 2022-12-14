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

class DiaryAssignDetails(object):
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
        'id': 'int',
        'assignment_name': 'str',
        'activity_name': 'str',
        'problem_name': 'str',
        'subject_group': 'DiaryAssignDetailsSubjectGroup',
        'teachers': 'list[DiaryAssignDetailsTeachers]',
        'product_id': 'int',
        'is_deleted': 'bool',
        'weight': 'int',
        '_date': 'date',
        'description': 'str',
        'attachments': 'list[DiaryAssignDetailsAttachments]',
        'content_elements': 'list[object]',
        'code_content_elements': 'list[object]'
    }

    attribute_map = {
        'id': 'id',
        'assignment_name': 'assignmentName',
        'activity_name': 'activityName',
        'problem_name': 'problemName',
        'subject_group': 'subjectGroup',
        'teachers': 'teachers',
        'product_id': 'productId',
        'is_deleted': 'isDeleted',
        'weight': 'weight',
        '_date': 'date',
        'description': 'description',
        'attachments': 'attachments',
        'content_elements': 'contentElements',
        'code_content_elements': 'codeContentElements'
    }

    def __init__(self, id=None, assignment_name=None, activity_name=None, problem_name=None, subject_group=None, teachers=None, product_id=None, is_deleted=None, weight=None, _date=None, description=None, attachments=None, content_elements=None, code_content_elements=None):  # noqa: E501
        """DiaryAssignDetails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._assignment_name = None
        self._activity_name = None
        self._problem_name = None
        self._subject_group = None
        self._teachers = None
        self._product_id = None
        self._is_deleted = None
        self._weight = None
        self.__date = None
        self._description = None
        self._attachments = None
        self._content_elements = None
        self._code_content_elements = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if assignment_name is not None:
            self.assignment_name = assignment_name
        if activity_name is not None:
            self.activity_name = activity_name
        if problem_name is not None:
            self.problem_name = problem_name
        if subject_group is not None:
            self.subject_group = subject_group
        if teachers is not None:
            self.teachers = teachers
        if product_id is not None:
            self.product_id = product_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if weight is not None:
            self.weight = weight
        if _date is not None:
            self._date = _date
        if description is not None:
            self.description = description
        if attachments is not None:
            self.attachments = attachments
        if content_elements is not None:
            self.content_elements = content_elements
        if code_content_elements is not None:
            self.code_content_elements = code_content_elements

    @property
    def id(self):
        """Gets the id of this DiaryAssignDetails.  # noqa: E501


        :return: The id of this DiaryAssignDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiaryAssignDetails.


        :param id: The id of this DiaryAssignDetails.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def assignment_name(self):
        """Gets the assignment_name of this DiaryAssignDetails.  # noqa: E501


        :return: The assignment_name of this DiaryAssignDetails.  # noqa: E501
        :rtype: str
        """
        return self._assignment_name

    @assignment_name.setter
    def assignment_name(self, assignment_name):
        """Sets the assignment_name of this DiaryAssignDetails.


        :param assignment_name: The assignment_name of this DiaryAssignDetails.  # noqa: E501
        :type: str
        """

        self._assignment_name = assignment_name

    @property
    def activity_name(self):
        """Gets the activity_name of this DiaryAssignDetails.  # noqa: E501


        :return: The activity_name of this DiaryAssignDetails.  # noqa: E501
        :rtype: str
        """
        return self._activity_name

    @activity_name.setter
    def activity_name(self, activity_name):
        """Sets the activity_name of this DiaryAssignDetails.


        :param activity_name: The activity_name of this DiaryAssignDetails.  # noqa: E501
        :type: str
        """

        self._activity_name = activity_name

    @property
    def problem_name(self):
        """Gets the problem_name of this DiaryAssignDetails.  # noqa: E501


        :return: The problem_name of this DiaryAssignDetails.  # noqa: E501
        :rtype: str
        """
        return self._problem_name

    @problem_name.setter
    def problem_name(self, problem_name):
        """Sets the problem_name of this DiaryAssignDetails.


        :param problem_name: The problem_name of this DiaryAssignDetails.  # noqa: E501
        :type: str
        """

        self._problem_name = problem_name

    @property
    def subject_group(self):
        """Gets the subject_group of this DiaryAssignDetails.  # noqa: E501


        :return: The subject_group of this DiaryAssignDetails.  # noqa: E501
        :rtype: DiaryAssignDetailsSubjectGroup
        """
        return self._subject_group

    @subject_group.setter
    def subject_group(self, subject_group):
        """Sets the subject_group of this DiaryAssignDetails.


        :param subject_group: The subject_group of this DiaryAssignDetails.  # noqa: E501
        :type: DiaryAssignDetailsSubjectGroup
        """

        self._subject_group = subject_group

    @property
    def teachers(self):
        """Gets the teachers of this DiaryAssignDetails.  # noqa: E501


        :return: The teachers of this DiaryAssignDetails.  # noqa: E501
        :rtype: list[DiaryAssignDetailsTeachers]
        """
        return self._teachers

    @teachers.setter
    def teachers(self, teachers):
        """Sets the teachers of this DiaryAssignDetails.


        :param teachers: The teachers of this DiaryAssignDetails.  # noqa: E501
        :type: list[DiaryAssignDetailsTeachers]
        """

        self._teachers = teachers

    @property
    def product_id(self):
        """Gets the product_id of this DiaryAssignDetails.  # noqa: E501


        :return: The product_id of this DiaryAssignDetails.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DiaryAssignDetails.


        :param product_id: The product_id of this DiaryAssignDetails.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this DiaryAssignDetails.  # noqa: E501


        :return: The is_deleted of this DiaryAssignDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this DiaryAssignDetails.


        :param is_deleted: The is_deleted of this DiaryAssignDetails.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def weight(self):
        """Gets the weight of this DiaryAssignDetails.  # noqa: E501


        :return: The weight of this DiaryAssignDetails.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DiaryAssignDetails.


        :param weight: The weight of this DiaryAssignDetails.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def _date(self):
        """Gets the _date of this DiaryAssignDetails.  # noqa: E501


        :return: The _date of this DiaryAssignDetails.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DiaryAssignDetails.


        :param _date: The _date of this DiaryAssignDetails.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def description(self):
        """Gets the description of this DiaryAssignDetails.  # noqa: E501


        :return: The description of this DiaryAssignDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiaryAssignDetails.


        :param description: The description of this DiaryAssignDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def attachments(self):
        """Gets the attachments of this DiaryAssignDetails.  # noqa: E501


        :return: The attachments of this DiaryAssignDetails.  # noqa: E501
        :rtype: list[DiaryAssignDetailsAttachments]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this DiaryAssignDetails.


        :param attachments: The attachments of this DiaryAssignDetails.  # noqa: E501
        :type: list[DiaryAssignDetailsAttachments]
        """

        self._attachments = attachments

    @property
    def content_elements(self):
        """Gets the content_elements of this DiaryAssignDetails.  # noqa: E501


        :return: The content_elements of this DiaryAssignDetails.  # noqa: E501
        :rtype: list[object]
        """
        return self._content_elements

    @content_elements.setter
    def content_elements(self, content_elements):
        """Sets the content_elements of this DiaryAssignDetails.


        :param content_elements: The content_elements of this DiaryAssignDetails.  # noqa: E501
        :type: list[object]
        """

        self._content_elements = content_elements

    @property
    def code_content_elements(self):
        """Gets the code_content_elements of this DiaryAssignDetails.  # noqa: E501


        :return: The code_content_elements of this DiaryAssignDetails.  # noqa: E501
        :rtype: list[object]
        """
        return self._code_content_elements

    @code_content_elements.setter
    def code_content_elements(self, code_content_elements):
        """Sets the code_content_elements of this DiaryAssignDetails.


        :param code_content_elements: The code_content_elements of this DiaryAssignDetails.  # noqa: E501
        :type: list[object]
        """

        self._code_content_elements = code_content_elements

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
        if issubclass(DiaryAssignDetails, dict):
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
        if not isinstance(other, DiaryAssignDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
