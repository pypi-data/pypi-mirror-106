from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 17 total commands, 17 Sub-groups, 0 group commands
	Repeated Capability: Fltr, default value after init: Fltr.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_fltr_get', 'repcap_fltr_set', repcap.Fltr.Ix1)

	def repcap_fltr_set(self, enum_value: repcap.Fltr) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Fltr.Default
		Default value after init: Fltr.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_fltr_get(self) -> repcap.Fltr:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .FilterPy_.Remove import Remove
			self._remove = Remove(self._core, self._base)
		return self._remove

	@property
	def hopLimit(self):
		"""hopLimit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopLimit'):
			from .FilterPy_.HopLimit import HopLimit
			self._hopLimit = HopLimit(self._core, self._base)
		return self._hopLimit

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .FilterPy_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	@property
	def bitrate(self):
		"""bitrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitrate'):
			from .FilterPy_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	@property
	def srcpRange(self):
		"""srcpRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srcpRange'):
			from .FilterPy_.SrcpRange import SrcpRange
			self._srcpRange = SrcpRange(self._core, self._base)
		return self._srcpRange

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .FilterPy_.Protocol import Protocol
			self._protocol = Protocol(self._core, self._base)
		return self._protocol

	@property
	def tcpAckPrio(self):
		"""tcpAckPrio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcpAckPrio'):
			from .FilterPy_.TcpAckPrio import TcpAckPrio
			self._tcpAckPrio = TcpAckPrio(self._core, self._base)
		return self._tcpAckPrio

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .FilterPy_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def ipAddress(self):
		"""ipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipAddress'):
			from .FilterPy_.IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._base)
		return self._ipAddress

	@property
	def prange(self):
		"""prange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prange'):
			from .FilterPy_.Prange import Prange
			self._prange = Prange(self._core, self._base)
		return self._prange

	@property
	def plRate(self):
		"""plRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plRate'):
			from .FilterPy_.PlRate import PlRate
			self._plRate = PlRate(self._core, self._base)
		return self._plRate

	@property
	def jitter(self):
		"""jitter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jitter'):
			from .FilterPy_.Jitter import Jitter
			self._jitter = Jitter(self._core, self._base)
		return self._jitter

	@property
	def jitterDistribution(self):
		"""jitterDistribution commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jitterDistribution'):
			from .FilterPy_.JitterDistribution import JitterDistribution
			self._jitterDistribution = JitterDistribution(self._core, self._base)
		return self._jitterDistribution

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .FilterPy_.Delay import Delay
			self._delay = Delay(self._core, self._base)
		return self._delay

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .FilterPy_.Crate import Crate
			self._crate = Crate(self._core, self._base)
		return self._crate

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drate'):
			from .FilterPy_.Drate import Drate
			self._drate = Drate(self._core, self._base)
		return self._drate

	@property
	def rrate(self):
		"""rrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrate'):
			from .FilterPy_.Rrate import Rrate
			self._rrate = Rrate(self._core, self._base)
		return self._rrate

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
