from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prefix:
	"""Prefix commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prefix", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.PrefixType:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:MOBile:PREFix:TYPE \n
		Snippet: value: enums.PrefixType = driver.configure.data.control.ipvSix.mobile.prefix.get_type_py() \n
		Selects the method to be used to define the IPv6 prefix pool for DUTs. This setting is only relevant for test setups with
		connected external network. It is ignored for a standalone test setup (AUTO set via method RsCmwDau.Configure.Data.
		Control.IpvSix.Address.typePy) . \n
			:return: prefix_type: STATic | DHCP STATic: static IP configuration DHCP: DHCP prefix delegation
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:MOBile:PREFix:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.PrefixType)

	def set_type_py(self, prefix_type: enums.PrefixType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:MOBile:PREFix:TYPE \n
		Snippet: driver.configure.data.control.ipvSix.mobile.prefix.set_type_py(prefix_type = enums.PrefixType.DHCP) \n
		Selects the method to be used to define the IPv6 prefix pool for DUTs. This setting is only relevant for test setups with
		connected external network. It is ignored for a standalone test setup (AUTO set via method RsCmwDau.Configure.Data.
		Control.IpvSix.Address.typePy) . \n
			:param prefix_type: STATic | DHCP STATic: static IP configuration DHCP: DHCP prefix delegation
		"""
		param = Conversions.enum_scalar_to_str(prefix_type, enums.PrefixType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:MOBile:PREFix:TYPE {param}')
