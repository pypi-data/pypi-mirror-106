from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prefixes:
	"""Prefixes commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prefixes", core, parent)

	def get_pool(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:PREFixes:POOL \n
		Snippet: value: bool = driver.configure.data.control.ipvSix.prefixes.get_pool() \n
		Enables or disables prefix delegation for automatic IPv6 configuration. \n
			:return: prefix_pool: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:PREFixes:POOL?')
		return Conversions.str_to_bool(response)

	def set_pool(self, prefix_pool: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:PREFixes:POOL \n
		Snippet: driver.configure.data.control.ipvSix.prefixes.set_pool(prefix_pool = False) \n
		Enables or disables prefix delegation for automatic IPv6 configuration. \n
			:param prefix_pool: OFF | ON
		"""
		param = Conversions.bool_to_str(prefix_pool)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:PREFixes:POOL {param}')
