from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ran:
	"""Ran commands group definition. 8 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ran", core, parent)

	@property
	def total(self):
		"""total commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_total'):
			from .Ran_.Total import Total
			self._total = Total(self._core, self._base)
		return self._total

	@property
	def dlink(self):
		"""dlink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlink'):
			from .Ran_.Dlink import Dlink
			self._dlink = Dlink(self._core, self._base)
		return self._dlink

	@property
	def ulink(self):
		"""ulink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulink'):
			from .Ran_.Ulink import Ulink
			self._ulink = Ulink(self._core, self._base)
		return self._ulink

	def clone(self) -> 'Ran':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ran(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
