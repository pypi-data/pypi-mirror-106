from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def get_smask(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IPVFour:CURRent:SMASk \n
		Snippet: value: str = driver.sense.data.control.ipvFour.current.get_smask() \n
		Queries the subnet mask of the current IPv4 data testing configuration. \n
			:return: subnet_mask: Subnet mask as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVFour:CURRent:SMASk?')
		return trim_str_response(response)

	def get_ip_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IPVFour:CURRent:IPADdress \n
		Snippet: value: str = driver.sense.data.control.ipvFour.current.get_ip_address() \n
		Queries the current IPv4 address of the DAU. \n
			:return: ip_address: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVFour:CURRent:IPADdress?')
		return trim_str_response(response)

	def get_gip(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IPVFour:CURRent:GIP \n
		Snippet: value: str = driver.sense.data.control.ipvFour.current.get_gip() \n
		Queries the current IPv4 address of the gateway server. \n
			:return: gateway_ip: IP address as string Range: '0.0.0.0' to '255.255.255.255'
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVFour:CURRent:GIP?')
		return trim_str_response(response)
