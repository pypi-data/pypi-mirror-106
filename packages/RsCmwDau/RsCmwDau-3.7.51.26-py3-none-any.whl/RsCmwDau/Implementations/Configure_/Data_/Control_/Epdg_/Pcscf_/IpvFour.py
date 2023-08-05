from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvFour:
	"""IpvFour commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvFour", core, parent)

	def get_type_py(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVFour:TYPE \n
		Snippet: value: int = driver.configure.data.control.epdg.pcscf.ipvFour.get_type_py() \n
		Sets the attribute type field of the P_CSCF_IP4_ADDRESS configuration attribute. \n
			:return: pcscf_ip_v_4_typ: Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVFour:TYPE?')
		return Conversions.str_to_int(response)

	def set_type_py(self, pcscf_ip_v_4_typ: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVFour:TYPE \n
		Snippet: driver.configure.data.control.epdg.pcscf.ipvFour.set_type_py(pcscf_ip_v_4_typ = 1) \n
		Sets the attribute type field of the P_CSCF_IP4_ADDRESS configuration attribute. \n
			:param pcscf_ip_v_4_typ: Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(pcscf_ip_v_4_typ)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVFour:TYPE {param}')
