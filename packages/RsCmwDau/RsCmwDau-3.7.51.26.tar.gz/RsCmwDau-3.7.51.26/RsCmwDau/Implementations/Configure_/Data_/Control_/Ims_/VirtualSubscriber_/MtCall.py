from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtCall:
	"""MtCall commands group definition. 25 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mtCall", core, parent)

	@property
	def sdp(self):
		"""sdp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdp'):
			from .MtCall_.Sdp import Sdp
			self._sdp = Sdp(self._core, self._base)
		return self._sdp

	@property
	def evs(self):
		"""evs commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_evs'):
			from .MtCall_.Evs import Evs
			self._evs = Evs(self._core, self._base)
		return self._evs

	@property
	def bearer(self):
		"""bearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bearer'):
			from .MtCall_.Bearer import Bearer
			self._bearer = Bearer(self._core, self._base)
		return self._bearer

	@property
	def destination(self):
		"""destination commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_destination'):
			from .MtCall_.Destination import Destination
			self._destination = Destination(self._core, self._base)
		return self._destination

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .MtCall_.TypePy import TypePy
			self._typePy = TypePy(self._core, self._base)
		return self._typePy

	@property
	def signalingType(self):
		"""signalingType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signalingType'):
			from .MtCall_.SignalingType import SignalingType
			self._signalingType = SignalingType(self._core, self._base)
		return self._signalingType

	@property
	def adCodec(self):
		"""adCodec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adCodec'):
			from .MtCall_.AdCodec import AdCodec
			self._adCodec = AdCodec(self._core, self._base)
		return self._adCodec

	@property
	def amr(self):
		"""amr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_amr'):
			from .MtCall_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	@property
	def video(self):
		"""video commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_video'):
			from .MtCall_.Video import Video
			self._video = Video(self._core, self._base)
		return self._video

	@property
	def call(self):
		"""call commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_call'):
			from .MtCall_.Call import Call
			self._call = Call(self._core, self._base)
		return self._call

	def clone(self) -> 'MtCall':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MtCall(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
