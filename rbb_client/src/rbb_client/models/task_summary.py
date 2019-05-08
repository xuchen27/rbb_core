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


class TaskSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TaskSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'detail_type': 'str',
            'identifier': 'str',
            'priority': 'float',
            'description': 'str',
            'assigned_to': 'str',
            'created': 'datetime',
            'last_updated': 'datetime',
            'state': 'int',
            'task': 'str',
            'success': 'bool',
            'runtime': 'float',
            'worker_labels': 'str'
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'identifier': 'identifier',
            'priority': 'priority',
            'description': 'description',
            'assigned_to': 'assigned_to',
            'created': 'created',
            'last_updated': 'last_updated',
            'state': 'state',
            'task': 'task',
            'success': 'success',
            'runtime': 'runtime',
            'worker_labels': 'worker_labels'
        }

        self._detail_type = None
        self._identifier = None
        self._priority = None
        self._description = None
        self._assigned_to = None
        self._created = None
        self._last_updated = None
        self._state = None
        self._task = None
        self._success = None
        self._runtime = None
        self._worker_labels = None

    @property
    def detail_type(self):
        """
        Gets the detail_type of this TaskSummary.


        :return: The detail_type of this TaskSummary.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type):
        """
        Sets the detail_type of this TaskSummary.


        :param detail_type: The detail_type of this TaskSummary.
        :type: str
        """
        self._detail_type = detail_type

    @property
    def identifier(self):
        """
        Gets the identifier of this TaskSummary.


        :return: The identifier of this TaskSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this TaskSummary.


        :param identifier: The identifier of this TaskSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def priority(self):
        """
        Gets the priority of this TaskSummary.


        :return: The priority of this TaskSummary.
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this TaskSummary.


        :param priority: The priority of this TaskSummary.
        :type: float
        """
        self._priority = priority

    @property
    def description(self):
        """
        Gets the description of this TaskSummary.
        Simple description to identify the type of task

        :return: The description of this TaskSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskSummary.
        Simple description to identify the type of task

        :param description: The description of this TaskSummary.
        :type: str
        """
        self._description = description

    @property
    def assigned_to(self):
        """
        Gets the assigned_to of this TaskSummary.
        Name of worker assigned to the task.

        :return: The assigned_to of this TaskSummary.
        :rtype: str
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """
        Sets the assigned_to of this TaskSummary.
        Name of worker assigned to the task.

        :param assigned_to: The assigned_to of this TaskSummary.
        :type: str
        """
        self._assigned_to = assigned_to

    @property
    def created(self):
        """
        Gets the created of this TaskSummary.
        Date the task was added to the queue.

        :return: The created of this TaskSummary.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this TaskSummary.
        Date the task was added to the queue.

        :param created: The created of this TaskSummary.
        :type: datetime
        """
        self._created = created

    @property
    def last_updated(self):
        """
        Gets the last_updated of this TaskSummary.
        Date the task was updated to the queue.

        :return: The last_updated of this TaskSummary.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this TaskSummary.
        Date the task was updated to the queue.

        :param last_updated: The last_updated of this TaskSummary.
        :type: datetime
        """
        self._last_updated = last_updated

    @property
    def state(self):
        """
        Gets the state of this TaskSummary.
        State of the task.

        :return: The state of this TaskSummary.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this TaskSummary.
        State of the task.

        :param state: The state of this TaskSummary.
        :type: int
        """
        self._state = state

    @property
    def task(self):
        """
        Gets the task of this TaskSummary.
        The task.

        :return: The task of this TaskSummary.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """
        Sets the task of this TaskSummary.
        The task.

        :param task: The task of this TaskSummary.
        :type: str
        """
        self._task = task

    @property
    def success(self):
        """
        Gets the success of this TaskSummary.


        :return: The success of this TaskSummary.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this TaskSummary.


        :param success: The success of this TaskSummary.
        :type: bool
        """
        self._success = success

    @property
    def runtime(self):
        """
        Gets the runtime of this TaskSummary.


        :return: The runtime of this TaskSummary.
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this TaskSummary.


        :param runtime: The runtime of this TaskSummary.
        :type: float
        """
        self._runtime = runtime

    @property
    def worker_labels(self):
        """
        Gets the worker_labels of this TaskSummary.
        Worker that can take this task.

        :return: The worker_labels of this TaskSummary.
        :rtype: str
        """
        return self._worker_labels

    @worker_labels.setter
    def worker_labels(self, worker_labels):
        """
        Sets the worker_labels of this TaskSummary.
        Worker that can take this task.

        :param worker_labels: The worker_labels of this TaskSummary.
        :type: str
        """
        self._worker_labels = worker_labels

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
