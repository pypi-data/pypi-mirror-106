from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trigger", core, parent)

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Trigger_.Start import Start
			self._start = Start(self._core, self._base)
		return self._start

	@property
	def end(self):
		"""end commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_end'):
			from .Trigger_.End import End
			self._end = End(self._core, self._base)
		return self._end

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
