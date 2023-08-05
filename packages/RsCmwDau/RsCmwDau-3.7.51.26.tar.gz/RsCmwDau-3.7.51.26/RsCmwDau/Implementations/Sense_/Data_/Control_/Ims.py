from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ims:
	"""Ims commands group definition. 28 total commands, 14 Sub-groups, 0 group commands
	Repeated Capability: Ims, default value after init: Ims.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ims", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_ims_get', 'repcap_ims_set', repcap.Ims.Ix1)

	def repcap_ims_set(self, enum_value: repcap.Ims) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Ims.Default
		Default value after init: Ims.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_ims_get(self) -> repcap.Ims:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def ecall(self):
		"""ecall commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ecall'):
			from .Ims_.Ecall import Ecall
			self._ecall = Ecall(self._core, self._base)
		return self._ecall

	@property
	def rcs(self):
		"""rcs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rcs'):
			from .Ims_.Rcs import Rcs
			self._rcs = Rcs(self._core, self._base)
		return self._rcs

	@property
	def conference(self):
		"""conference commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_conference'):
			from .Ims_.Conference import Conference
			self._conference = Conference(self._core, self._base)
		return self._conference

	@property
	def mobile(self):
		"""mobile commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_mobile'):
			from .Ims_.Mobile import Mobile
			self._mobile = Mobile(self._core, self._base)
		return self._mobile

	@property
	def pcscf(self):
		"""pcscf commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcscf'):
			from .Ims_.Pcscf import Pcscf
			self._pcscf = Pcscf(self._core, self._base)
		return self._pcscf

	@property
	def intern(self):
		"""intern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_intern'):
			from .Ims_.Intern import Intern
			self._intern = Intern(self._core, self._base)
		return self._intern

	@property
	def ginfo(self):
		"""ginfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ginfo'):
			from .Ims_.Ginfo import Ginfo
			self._ginfo = Ginfo(self._core, self._base)
		return self._ginfo

	@property
	def virtualSubscriber(self):
		"""virtualSubscriber commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_virtualSubscriber'):
			from .Ims_.VirtualSubscriber import VirtualSubscriber
			self._virtualSubscriber = VirtualSubscriber(self._core, self._base)
		return self._virtualSubscriber

	@property
	def events(self):
		"""events commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_events'):
			from .Ims_.Events import Events
			self._events = Events(self._core, self._base)
		return self._events

	@property
	def subscriber(self):
		"""subscriber commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subscriber'):
			from .Ims_.Subscriber import Subscriber
			self._subscriber = Subscriber(self._core, self._base)
		return self._subscriber

	@property
	def history(self):
		"""history commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_history'):
			from .Ims_.History import History
			self._history = History(self._core, self._base)
		return self._history

	@property
	def release(self):
		"""release commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_release'):
			from .Ims_.Release import Release
			self._release = Release(self._core, self._base)
		return self._release

	@property
	def sms(self):
		"""sms commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Ims_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def voice(self):
		"""voice commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_voice'):
			from .Ims_.Voice import Voice
			self._voice = Voice(self._core, self._base)
		return self._voice

	def clone(self) -> 'Ims':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ims(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
