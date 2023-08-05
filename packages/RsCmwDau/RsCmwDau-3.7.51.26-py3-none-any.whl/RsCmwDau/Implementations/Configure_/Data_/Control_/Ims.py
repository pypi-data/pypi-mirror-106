from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ims:
	"""Ims commands group definition. 185 total commands, 19 Sub-groups, 0 group commands
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
	def virtualSubscriber(self):
		"""virtualSubscriber commands group. 24 Sub-classes, 1 commands."""
		if not hasattr(self, '_virtualSubscriber'):
			from .Ims_.VirtualSubscriber import VirtualSubscriber
			self._virtualSubscriber = VirtualSubscriber(self._core, self._base)
		return self._virtualSubscriber

	@property
	def sip(self):
		"""sip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sip'):
			from .Ims_.Sip import Sip
			self._sip = Sip(self._core, self._base)
		return self._sip

	@property
	def rcs(self):
		"""rcs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rcs'):
			from .Ims_.Rcs import Rcs
			self._rcs = Rcs(self._core, self._base)
		return self._rcs

	@property
	def conference(self):
		"""conference commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_conference'):
			from .Ims_.Conference import Conference
			self._conference = Conference(self._core, self._base)
		return self._conference

	@property
	def tcpAlive(self):
		"""tcpAlive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcpAlive'):
			from .Ims_.TcpAlive import TcpAlive
			self._tcpAlive = TcpAlive(self._core, self._base)
		return self._tcpAlive

	@property
	def threshold(self):
		"""threshold commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_threshold'):
			from .Ims_.Threshold import Threshold
			self._threshold = Threshold(self._core, self._base)
		return self._threshold

	@property
	def transport(self):
		"""transport commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_transport'):
			from .Ims_.Transport import Transport
			self._transport = Transport(self._core, self._base)
		return self._transport

	@property
	def mobile(self):
		"""mobile commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mobile'):
			from .Ims_.Mobile import Mobile
			self._mobile = Mobile(self._core, self._base)
		return self._mobile

	@property
	def susage(self):
		"""susage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_susage'):
			from .Ims_.Susage import Susage
			self._susage = Susage(self._core, self._base)
		return self._susage

	@property
	def intern(self):
		"""intern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_intern'):
			from .Ims_.Intern import Intern
			self._intern = Intern(self._core, self._base)
		return self._intern

	@property
	def extern(self):
		"""extern commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_extern'):
			from .Ims_.Extern import Extern
			self._extern = Extern(self._core, self._base)
		return self._extern

	@property
	def uauthentication(self):
		"""uauthentication commands group. 1 Sub-classes, 11 commands."""
		if not hasattr(self, '_uauthentication'):
			from .Ims_.Uauthentication import Uauthentication
			self._uauthentication = Uauthentication(self._core, self._base)
		return self._uauthentication

	@property
	def clean(self):
		"""clean commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clean'):
			from .Ims_.Clean import Clean
			self._clean = Clean(self._core, self._base)
		return self._clean

	@property
	def subscriber(self):
		"""subscriber commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_subscriber'):
			from .Ims_.Subscriber import Subscriber
			self._subscriber = Subscriber(self._core, self._base)
		return self._subscriber

	@property
	def pcscf(self):
		"""pcscf commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcscf'):
			from .Ims_.Pcscf import Pcscf
			self._pcscf = Pcscf(self._core, self._base)
		return self._pcscf

	@property
	def update(self):
		"""update commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_update'):
			from .Ims_.Update import Update
			self._update = Update(self._core, self._base)
		return self._update

	@property
	def release(self):
		"""release commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_release'):
			from .Ims_.Release import Release
			self._release = Release(self._core, self._base)
		return self._release

	@property
	def sms(self):
		"""sms commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_sms'):
			from .Ims_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def voice(self):
		"""voice commands group. 3 Sub-classes, 6 commands."""
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
