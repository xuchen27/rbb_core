# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.simulation_environment_summary import SimulationEnvironmentSummary  # noqa: F401,E501
from rbb_swagger_server import util


class SimulationEnvironmentDetailed(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, detail_type: str=None, name: str=None, module_name: str=None, rosbag_store: str=None, config: object=None, example_config: str=None):  # noqa: E501
        """SimulationEnvironmentDetailed - a model defined in Swagger

        :param detail_type: The detail_type of this SimulationEnvironmentDetailed.  # noqa: E501
        :type detail_type: str
        :param name: The name of this SimulationEnvironmentDetailed.  # noqa: E501
        :type name: str
        :param module_name: The module_name of this SimulationEnvironmentDetailed.  # noqa: E501
        :type module_name: str
        :param rosbag_store: The rosbag_store of this SimulationEnvironmentDetailed.  # noqa: E501
        :type rosbag_store: str
        :param config: The config of this SimulationEnvironmentDetailed.  # noqa: E501
        :type config: object
        :param example_config: The example_config of this SimulationEnvironmentDetailed.  # noqa: E501
        :type example_config: str
        """
        self.swagger_types = {
            'detail_type': str,
            'name': str,
            'module_name': str,
            'rosbag_store': str,
            'config': object,
            'example_config': str
        }

        self.attribute_map = {
            'detail_type': 'detail_type',
            'name': 'name',
            'module_name': 'module_name',
            'rosbag_store': 'rosbag_store',
            'config': 'config',
            'example_config': 'example_config'
        }

        self._detail_type = detail_type
        self._name = name
        self._module_name = module_name
        self._rosbag_store = rosbag_store
        self._config = config
        self._example_config = example_config

    @classmethod
    def from_dict(cls, dikt) -> 'SimulationEnvironmentDetailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SimulationEnvironmentDetailed of this SimulationEnvironmentDetailed.  # noqa: E501
        :rtype: SimulationEnvironmentDetailed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail_type(self) -> str:
        """Gets the detail_type of this SimulationEnvironmentDetailed.


        :return: The detail_type of this SimulationEnvironmentDetailed.
        :rtype: str
        """
        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type: str):
        """Sets the detail_type of this SimulationEnvironmentDetailed.


        :param detail_type: The detail_type of this SimulationEnvironmentDetailed.
        :type detail_type: str
        """
        if detail_type is None:
            raise ValueError("Invalid value for `detail_type`, must not be `None`")  # noqa: E501

        self._detail_type = detail_type

    @property
    def name(self) -> str:
        """Gets the name of this SimulationEnvironmentDetailed.


        :return: The name of this SimulationEnvironmentDetailed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SimulationEnvironmentDetailed.


        :param name: The name of this SimulationEnvironmentDetailed.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def module_name(self) -> str:
        """Gets the module_name of this SimulationEnvironmentDetailed.


        :return: The module_name of this SimulationEnvironmentDetailed.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name: str):
        """Sets the module_name of this SimulationEnvironmentDetailed.


        :param module_name: The module_name of this SimulationEnvironmentDetailed.
        :type module_name: str
        """
        if module_name is None:
            raise ValueError("Invalid value for `module_name`, must not be `None`")  # noqa: E501

        self._module_name = module_name

    @property
    def rosbag_store(self) -> str:
        """Gets the rosbag_store of this SimulationEnvironmentDetailed.


        :return: The rosbag_store of this SimulationEnvironmentDetailed.
        :rtype: str
        """
        return self._rosbag_store

    @rosbag_store.setter
    def rosbag_store(self, rosbag_store: str):
        """Sets the rosbag_store of this SimulationEnvironmentDetailed.


        :param rosbag_store: The rosbag_store of this SimulationEnvironmentDetailed.
        :type rosbag_store: str
        """

        self._rosbag_store = rosbag_store

    @property
    def config(self) -> object:
        """Gets the config of this SimulationEnvironmentDetailed.

        Configuration of the simulation environment.  # noqa: E501

        :return: The config of this SimulationEnvironmentDetailed.
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config: object):
        """Sets the config of this SimulationEnvironmentDetailed.

        Configuration of the simulation environment.  # noqa: E501

        :param config: The config of this SimulationEnvironmentDetailed.
        :type config: object
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def example_config(self) -> str:
        """Gets the example_config of this SimulationEnvironmentDetailed.

        Example simulation configuration shown in the simulation overview  # noqa: E501

        :return: The example_config of this SimulationEnvironmentDetailed.
        :rtype: str
        """
        return self._example_config

    @example_config.setter
    def example_config(self, example_config: str):
        """Sets the example_config of this SimulationEnvironmentDetailed.

        Example simulation configuration shown in the simulation overview  # noqa: E501

        :param example_config: The example_config of this SimulationEnvironmentDetailed.
        :type example_config: str
        """
        if example_config is None:
            raise ValueError("Invalid value for `example_config`, must not be `None`")  # noqa: E501

        self._example_config = example_config
