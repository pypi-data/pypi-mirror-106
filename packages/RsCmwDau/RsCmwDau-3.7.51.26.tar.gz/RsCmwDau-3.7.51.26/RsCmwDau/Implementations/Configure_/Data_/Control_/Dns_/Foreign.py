from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foreign:
	"""Foreign commands group definition. 9 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("foreign", core, parent)

	@property
	def ipvFour(self):
		"""ipvFour commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Foreign_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	@property
	def ipvSix(self):
		"""ipvSix commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Foreign_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	# noinspection PyTypeChecker
	class UdhcpStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Prim_Ip_4: bool: OFF | ON DHCPv4 address, primary DNS server
			- Prim_Ip_6: bool: OFF | ON DHCPv6 address, primary DNS server
			- Sec_Ip_4: bool: OFF | ON DHCPv4 address, secondary DNS server
			- Sec_Ip_6: bool: OFF | ON DHCPv6 address, secondary DNS server"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Prim_Ip_4'),
			ArgStruct.scalar_bool('Prim_Ip_6'),
			ArgStruct.scalar_bool('Sec_Ip_4'),
			ArgStruct.scalar_bool('Sec_Ip_6')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Prim_Ip_4: bool = None
			self.Prim_Ip_6: bool = None
			self.Sec_Ip_4: bool = None
			self.Sec_Ip_6: bool = None

	def get_udhcp(self) -> UdhcpStruct:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:UDHCp \n
		Snippet: value: UdhcpStruct = driver.configure.data.control.dns.foreign.get_udhcp() \n
		Specifies whether an IP address received via DHCPv4 / DHCPv6 is used (if available) instead of the IPv4 / IPv6 address
		configured statically for the foreign DNS server. \n
			:return: structure: for return value, see the help for UdhcpStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:DNS:FOReign:UDHCp?', self.__class__.UdhcpStruct())

	def set_udhcp(self, value: UdhcpStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:FOReign:UDHCp \n
		Snippet: driver.configure.data.control.dns.foreign.set_udhcp(value = UdhcpStruct()) \n
		Specifies whether an IP address received via DHCPv4 / DHCPv6 is used (if available) instead of the IPv4 / IPv6 address
		configured statically for the foreign DNS server. \n
			:param value: see the help for UdhcpStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:DNS:FOReign:UDHCp', value)

	def clone(self) -> 'Foreign':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Foreign(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
