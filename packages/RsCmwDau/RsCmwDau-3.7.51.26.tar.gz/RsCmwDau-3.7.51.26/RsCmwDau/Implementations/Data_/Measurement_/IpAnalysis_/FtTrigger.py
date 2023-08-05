from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FtTrigger:
	"""FtTrigger commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ftTrigger", core, parent)

	@property
	def traces(self):
		"""traces commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_traces'):
			from .FtTrigger_.Traces import Traces
			self._traces = Traces(self._core, self._base)
		return self._traces

	@property
	def trigger(self):
		"""trigger commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .FtTrigger_.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	def clone(self) -> 'FtTrigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FtTrigger(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
