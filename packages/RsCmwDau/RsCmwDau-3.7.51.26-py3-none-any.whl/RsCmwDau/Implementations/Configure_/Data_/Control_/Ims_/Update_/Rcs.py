from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rcs:
	"""Rcs commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rcs", core, parent)

	@property
	def chat(self):
		"""chat commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_chat'):
			from .Rcs_.Chat import Chat
			self._chat = Chat(self._core, self._base)
		return self._chat

	@property
	def idle(self):
		"""idle commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_idle'):
			from .Rcs_.Idle import Idle
			self._idle = Idle(self._core, self._base)
		return self._idle

	@property
	def compSng(self):
		"""compSng commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_compSng'):
			from .Rcs_.CompSng import CompSng
			self._compSng = CompSng(self._core, self._base)
		return self._compSng

	def clone(self) -> 'Rcs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rcs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
