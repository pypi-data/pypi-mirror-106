from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nimpairments:
	"""Nimpairments commands group definition. 10 total commands, 10 Sub-groups, 0 group commands
	Repeated Capability: Impairments, default value after init: Impairments.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nimpairments", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_impairments_get', 'repcap_impairments_set', repcap.Impairments.Ix1)

	def repcap_impairments_set(self, enum_value: repcap.Impairments) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Impairments.Default
		Default value after init: Impairments.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_impairments_get(self) -> repcap.Impairments:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Nimpairments_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def ipAddress(self):
		"""ipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipAddress'):
			from .Nimpairments_.IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._base)
		return self._ipAddress

	@property
	def prange(self):
		"""prange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prange'):
			from .Nimpairments_.Prange import Prange
			self._prange = Prange(self._core, self._base)
		return self._prange

	@property
	def plRate(self):
		"""plRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plRate'):
			from .Nimpairments_.PlRate import PlRate
			self._plRate = PlRate(self._core, self._base)
		return self._plRate

	@property
	def jitter(self):
		"""jitter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jitter'):
			from .Nimpairments_.Jitter import Jitter
			self._jitter = Jitter(self._core, self._base)
		return self._jitter

	@property
	def jitterDistribution(self):
		"""jitterDistribution commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jitterDistribution'):
			from .Nimpairments_.JitterDistribution import JitterDistribution
			self._jitterDistribution = JitterDistribution(self._core, self._base)
		return self._jitterDistribution

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Nimpairments_.Delay import Delay
			self._delay = Delay(self._core, self._base)
		return self._delay

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Nimpairments_.Crate import Crate
			self._crate = Crate(self._core, self._base)
		return self._crate

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drate'):
			from .Nimpairments_.Drate import Drate
			self._drate = Drate(self._core, self._base)
		return self._drate

	@property
	def rrate(self):
		"""rrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrate'):
			from .Nimpairments_.Rrate import Rrate
			self._rrate = Rrate(self._core, self._base)
		return self._rrate

	def clone(self) -> 'Nimpairments':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nimpairments(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
