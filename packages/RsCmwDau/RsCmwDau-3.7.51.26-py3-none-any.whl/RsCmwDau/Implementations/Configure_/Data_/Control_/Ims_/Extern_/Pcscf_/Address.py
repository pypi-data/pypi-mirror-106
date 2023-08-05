from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("address", core, parent)

	@property
	def ipvFour(self):
		"""ipvFour commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Address_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	@property
	def ipvSix(self):
		"""ipvSix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Address_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	def clone(self) -> 'Address':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Address(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
