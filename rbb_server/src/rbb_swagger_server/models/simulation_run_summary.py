# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server import util


class SimulationRunSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, detail_type: str=None, identifier: int=None, success: bool=None, description: str=None, duration: float=None, bag_name: str=None, bag_store_name: str=None):  # noqa: E501
        """SimulationRunSummary - a model defined in Swagger

        :param detail_type: The detail_type of this SimulationRunSummary.  # noqa: E501
        :type detail_type: str
        :param identifier: The identifier of this SimulationRunSummary.  # noqa: E501
        :type identifier: int
        :param success: The success of this SimulationRunSummary.  # noqa: E501
        :type success: bool
        :param description: The description of this SimulationRunSummary.  # noqa: E501
        :type description: str
        :param duration: The duration of this SimulationRunSummary.  # noqa: E501
        :type duration: float
        :param bag_name: The bag_name of this SimulationRunSummary.  # noqa: E501
        :type bag_name: str
        :param bag_store_name: The bag_store_name of this SimulationRunSummary.  # noqa: E501
        :type bag_store_name: str
        """
        self.swagger_types = {
            'detail_type': str,
            'identifier': int,
            'success': bool,
            'description': str,
            'duration': float,
            'bag_name': str,
            'bag_store_name': str
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'identifier': 'identifier',
            'success': 'success',
            'description': 'description',
            'duration': 'duration',
            'bag_name': 'bag_name',
            'bag_store_name': 'bag_store_name'
        }

        self._detail_type = detail_type
        self._identifier = identifier
        self._success = success
        self._description = description
        self._duration = duration
        self._bag_name = bag_name
        self._bag_store_name = bag_store_name

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationRunSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationRunSummary of this SimulationRunSummary.  # noqa: E501
        :rtype: SimulationRunSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail_type(self) -> str:
        """Gets the detail_type of this SimulationRunSummary.


        :return: The detail_type of this SimulationRunSummary.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type: str):
        """Sets the detail_type of this SimulationRunSummary.


        :param detail_type: The detail_type of this SimulationRunSummary.
        :type detail_type: str
        """
        if detail_type is None:
            raise ValueError("Invalid value for `detail_type`, must not be `None`")  # noqa: E501

        self._detail_type = detail_type

    @property
    def identifier(self) -> int:
        """Gets the identifier of this SimulationRunSummary.


        :return: The identifier of this SimulationRunSummary.
        :rtype: int
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: int):
        """Sets the identifier of this SimulationRunSummary.


        :param identifier: The identifier of this SimulationRunSummary.
        :type identifier: int
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def success(self) -> bool:
        """Gets the success of this SimulationRunSummary.


        :return: The success of this SimulationRunSummary.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this SimulationRunSummary.


        :param success: The success of this SimulationRunSummary.
        :type success: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def description(self) -> str:
        """Gets the description of this SimulationRunSummary.


        :return: The description of this SimulationRunSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this SimulationRunSummary.


        :param description: The description of this SimulationRunSummary.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def duration(self) -> float:
        """Gets the duration of this SimulationRunSummary.


        :return: The duration of this SimulationRunSummary.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        """Sets the duration of this SimulationRunSummary.


        :param duration: The duration of this SimulationRunSummary.
        :type duration: float
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def bag_name(self) -> str:
        """Gets the bag_name of this SimulationRunSummary.


        :return: The bag_name of this SimulationRunSummary.
        :rtype: str
        """
        return self._bag_name

    @bag_name.setter
    def bag_name(self, bag_name: str):
        """Sets the bag_name of this SimulationRunSummary.


        :param bag_name: The bag_name of this SimulationRunSummary.
        :type bag_name: str
        """

        self._bag_name = bag_name

    @property
    def bag_store_name(self) -> str:
        """Gets the bag_store_name of this SimulationRunSummary.


        :return: The bag_store_name of this SimulationRunSummary.
        :rtype: str
        """
        return self._bag_store_name

    @bag_store_name.setter
    def bag_store_name(self, bag_store_name: str):
        """Sets the bag_store_name of this SimulationRunSummary.


        :param bag_store_name: The bag_store_name of this SimulationRunSummary.
        :type bag_store_name: str
        """

        self._bag_store_name = bag_store_name
