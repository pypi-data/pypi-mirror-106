from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Primary:
	"""Primary commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("primary", core, parent)

	def get_udhcp(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:UDHCp \n
		Snippet: value: bool = driver.configure.data.control.dns.foreign.ipvSix.primary.get_udhcp() \n
		No command help available \n
			:return: use_dhcpip_6: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:UDHCp?')
		return Conversions.str_to_bool(response)

	def set_udhcp(self, use_dhcpip_6: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:UDHCp \n
		Snippet: driver.configure.data.control.dns.foreign.ipvSix.primary.set_udhcp(use_dhcpip_6 = False) \n
		No command help available \n
			:param use_dhcpip_6: No help available
		"""
		param = Conversions.bool_to_str(use_dhcpip_6)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:UDHCp {param}')

	def get_address(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:ADDRess \n
		Snippet: value: str = driver.configure.data.control.dns.foreign.ipvSix.primary.get_address() \n
		Specifies the IPv6 address of the foreign primary DNS server. \n
			:return: fdns_prim_ip_6: IPv6 address as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:ADDRess?')
		return trim_str_response(response)

	def set_address(self, fdns_prim_ip_6: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:ADDRess \n
		Snippet: driver.configure.data.control.dns.foreign.ipvSix.primary.set_address(fdns_prim_ip_6 = '1') \n
		Specifies the IPv6 address of the foreign primary DNS server. \n
			:param fdns_prim_ip_6: IPv6 address as string
		"""
		param = Conversions.value_to_quoted_str(fdns_prim_ip_6)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:PRIMary:ADDRess {param}')
