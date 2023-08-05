from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 12 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def overall(self):
		"""overall commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_overall'):
			from .Trace_.Overall import Overall
			self._overall = Overall(self._core, self._base)
		return self._overall

	@property
	def ran(self):
		"""ran commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ran'):
			from .Trace_.Ran import Ran
			self._ran = Ran(self._core, self._base)
		return self._ran

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
