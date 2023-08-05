from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def get_ip_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IPVSix:CURRent:IPADdress \n
		Snippet: value: str = driver.sense.data.control.ipvSix.current.get_ip_address() \n
		Queries the current IPv6 address of the DAU. \n
			:return: ip_address: IPv6 address as string, e.g.'fcb1:abab:cdcd:efe0::1/64'
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVSix:CURRent:IPADdress?')
		return trim_str_response(response)

	def get_drouter(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IPVSix:CURRent:DROuter \n
		Snippet: value: str = driver.sense.data.control.ipvSix.current.get_drouter() \n
		Queries the IPv6 address currently used to address the default router. \n
			:return: def_router: IPv6 address as string, e.g. 'fcb1:abab:cdcd:efe0::1'
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IPVSix:CURRent:DROuter?')
		return trim_str_response(response)
