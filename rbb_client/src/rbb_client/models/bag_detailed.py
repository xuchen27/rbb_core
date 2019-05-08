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


class BagDetailed(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BagDetailed - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'detail_type': 'str',
            'name': 'str',
            'store_data': 'object',
            'discovered': 'datetime',
            'extraction_failure': 'bool',
            'in_trash': 'bool',
            'is_extracted': 'bool',
            'meta_available': 'bool',
            'size': 'int',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'duration': 'float',
            'messages': 'int',
            'tags': 'list[Tag]',
            'topics': 'list[Topic]',
            'products': 'list[Product]',
            'comment': 'str'
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'name': 'name',
            'store_data': 'store_data',
            'discovered': 'discovered',
            'extraction_failure': 'extraction_failure',
            'in_trash': 'in_trash',
            'is_extracted': 'is_extracted',
            'meta_available': 'meta_available',
            'size': 'size',
            'start_time': 'start_time',
            'end_time': 'end_time',
            'duration': 'duration',
            'messages': 'messages',
            'tags': 'tags',
            'topics': 'topics',
            'products': 'products',
            'comment': 'comment'
        }

        self._detail_type = None
        self._name = None
        self._store_data = None
        self._discovered = None
        self._extraction_failure = None
        self._in_trash = None
        self._is_extracted = None
        self._meta_available = None
        self._size = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._messages = None
        self._tags = None
        self._topics = None
        self._products = None
        self._comment = None

    @property
    def detail_type(self):
        """
        Gets the detail_type of this BagDetailed.


        :return: The detail_type of this BagDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type):
        """
        Sets the detail_type of this BagDetailed.


        :param detail_type: The detail_type of this BagDetailed.
        :type: str
        """
        self._detail_type = detail_type

    @property
    def name(self):
        """
        Gets the name of this BagDetailed.


        :return: The name of this BagDetailed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BagDetailed.


        :param name: The name of this BagDetailed.
        :type: str
        """
        self._name = name

    @property
    def store_data(self):
        """
        Gets the store_data of this BagDetailed.
        Data that is specific to the bag store type.

        :return: The store_data of this BagDetailed.
        :rtype: object
        """
        return self._store_data

    @store_data.setter
    def store_data(self, store_data):
        """
        Sets the store_data of this BagDetailed.
        Data that is specific to the bag store type.

        :param store_data: The store_data of this BagDetailed.
        :type: object
        """
        self._store_data = store_data

    @property
    def discovered(self):
        """
        Gets the discovered of this BagDetailed.
        Date and time this bag was discovered.

        :return: The discovered of this BagDetailed.
        :rtype: datetime
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """
        Sets the discovered of this BagDetailed.
        Date and time this bag was discovered.

        :param discovered: The discovered of this BagDetailed.
        :type: datetime
        """
        self._discovered = discovered

    @property
    def extraction_failure(self):
        """
        Gets the extraction_failure of this BagDetailed.
        True if the extraction failed

        :return: The extraction_failure of this BagDetailed.
        :rtype: bool
        """
        return self._extraction_failure

    @extraction_failure.setter
    def extraction_failure(self, extraction_failure):
        """
        Sets the extraction_failure of this BagDetailed.
        True if the extraction failed

        :param extraction_failure: The extraction_failure of this BagDetailed.
        :type: bool
        """
        self._extraction_failure = extraction_failure

    @property
    def in_trash(self):
        """
        Gets the in_trash of this BagDetailed.
        True if the bag is in the trash bin.

        :return: The in_trash of this BagDetailed.
        :rtype: bool
        """
        return self._in_trash

    @in_trash.setter
    def in_trash(self, in_trash):
        """
        Sets the in_trash of this BagDetailed.
        True if the bag is in the trash bin.

        :param in_trash: The in_trash of this BagDetailed.
        :type: bool
        """
        self._in_trash = in_trash

    @property
    def is_extracted(self):
        """
        Gets the is_extracted of this BagDetailed.
        True if data is extracted from this bag.

        :return: The is_extracted of this BagDetailed.
        :rtype: bool
        """
        return self._is_extracted

    @is_extracted.setter
    def is_extracted(self, is_extracted):
        """
        Sets the is_extracted of this BagDetailed.
        True if data is extracted from this bag.

        :param is_extracted: The is_extracted of this BagDetailed.
        :type: bool
        """
        self._is_extracted = is_extracted

    @property
    def meta_available(self):
        """
        Gets the meta_available of this BagDetailed.
        True if meta data is known for this bag.

        :return: The meta_available of this BagDetailed.
        :rtype: bool
        """
        return self._meta_available

    @meta_available.setter
    def meta_available(self, meta_available):
        """
        Sets the meta_available of this BagDetailed.
        True if meta data is known for this bag.

        :param meta_available: The meta_available of this BagDetailed.
        :type: bool
        """
        self._meta_available = meta_available

    @property
    def size(self):
        """
        Gets the size of this BagDetailed.
        Size of the bag in bytes.

        :return: The size of this BagDetailed.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this BagDetailed.
        Size of the bag in bytes.

        :param size: The size of this BagDetailed.
        :type: int
        """
        self._size = size

    @property
    def start_time(self):
        """
        Gets the start_time of this BagDetailed.
        Start time of this bag.

        :return: The start_time of this BagDetailed.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BagDetailed.
        Start time of this bag.

        :param start_time: The start_time of this BagDetailed.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BagDetailed.
        Start time of this bag.

        :return: The end_time of this BagDetailed.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BagDetailed.
        Start time of this bag.

        :param end_time: The end_time of this BagDetailed.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def duration(self):
        """
        Gets the duration of this BagDetailed.
        duration of this bag in seconds.

        :return: The duration of this BagDetailed.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this BagDetailed.
        duration of this bag in seconds.

        :param duration: The duration of this BagDetailed.
        :type: float
        """
        self._duration = duration

    @property
    def messages(self):
        """
        Gets the messages of this BagDetailed.
        Number of messages in this bag.

        :return: The messages of this BagDetailed.
        :rtype: int
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this BagDetailed.
        Number of messages in this bag.

        :param messages: The messages of this BagDetailed.
        :type: int
        """
        self._messages = messages

    @property
    def tags(self):
        """
        Gets the tags of this BagDetailed.


        :return: The tags of this BagDetailed.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BagDetailed.


        :param tags: The tags of this BagDetailed.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def topics(self):
        """
        Gets the topics of this BagDetailed.


        :return: The topics of this BagDetailed.
        :rtype: list[Topic]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """
        Sets the topics of this BagDetailed.


        :param topics: The topics of this BagDetailed.
        :type: list[Topic]
        """
        self._topics = topics

    @property
    def products(self):
        """
        Gets the products of this BagDetailed.


        :return: The products of this BagDetailed.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """
        Sets the products of this BagDetailed.


        :param products: The products of this BagDetailed.
        :type: list[Product]
        """
        self._products = products

    @property
    def comment(self):
        """
        Gets the comment of this BagDetailed.
        Manual comment on the bag.

        :return: The comment of this BagDetailed.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this BagDetailed.
        Manual comment on the bag.

        :param comment: The comment of this BagDetailed.
        :type: str
        """
        self._comment = comment

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

