from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evs:
	"""Evs commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evs", core, parent)

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Evs_.Bw import Bw
			self._bw = Bw(self._core, self._base)
		return self._bw

	@property
	def codec(self):
		"""codec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_codec'):
			from .Evs_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	def clone(self) -> 'Evs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
