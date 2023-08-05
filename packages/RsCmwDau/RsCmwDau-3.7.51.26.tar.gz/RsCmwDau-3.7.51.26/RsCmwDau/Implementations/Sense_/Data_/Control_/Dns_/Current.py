from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def ipvFour(self):
		"""ipvFour commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Current_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	@property
	def ipvSix(self):
		"""ipvSix commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Current_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
