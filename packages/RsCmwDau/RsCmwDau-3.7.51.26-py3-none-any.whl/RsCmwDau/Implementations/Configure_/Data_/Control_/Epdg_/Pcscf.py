from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcscf:
	"""Pcscf commands group definition. 4 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcscf", core, parent)

	@property
	def ipvSix(self):
		"""ipvSix commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Pcscf_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	@property
	def ipvFour(self):
		"""ipvFour commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Pcscf_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:AUTO \n
		Snippet: value: bool = driver.configure.data.control.epdg.pcscf.get_auto() \n
		Enables or disables the automatic mode for the IPv4 and IPv6 type settings. \n
			:return: auto: OFF | ON OFF: The configured IP types are used. ON: The IP type offered by the DUT is used.
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:PCSCf:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, auto: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:PCSCf:AUTO \n
		Snippet: driver.configure.data.control.epdg.pcscf.set_auto(auto = False) \n
		Enables or disables the automatic mode for the IPv4 and IPv6 type settings. \n
			:param auto: OFF | ON OFF: The configured IP types are used. ON: The IP type offered by the DUT is used.
		"""
		param = Conversions.bool_to_str(auto)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:PCSCf:AUTO {param}')

	def clone(self) -> 'Pcscf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcscf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
