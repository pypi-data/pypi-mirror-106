from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 33 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("update", core, parent)

	@property
	def rcs(self):
		"""rcs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rcs'):
			from .Update_.Rcs import Rcs
			self._rcs = Rcs(self._core, self._base)
		return self._rcs

	@property
	def inband(self):
		"""inband commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_inband'):
			from .Update_.Inband import Inband
			self._inband = Inband(self._core, self._base)
		return self._inband

	@property
	def call(self):
		"""call commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_call'):
			from .Update_.Call import Call
			self._call = Call(self._core, self._base)
		return self._call

	@property
	def evs(self):
		"""evs commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_evs'):
			from .Update_.Evs import Evs
			self._evs = Evs(self._core, self._base)
		return self._evs

	@property
	def adCodec(self):
		"""adCodec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adCodec'):
			from .Update_.AdCodec import AdCodec
			self._adCodec = AdCodec(self._core, self._base)
		return self._adCodec

	@property
	def amr(self):
		"""amr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_amr'):
			from .Update_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	@property
	def video(self):
		"""video commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_video'):
			from .Update_.Video import Video
			self._video = Video(self._core, self._base)
		return self._video

	@property
	def perform(self):
		"""perform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perform'):
			from .Update_.Perform import Perform
			self._perform = Perform(self._core, self._base)
		return self._perform

	def clone(self) -> 'Update':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Update(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
