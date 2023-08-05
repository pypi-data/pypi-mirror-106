from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Secondary:
	"""Secondary commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("secondary", core, parent)

	def get_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:DNS:CURRent:IPVFour:SECondary:ADDRess \n
		Snippet: value: str = driver.sense.data.control.dns.current.ipvFour.secondary.get_address() \n
		Queries the IPv4 address sent to the DUT as secondary DNS server address. \n
			:return: cdns_sec_ip_4: IPv4 address as string
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:DNS:CURRent:IPVFour:SECondary:ADDRess?')
		return trim_str_response(response)
