from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcscf:
	"""Pcscf commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcscf", core, parent)

	# noinspection PyTypeChecker
	def get_atype(self) -> enums.AddressType:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:INTern:PCSCf:ATYPe \n
		Snippet: value: enums.AddressType = driver.configure.data.control.ims.intern.pcscf.get_atype() \n
		No command help available \n
			:return: addr_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:INTern:PCSCf:ATYPe?')
		return Conversions.str_to_scalar_enum(response, enums.AddressType)

	def set_atype(self, addr_type: enums.AddressType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:INTern:PCSCf:ATYPe \n
		Snippet: driver.configure.data.control.ims.intern.pcscf.set_atype(addr_type = enums.AddressType.IPVFour) \n
		No command help available \n
			:param addr_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(addr_type, enums.AddressType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:INTern:PCSCf:ATYPe {param}')
