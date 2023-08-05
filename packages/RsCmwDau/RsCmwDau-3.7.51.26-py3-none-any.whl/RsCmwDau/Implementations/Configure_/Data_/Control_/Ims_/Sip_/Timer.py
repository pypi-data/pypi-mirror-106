from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timer:
	"""Timer commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("timer", core, parent)

	@property
	def case(self):
		"""case commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_case'):
			from .Timer_.Case import Case
			self._case = Case(self._core, self._base)
		return self._case

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Timer_.Value import Value
			self._value = Value(self._core, self._base)
		return self._value

	def clone(self) -> 'Timer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Timer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
