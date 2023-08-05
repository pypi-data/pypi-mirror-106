from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("address", core, parent)

	# noinspection PyTypeChecker
	def get_length(self) -> enums.IpV6AddLgh:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:ADDRess:LENGth \n
		Snippet: value: enums.IpV6AddLgh = driver.configure.data.control.epdg.pcscf.ipvSix.address.get_length() \n
		Sets the length field of the P_CSCF_IP6_ADDRESS configuration attribute. \n
			:return: ip_v_6_add_lgh: L16 | L17
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:ADDRess:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.IpV6AddLgh)

	def set_length(self, ip_v_6_add_lgh: enums.IpV6AddLgh) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:ADDRess:LENGth \n
		Snippet: driver.configure.data.control.epdg.pcscf.ipvSix.address.set_length(ip_v_6_add_lgh = enums.IpV6AddLgh.L16) \n
		Sets the length field of the P_CSCF_IP6_ADDRESS configuration attribute. \n
			:param ip_v_6_add_lgh: L16 | L17
		"""
		param = Conversions.enum_scalar_to_str(ip_v_6_add_lgh, enums.IpV6AddLgh)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:ADDRess:LENGth {param}')
