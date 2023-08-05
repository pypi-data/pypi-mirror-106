from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Session:
	"""Session commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("session", core, parent)

	@property
	def expiry(self):
		"""expiry commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_expiry'):
			from .Session_.Expiry import Expiry
			self._expiry = Expiry(self._core, self._base)
		return self._expiry

	@property
	def minSe(self):
		"""minSe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minSe'):
			from .Session_.MinSe import MinSe
			self._minSe = MinSe(self._core, self._base)
		return self._minSe

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Session_.Usage import Usage
			self._usage = Usage(self._core, self._base)
		return self._usage

	def clone(self) -> 'Session':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Session(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
