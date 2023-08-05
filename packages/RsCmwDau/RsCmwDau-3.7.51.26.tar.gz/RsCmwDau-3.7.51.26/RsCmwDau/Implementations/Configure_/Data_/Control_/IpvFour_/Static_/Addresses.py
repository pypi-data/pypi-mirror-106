from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Addresses:
	"""Addresses commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("addresses", core, parent)

	def set_add(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:ADDResses:ADD \n
		Snippet: driver.configure.data.control.ipvFour.static.addresses.set_add(ip_address = '1') \n
		Adds an IP address to the IPv4 address pool for DUTs, for static IPv4 configuration. \n
			:param ip_address: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:STATic:ADDResses:ADD {param}')

	def delete(self, ip_address: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:STATic:ADDResses:DELete \n
		Snippet: driver.configure.data.control.ipvFour.static.addresses.delete(ip_address = 1) \n
		Deletes an address from the IPv4 address pool for DUTs, for static IPv4 configuration. \n
			:param ip_address: IP address to be deleted, either identified via its index number or as string Range: 0 to total number of entries - 1 | '0.0.0.0' to '255.255.255.255'
		"""
		param = Conversions.decimal_value_to_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:STATic:ADDResses:DELete {param}')
