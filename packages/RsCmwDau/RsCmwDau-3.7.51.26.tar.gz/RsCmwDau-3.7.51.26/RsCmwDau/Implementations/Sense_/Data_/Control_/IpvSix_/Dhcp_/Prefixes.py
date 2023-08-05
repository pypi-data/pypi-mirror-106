from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prefixes:
	"""Prefixes commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prefixes", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SENSe:DATA:CONTrol:IPVSix:DHCP:PREFixes:CATalog \n
		Snippet: value: List[str] = driver.sense.data.control.ipvSix.dhcp.prefixes.get_catalog() \n
		Queries the current IPv6 prefix pool for DUTs, configured via DHCP prefix delegation. \n
			:return: prefixes: Comma-separated list of strings, each string representing a pool entry
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVSix:DHCP:PREFixes:CATalog?')
		return Conversions.str_to_str_list(response)
