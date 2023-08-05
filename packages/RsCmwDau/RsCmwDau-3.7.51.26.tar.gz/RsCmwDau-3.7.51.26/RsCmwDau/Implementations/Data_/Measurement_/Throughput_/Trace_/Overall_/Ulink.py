from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulink:
	"""Ulink commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ulink", core, parent)

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extended'):
			from .Ulink_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Ulink_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'Ulink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ulink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
