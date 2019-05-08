# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Comment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Comment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'int',
            'comment_text': 'str',
            'created': 'datetime',
            'posted_by': 'User'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'comment_text': 'comment_text',
            'created': 'created',
            'posted_by': 'posted_by'
        }

        self._identifier = None
        self._comment_text = None
        self._created = None
        self._posted_by = None

    @property
    def identifier(self):
        """
        Gets the identifier of this Comment.


        :return: The identifier of this Comment.
        :rtype: int
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Comment.


        :param identifier: The identifier of this Comment.
        :type: int
        """
        self._identifier = identifier

    @property
    def comment_text(self):
        """
        Gets the comment_text of this Comment.


        :return: The comment_text of this Comment.
        :rtype: str
        """
        return self._comment_text

    @comment_text.setter
    def comment_text(self, comment_text):
        """
        Sets the comment_text of this Comment.


        :param comment_text: The comment_text of this Comment.
        :type: str
        """
        self._comment_text = comment_text

    @property
    def created(self):
        """
        Gets the created of this Comment.


        :return: The created of this Comment.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Comment.


        :param created: The created of this Comment.
        :type: datetime
        """
        self._created = created

    @property
    def posted_by(self):
        """
        Gets the posted_by of this Comment.


        :return: The posted_by of this Comment.
        :rtype: User
        """
        return self._posted_by

    @posted_by.setter
    def posted_by(self, posted_by):
        """
        Sets the posted_by of this Comment.


        :param posted_by: The posted_by of this Comment.
        :type: User
        """
        self._posted_by = posted_by

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

