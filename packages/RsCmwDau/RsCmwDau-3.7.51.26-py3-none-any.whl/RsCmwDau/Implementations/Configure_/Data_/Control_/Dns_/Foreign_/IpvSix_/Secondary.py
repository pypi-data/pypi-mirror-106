from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Secondary:
	"""Secondary commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("secondary", core, parent)

	def get_udhcp(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:UDHCp \n
		Snippet: value: bool = driver.configure.data.control.dns.foreign.ipvSix.secondary.get_udhcp() \n
		No command help available \n
			:return: use_dhcpip_6: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:UDHCp?')
		return Conversions.str_to_bool(response)

	def set_udhcp(self, use_dhcpip_6: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:UDHCp \n
		Snippet: driver.configure.data.control.dns.foreign.ipvSix.secondary.set_udhcp(use_dhcpip_6 = False) \n
		No command help available \n
			:param use_dhcpip_6: No help available
		"""
		param = Conversions.bool_to_str(use_dhcpip_6)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:UDHCp {param}')

	def get_address(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:ADDRess \n
		Snippet: value: str = driver.configure.data.control.dns.foreign.ipvSix.secondary.get_address() \n
		Specifies the IPv6 address of the foreign secondary DNS server. \n
			:return: fdns_sec_ip_6: IPv6 address as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:ADDRess?')
		return trim_str_response(response)

	def set_address(self, fdns_sec_ip_6: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:ADDRess \n
		Snippet: driver.configure.data.control.dns.foreign.ipvSix.secondary.set_address(fdns_sec_ip_6 = '1') \n
		Specifies the IPv6 address of the foreign secondary DNS server. \n
			:param fdns_sec_ip_6: IPv6 address as string
		"""
		param = Conversions.value_to_quoted_str(fdns_sec_ip_6)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:FOReign:IPVSix:SECondary:ADDRess {param}')
