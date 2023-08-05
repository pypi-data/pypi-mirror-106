from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Chat:
	"""Chat commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("chat", core, parent)

	@property
	def perform(self):
		"""perform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perform'):
			from .Chat_.Perform import Perform
			self._perform = Perform(self._core, self._base)
		return self._perform

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Chat_.Text import Text
			self._text = Text(self._core, self._base)
		return self._text

	def clone(self) -> 'Chat':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Chat(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
