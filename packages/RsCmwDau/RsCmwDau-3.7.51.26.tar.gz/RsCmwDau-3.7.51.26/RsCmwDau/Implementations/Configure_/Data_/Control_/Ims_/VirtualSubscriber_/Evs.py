from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evs:
	"""Evs commands group definition. 15 total commands, 13 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evs", core, parent)

	@property
	def io(self):
		"""io commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_io'):
			from .Evs_.Io import Io
			self._io = Io(self._core, self._base)
		return self._io

	@property
	def codec(self):
		"""codec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_codec'):
			from .Evs_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	@property
	def common(self):
		"""common commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_common'):
			from .Evs_.Common import Common
			self._common = Common(self._core, self._base)
		return self._common

	@property
	def receive(self):
		"""receive commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_receive'):
			from .Evs_.Receive import Receive
			self._receive = Receive(self._core, self._base)
		return self._receive

	@property
	def send(self):
		"""send commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_send'):
			from .Evs_.Send import Send
			self._send = Send(self._core, self._base)
		return self._send

	@property
	def synch(self):
		"""synch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_synch'):
			from .Evs_.Synch import Synch
			self._synch = Synch(self._core, self._base)
		return self._synch

	@property
	def startMode(self):
		"""startMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_startMode'):
			from .Evs_.StartMode import StartMode
			self._startMode = StartMode(self._core, self._base)
		return self._startMode

	@property
	def chawMode(self):
		"""chawMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chawMode'):
			from .Evs_.ChawMode import ChawMode
			self._chawMode = ChawMode(self._core, self._base)
		return self._chawMode

	@property
	def cmr(self):
		"""cmr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmr'):
			from .Evs_.Cmr import Cmr
			self._cmr = Cmr(self._core, self._base)
		return self._cmr

	@property
	def dtxRecv(self):
		"""dtxRecv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtxRecv'):
			from .Evs_.DtxRecv import DtxRecv
			self._dtxRecv = DtxRecv(self._core, self._base)
		return self._dtxRecv

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtx'):
			from .Evs_.Dtx import Dtx
			self._dtx = Dtx(self._core, self._base)
		return self._dtx

	@property
	def hfOnly(self):
		"""hfOnly commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hfOnly'):
			from .Evs_.HfOnly import HfOnly
			self._hfOnly = HfOnly(self._core, self._base)
		return self._hfOnly

	@property
	def bwCommon(self):
		"""bwCommon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwCommon'):
			from .Evs_.BwCommon import BwCommon
			self._bwCommon = BwCommon(self._core, self._base)
		return self._bwCommon

	def clone(self) -> 'Evs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
