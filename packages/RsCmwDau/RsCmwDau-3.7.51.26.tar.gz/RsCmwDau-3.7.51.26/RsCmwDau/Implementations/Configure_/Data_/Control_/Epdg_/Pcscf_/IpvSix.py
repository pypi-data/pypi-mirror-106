from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvSix:
	"""IpvSix commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvSix", core, parent)

	@property
	def address(self):
		"""address commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_address'):
			from .IpvSix_.Address import Address
			self._address = Address(self._core, self._base)
		return self._address

	def get_type_py(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:TYPE \n
		Snippet: value: int = driver.configure.data.control.epdg.pcscf.ipvSix.get_type_py() \n
		Sets the attribute type field of the P_CSCF_IP6_ADDRESS configuration attribute. \n
			:return: pcscf_ip_v_6_typ: Range: 0 to 65535
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:TYPE?')
		return Conversions.str_to_int(response)

	def set_type_py(self, pcscf_ip_v_6_typ: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:TYPE \n
		Snippet: driver.configure.data.control.epdg.pcscf.ipvSix.set_type_py(pcscf_ip_v_6_typ = 1) \n
		Sets the attribute type field of the P_CSCF_IP6_ADDRESS configuration attribute. \n
			:param pcscf_ip_v_6_typ: Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(pcscf_ip_v_6_typ)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:PCSCf:IPVSix:TYPE {param}')

	def clone(self) -> 'IpvSix':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpvSix(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
