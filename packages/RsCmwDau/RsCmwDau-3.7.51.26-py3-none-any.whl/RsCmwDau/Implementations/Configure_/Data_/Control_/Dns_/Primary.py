from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Primary:
	"""Primary commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("primary", core, parent)

	# noinspection PyTypeChecker
	def get_stype(self) -> enums.ServerType:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:PRIMary:STYPe \n
		Snippet: value: enums.ServerType = driver.configure.data.control.dns.primary.get_stype() \n
		Select the primary and secondary DNS server type. \n
			:return: stype: NONE | INTernal | IAForeign | FOReign NONE: no DNS server address sent to the DUT INTernal: use local DNS server IAForeign: use local DNS server, if no entry found then foreign DNS server FOReign: use foreign DNS server
		"""
		response = self._core.io.query_str_with_opc('CONFigure:DATA:CONTrol:DNS:PRIMary:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.ServerType)

	def set_stype(self, stype: enums.ServerType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:PRIMary:STYPe \n
		Snippet: driver.configure.data.control.dns.primary.set_stype(stype = enums.ServerType.FOReign) \n
		Select the primary and secondary DNS server type. \n
			:param stype: NONE | INTernal | IAForeign | FOReign NONE: no DNS server address sent to the DUT INTernal: use local DNS server IAForeign: use local DNS server, if no entry found then foreign DNS server FOReign: use foreign DNS server
		"""
		param = Conversions.enum_scalar_to_str(stype, enums.ServerType)
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:DNS:PRIMary:STYPe {param}')
