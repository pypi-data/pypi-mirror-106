from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VoIms:
	"""VoIms commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("voIms", core, parent)

	@property
	def bitrate(self):
		"""bitrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bitrate'):
			from .VoIms_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	@property
	def flows(self):
		"""flows commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_flows'):
			from .VoIms_.Flows import Flows
			self._flows = Flows(self._core, self._base)
		return self._flows

	@property
	def perdTx(self):
		"""perdTx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perdTx'):
			from .VoIms_.PerdTx import PerdTx
			self._perdTx = PerdTx(self._core, self._base)
		return self._perdTx

	@property
	def jitter(self):
		"""jitter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jitter'):
			from .VoIms_.Jitter import Jitter
			self._jitter = Jitter(self._core, self._base)
		return self._jitter

	def clone(self) -> 'VoIms':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VoIms(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
