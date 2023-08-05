from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nat:
	"""Nat commands group definition. 6 total commands, 6 Sub-groups, 0 group commands
	Repeated Capability: Nat, default value after init: Nat.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nat", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_nat_get', 'repcap_nat_set', repcap.Nat.Ix1)

	def repcap_nat_set(self, enum_value: repcap.Nat) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Nat.Default
		Default value after init: Nat.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_nat_get(self) -> repcap.Nat:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def sbSize(self):
		"""sbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbSize'):
			from .Nat_.SbSize import SbSize
			self._sbSize = SbSize(self._core, self._base)
		return self._sbSize

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Nat_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .Nat_.Protocol import Protocol
			self._protocol = Protocol(self._core, self._base)
		return self._protocol

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Nat_.Port import Port
			self._port = Port(self._core, self._base)
		return self._port

	@property
	def pconnection(self):
		"""pconnection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pconnection'):
			from .Nat_.Pconnection import Pconnection
			self._pconnection = Pconnection(self._core, self._base)
		return self._pconnection

	@property
	def bitrate(self):
		"""bitrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitrate'):
			from .Nat_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	def clone(self) -> 'Nat':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nat(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
