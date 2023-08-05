from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prefixes:
	"""Prefixes commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prefixes", core, parent)

	def set_add(self, prefix: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:PREFixes:ADD \n
		Snippet: driver.configure.data.control.ipvSix.static.prefixes.set_add(prefix = '1') \n
		Adds a new prefix to the IPv6 prefix pool for DUTs, for static IPv6 configuration. \n
			:param prefix: String, e.g. 'fcb1:abab:cdcd:efe0::/64'
		"""
		param = Conversions.value_to_quoted_str(prefix)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:STATic:PREFixes:ADD {param}')

	def delete(self, prefix: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:PREFixes:DELete \n
		Snippet: driver.configure.data.control.ipvSix.static.prefixes.delete(prefix = 1) \n
		Deletes an entry from the IPv6 prefix pool for DUTs, for static IPv6 configuration. \n
			:param prefix: Entry to be deleted, either identified via its index number or its prefix string Range: 0 to total number of entries - 1 | 'prefix'
		"""
		param = Conversions.decimal_value_to_str(prefix)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:STATic:PREFixes:DELete {param}')
