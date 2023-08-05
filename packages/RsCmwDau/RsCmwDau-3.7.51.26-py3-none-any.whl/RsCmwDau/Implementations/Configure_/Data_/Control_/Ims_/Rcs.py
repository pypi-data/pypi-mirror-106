from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rcs:
	"""Rcs commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rcs", core, parent)

	@property
	def grpChat(self):
		"""grpChat commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_grpChat'):
			from .Rcs_.GrpChat import GrpChat
			self._grpChat = GrpChat(self._core, self._base)
		return self._grpChat

	def clone(self) -> 'Rcs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rcs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
