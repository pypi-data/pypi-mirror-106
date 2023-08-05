from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Primary:
	"""Primary commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("primary", core, parent)

	def get_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:DNS:CURRent:IPVSix:PRIMary:ADDRess \n
		Snippet: value: str = driver.sense.data.control.dns.current.ipvSix.primary.get_address() \n
		Queries the IPv6 address sent to the DUT as primary DNS server address. \n
			:return: cdns_prim_ip_6: IPv6 address as string
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:DNS:CURRent:IPVSix:PRIMary:ADDRess?')
		return trim_str_response(response)
