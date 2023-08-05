from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Static:
	"""Static commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("static", core, parent)

	@property
	def addresses(self):
		"""addresses commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_addresses'):
			from .Static_.Addresses import Addresses
			self._addresses = Addresses(self._core, self._base)
		return self._addresses

	def get_gip(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:GIP \n
		Snippet: value: str = driver.configure.data.control.ipvFour.static.get_gip() \n
		Defines the address of an external gateway to be used for static IPv4 configuration. \n
			:return: gateway_ip: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVFour:STATic:GIP?')
		return trim_str_response(response)

	def set_gip(self, gateway_ip: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:GIP \n
		Snippet: driver.configure.data.control.ipvFour.static.set_gip(gateway_ip = '1') \n
		Defines the address of an external gateway to be used for static IPv4 configuration. \n
			:param gateway_ip: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		param = Conversions.value_to_quoted_str(gateway_ip)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:STATic:GIP {param}')

	def get_ip_address(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:IPADdress \n
		Snippet: value: str = driver.configure.data.control.ipvFour.static.get_ip_address() \n
		Sets the IP address of the DAU to be used for static IPv4 configuration. \n
			:return: ip_address: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVFour:STATic:IPADdress?')
		return trim_str_response(response)

	def set_ip_address(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:IPADdress \n
		Snippet: driver.configure.data.control.ipvFour.static.set_ip_address(ip_address = '1') \n
		Sets the IP address of the DAU to be used for static IPv4 configuration. \n
			:param ip_address: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:STATic:IPADdress {param}')

	def get_smask(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:SMASk \n
		Snippet: value: str = driver.configure.data.control.ipvFour.static.get_smask() \n
		Defines the subnet mask for static IPv4 configuration. \n
			:return: subnet_mask: Subnet mask as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVFour:STATic:SMASk?')
		return trim_str_response(response)

	def set_smask(self, subnet_mask: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:SMASk \n
		Snippet: driver.configure.data.control.ipvFour.static.set_smask(subnet_mask = '1') \n
		Defines the subnet mask for static IPv4 configuration. \n
			:param subnet_mask: Subnet mask as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		param = Conversions.value_to_quoted_str(subnet_mask)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:STATic:SMASk {param}')

	def clone(self) -> 'Static':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Static(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
