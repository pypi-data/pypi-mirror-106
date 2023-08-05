from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Addresses:
	"""Addresses commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("addresses", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: SENSe:DATA:CONTrol:IPVFour:AUTomatic:ADDResses:CATalog \n
		Snippet: value: List[str] = driver.sense.data.control.ipvFour.automatic.addresses.get_catalog() \n
		Queries the current IPv4 address pool for DUTs, configured automatically (standalone setup) . \n
			:return: ip_address: Comma-separated list of strings. Each string represents an IPv4 address.
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVFour:AUTomatic:ADDResses:CATalog?')
		return Conversions.str_to_str_list(response)
