from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpReplay:
	"""IpReplay commands group definition. 6 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipReplay", core, parent)

	@property
	def createList(self):
		"""createList commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_createList'):
			from .IpReplay_.CreateList import CreateList
			self._createList = CreateList(self._core, self._base)
		return self._createList

	@property
	def removeList(self):
		"""removeList commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_removeList'):
			from .IpReplay_.RemoveList import RemoveList
			self._removeList = RemoveList(self._core, self._base)
		return self._removeList

	@property
	def iteration(self):
		"""iteration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iteration'):
			from .IpReplay_.Iteration import Iteration
			self._iteration = Iteration(self._core, self._base)
		return self._iteration

	@property
	def interface(self):
		"""interface commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interface'):
			from .IpReplay_.Interface import Interface
			self._interface = Interface(self._core, self._base)
		return self._interface

	@property
	def playAll(self):
		"""playAll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_playAll'):
			from .IpReplay_.PlayAll import PlayAll
			self._playAll = PlayAll(self._core, self._base)
		return self._playAll

	@property
	def stopAll(self):
		"""stopAll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stopAll'):
			from .IpReplay_.StopAll import StopAll
			self._stopAll = StopAll(self._core, self._base)
		return self._stopAll

	def clone(self) -> 'IpReplay':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpReplay(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
