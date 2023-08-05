from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Routing:
	"""Routing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("routing", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.RoutingType:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:ROUTing:TYPE \n
		Snippet: value: enums.RoutingType = driver.configure.data.control.ipvSix.routing.get_type_py() \n
		Selects the mechanism to be used for IPv6 route configuration. The routes are only relevant for mobile-originating
		packets with destination addresses that do not belong to the subnet of the DAU and that are not reachable via the default
		router. \n
			:return: routing_type: MANual In the current software version, the value is fixed. MANual: manually configured routes
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:ROUTing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.RoutingType)

	def set_type_py(self, routing_type: enums.RoutingType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:ROUTing:TYPE \n
		Snippet: driver.configure.data.control.ipvSix.routing.set_type_py(routing_type = enums.RoutingType.MANual) \n
		Selects the mechanism to be used for IPv6 route configuration. The routes are only relevant for mobile-originating
		packets with destination addresses that do not belong to the subnet of the DAU and that are not reachable via the default
		router. \n
			:param routing_type: MANual In the current software version, the value is fixed. MANual: manually configured routes
		"""
		param = Conversions.enum_scalar_to_str(routing_type, enums.RoutingType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:ROUTing:TYPE {param}')
