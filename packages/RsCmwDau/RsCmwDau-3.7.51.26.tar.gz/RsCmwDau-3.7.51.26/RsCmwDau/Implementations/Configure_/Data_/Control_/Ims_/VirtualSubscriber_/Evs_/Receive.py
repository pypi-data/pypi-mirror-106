from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Receive:
	"""Receive commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("receive", core, parent)

	@property
	def bitrate(self):
		"""bitrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bitrate'):
			from .Receive_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Receive_.Bw import Bw
			self._bw = Bw(self._core, self._base)
		return self._bw

	def clone(self) -> 'Receive':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Receive(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
