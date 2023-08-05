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
	def get_type_py(self) -> enums.AddressModeB:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:ADDRess:TYPE \n
		Snippet: value: enums.AddressModeB = driver.configure.data.control.ipvSix.address.get_type_py() \n
		Selects the method to be used for IPv6 DAU address configuration. \n
			:return: address_type: AUTO | STATic | ACONf AUTO: predefined automatic configuration (standalone setup) STATic: static IP configuration ACONf: dynamic autoconfiguration
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:ADDRess:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AddressModeB)

	def set_type_py(self, address_type: enums.AddressModeB) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:ADDRess:TYPE \n
		Snippet: driver.configure.data.control.ipvSix.address.set_type_py(address_type = enums.AddressModeB.ACONf) \n
		Selects the method to be used for IPv6 DAU address configuration. \n
			:param address_type: AUTO | STATic | ACONf AUTO: predefined automatic configuration (standalone setup) STATic: static IP configuration ACONf: dynamic autoconfiguration
		"""
		param = Conversions.enum_scalar_to_str(address_type, enums.AddressModeB)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:ADDRess:TYPE {param}')
