from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("address", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.AddressModeA:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:ADDRess:TYPE \n
		Snippet: value: enums.AddressModeA = driver.configure.data.control.ipvFour.address.get_type_py() \n
		Selects the type of the IPv4 configuration. \n
			:return: address_type: AUTomatic | STATic | DHCPv4 AUTomatic: predefined internal IP configuration STATic: user-defined static IP configuration defined via the commands CONFigure:DATA:CONTrol:IPVFour:STATic:... DHCPv4: the IPv4 address is obtained from a DHCP server in the company LAN
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVFour:ADDRess:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AddressModeA)

	def set_type_py(self, address_type: enums.AddressModeA) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVFour:ADDRess:TYPE \n
		Snippet: driver.configure.data.control.ipvFour.address.set_type_py(address_type = enums.AddressModeA.AUTomatic) \n
		Selects the type of the IPv4 configuration. \n
			:param address_type: AUTomatic | STATic | DHCPv4 AUTomatic: predefined internal IP configuration STATic: user-defined static IP configuration defined via the commands CONFigure:DATA:CONTrol:IPVFour:STATic:... DHCPv4: the IPv4 address is obtained from a DHCP server in the company LAN
		"""
		param = Conversions.enum_scalar_to_str(address_type, enums.AddressModeA)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVFour:ADDRess:TYPE {param}')
