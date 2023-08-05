from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inband:
	"""Inband commands group definition. 6 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("inband", core, parent)

	@property
	def perform(self):
		"""perform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perform'):
			from .Inband_.Perform import Perform
			self._perform = Perform(self._core, self._base)
		return self._perform

	@property
	def evs(self):
		"""evs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_evs'):
			from .Inband_.Evs import Evs
			self._evs = Evs(self._core, self._base)
		return self._evs

	@property
	def repetition(self):
		"""repetition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repetition'):
			from .Inband_.Repetition import Repetition
			self._repetition = Repetition(self._core, self._base)
		return self._repetition

	@property
	def amRnb(self):
		"""amRnb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amRnb'):
			from .Inband_.AmRnb import AmRnb
			self._amRnb = AmRnb(self._core, self._base)
		return self._amRnb

	@property
	def amRwb(self):
		"""amRwb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amRwb'):
			from .Inband_.AmRwb import AmRwb
			self._amRwb = AmRwb(self._core, self._base)
		return self._amRwb

	def clone(self) -> 'Inband':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Inband(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
