# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.task_summary import TaskSummary  # noqa: F401,E501
from rbb_swagger_server import util


class TaskDetailed(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, detail_type: str=None, identifier: str=None, priority: float=None, description: str=None, assigned_to: str=None, created: datetime=None, last_updated: datetime=None, state: int=None, task: str=None, success: bool=None, runtime: float=None, worker_labels: str=None, config: object=None, result: object=None, log: str=None):  # noqa: E501
        """TaskDetailed - a model defined in Swagger

        :param detail_type: The detail_type of this TaskDetailed.  # noqa: E501
        :type detail_type: str
        :param identifier: The identifier of this TaskDetailed.  # noqa: E501
        :type identifier: str
        :param priority: The priority of this TaskDetailed.  # noqa: E501
        :type priority: float
        :param description: The description of this TaskDetailed.  # noqa: E501
        :type description: str
        :param assigned_to: The assigned_to of this TaskDetailed.  # noqa: E501
        :type assigned_to: str
        :param created: The created of this TaskDetailed.  # noqa: E501
        :type created: datetime
        :param last_updated: The last_updated of this TaskDetailed.  # noqa: E501
        :type last_updated: datetime
        :param state: The state of this TaskDetailed.  # noqa: E501
        :type state: int
        :param task: The task of this TaskDetailed.  # noqa: E501
        :type task: str
        :param success: The success of this TaskDetailed.  # noqa: E501
        :type success: bool
        :param runtime: The runtime of this TaskDetailed.  # noqa: E501
        :type runtime: float
        :param worker_labels: The worker_labels of this TaskDetailed.  # noqa: E501
        :type worker_labels: str
        :param config: The config of this TaskDetailed.  # noqa: E501
        :type config: object
        :param result: The result of this TaskDetailed.  # noqa: E501
        :type result: object
        :param log: The log of this TaskDetailed.  # noqa: E501
        :type log: str
        """
        self.swagger_types = {
            'detail_type': str,
            'identifier': str,
            'priority': float,
            'description': str,
            'assigned_to': str,
            'created': datetime,
            'last_updated': datetime,
            'state': int,
            'task': str,
            'success': bool,
            'runtime': float,
            'worker_labels': str,
            'config': object,
            'result': object,
            'log': str
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
            'worker_labels': 'worker_labels',
            'config': 'config',
            'result': 'result',
            'log': 'log'
        }

        self._detail_type = detail_type
        self._identifier = identifier
        self._priority = priority
        self._description = description
        self._assigned_to = assigned_to
        self._created = created
        self._last_updated = last_updated
        self._state = state
        self._task = task
        self._success = success
        self._runtime = runtime
        self._worker_labels = worker_labels
        self._config = config
        self._result = result
        self._log = log

    @classmethod
    def from_dict(cls, dikt) -> 'TaskDetailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TaskDetailed of this TaskDetailed.  # noqa: E501
        :rtype: TaskDetailed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail_type(self) -> str:
        """Gets the detail_type of this TaskDetailed.


        :return: The detail_type of this TaskDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type: str):
        """Sets the detail_type of this TaskDetailed.


        :param detail_type: The detail_type of this TaskDetailed.
        :type detail_type: str
        """
        if detail_type is None:
            raise ValueError("Invalid value for `detail_type`, must not be `None`")  # noqa: E501

        self._detail_type = detail_type

    @property
    def identifier(self) -> str:
        """Gets the identifier of this TaskDetailed.


        :return: The identifier of this TaskDetailed.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: str):
        """Sets the identifier of this TaskDetailed.


        :param identifier: The identifier of this TaskDetailed.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def priority(self) -> float:
        """Gets the priority of this TaskDetailed.


        :return: The priority of this TaskDetailed.
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority: float):
        """Sets the priority of this TaskDetailed.


        :param priority: The priority of this TaskDetailed.
        :type priority: float
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def description(self) -> str:
        """Gets the description of this TaskDetailed.

        Simple description to identify the type of task  # noqa: E501

        :return: The description of this TaskDetailed.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this TaskDetailed.

        Simple description to identify the type of task  # noqa: E501

        :param description: The description of this TaskDetailed.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def assigned_to(self) -> str:
        """Gets the assigned_to of this TaskDetailed.

        Name of worker assigned to the task.  # noqa: E501

        :return: The assigned_to of this TaskDetailed.
        :rtype: str
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to: str):
        """Sets the assigned_to of this TaskDetailed.

        Name of worker assigned to the task.  # noqa: E501

        :param assigned_to: The assigned_to of this TaskDetailed.
        :type assigned_to: str
        """
        if assigned_to is None:
            raise ValueError("Invalid value for `assigned_to`, must not be `None`")  # noqa: E501

        self._assigned_to = assigned_to

    @property
    def created(self) -> datetime:
        """Gets the created of this TaskDetailed.

        Date the task was added to the queue.  # noqa: E501

        :return: The created of this TaskDetailed.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this TaskDetailed.

        Date the task was added to the queue.  # noqa: E501

        :param created: The created of this TaskDetailed.
        :type created: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def last_updated(self) -> datetime:
        """Gets the last_updated of this TaskDetailed.

        Date the task was updated to the queue.  # noqa: E501

        :return: The last_updated of this TaskDetailed.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: datetime):
        """Sets the last_updated of this TaskDetailed.

        Date the task was updated to the queue.  # noqa: E501

        :param last_updated: The last_updated of this TaskDetailed.
        :type last_updated: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def state(self) -> int:
        """Gets the state of this TaskDetailed.

        State of the task.  # noqa: E501

        :return: The state of this TaskDetailed.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state: int):
        """Sets the state of this TaskDetailed.

        State of the task.  # noqa: E501

        :param state: The state of this TaskDetailed.
        :type state: int
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def task(self) -> str:
        """Gets the task of this TaskDetailed.

        The task.  # noqa: E501

        :return: The task of this TaskDetailed.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task: str):
        """Sets the task of this TaskDetailed.

        The task.  # noqa: E501

        :param task: The task of this TaskDetailed.
        :type task: str
        """
        if task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

    @property
    def success(self) -> bool:
        """Gets the success of this TaskDetailed.


        :return: The success of this TaskDetailed.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this TaskDetailed.


        :param success: The success of this TaskDetailed.
        :type success: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def runtime(self) -> float:
        """Gets the runtime of this TaskDetailed.


        :return: The runtime of this TaskDetailed.
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime: float):
        """Sets the runtime of this TaskDetailed.


        :param runtime: The runtime of this TaskDetailed.
        :type runtime: float
        """
        if runtime is None:
            raise ValueError("Invalid value for `runtime`, must not be `None`")  # noqa: E501

        self._runtime = runtime

    @property
    def worker_labels(self) -> str:
        """Gets the worker_labels of this TaskDetailed.

        Worker that can take this task.  # noqa: E501

        :return: The worker_labels of this TaskDetailed.
        :rtype: str
        """
        return self._worker_labels

    @worker_labels.setter
    def worker_labels(self, worker_labels: str):
        """Sets the worker_labels of this TaskDetailed.

        Worker that can take this task.  # noqa: E501

        :param worker_labels: The worker_labels of this TaskDetailed.
        :type worker_labels: str
        """
        if worker_labels is None:
            raise ValueError("Invalid value for `worker_labels`, must not be `None`")  # noqa: E501

        self._worker_labels = worker_labels

    @property
    def config(self) -> object:
        """Gets the config of this TaskDetailed.

        Configuration of the task.  # noqa: E501

        :return: The config of this TaskDetailed.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config: object):
        """Sets the config of this TaskDetailed.

        Configuration of the task.  # noqa: E501

        :param config: The config of this TaskDetailed.
        :type config: object
        """

        self._config = config

    @property
    def result(self) -> object:
        """Gets the result of this TaskDetailed.

        Result of the task  # noqa: E501

        :return: The result of this TaskDetailed.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result: object):
        """Sets the result of this TaskDetailed.

        Result of the task  # noqa: E501

        :param result: The result of this TaskDetailed.
        :type result: object
        """

        self._result = result

    @property
    def log(self) -> str:
        """Gets the log of this TaskDetailed.

        Standard output of the task  # noqa: E501

        :return: The log of this TaskDetailed.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log: str):
        """Sets the log of this TaskDetailed.

        Standard output of the task  # noqa: E501

        :param log: The log of this TaskDetailed.
        :type log: str
        """

        self._log = log
