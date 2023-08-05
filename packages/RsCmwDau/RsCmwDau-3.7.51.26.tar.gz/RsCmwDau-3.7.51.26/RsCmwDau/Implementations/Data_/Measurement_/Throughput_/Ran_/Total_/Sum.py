from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sum:
	"""Sum commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sum", core, parent)

	@property
	def dlink(self):
		"""dlink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlink'):
			from .Sum_.Dlink import Dlink
			self._dlink = Dlink(self._core, self._base)
		return self._dlink

	@property
	def ulink(self):
		"""ulink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulink'):
			from .Sum_.Ulink import Ulink
			self._ulink = Ulink(self._core, self._base)
		return self._ulink

	def clone(self) -> 'Sum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
