from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Client:
	"""Client commands group definition. 9 total commands, 9 Sub-groups, 0 group commands
	Repeated Capability: Client, default value after init: Client.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("client", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_client_get', 'repcap_client_set', repcap.Client.Ix1)

	def repcap_client_set(self, enum_value: repcap.Client) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Client.Default
		Default value after init: Client.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_client_get(self) -> repcap.Client:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def sbSize(self):
		"""sbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbSize'):
			from .Client_.SbSize import SbSize
			self._sbSize = SbSize(self._core, self._base)
		return self._sbSize

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Client_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .Client_.Protocol import Protocol
			self._protocol = Protocol(self._core, self._base)
		return self._protocol

	@property
	def wsize(self):
		"""wsize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wsize'):
			from .Client_.Wsize import Wsize
			self._wsize = Wsize(self._core, self._base)
		return self._wsize

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Client_.Port import Port
			self._port = Port(self._core, self._base)
		return self._port

	@property
	def ipAddress(self):
		"""ipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipAddress'):
			from .Client_.IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._base)
		return self._ipAddress

	@property
	def pconnection(self):
		"""pconnection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pconnection'):
			from .Client_.Pconnection import Pconnection
			self._pconnection = Pconnection(self._core, self._base)
		return self._pconnection

	@property
	def bitrate(self):
		"""bitrate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitrate'):
			from .Client_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	@property
	def reverse(self):
		"""reverse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reverse'):
			from .Client_.Reverse import Reverse
			self._reverse = Reverse(self._core, self._base)
		return self._reverse

	def clone(self) -> 'Client':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Client(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
