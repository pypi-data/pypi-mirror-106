from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Server:
	"""Server commands group definition. 5 total commands, 5 Sub-groups, 0 group commands
	Repeated Capability: Server, default value after init: Server.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("server", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_server_get', 'repcap_server_set', repcap.Server.Ix1)

	def repcap_server_set(self, enum_value: repcap.Server) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Server.Default
		Default value after init: Server.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_server_get(self) -> repcap.Server:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def sbSize(self):
		"""sbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbSize'):
			from .Server_.SbSize import SbSize
			self._sbSize = SbSize(self._core, self._base)
		return self._sbSize

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Server_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def protocol(self):
		"""protocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protocol'):
			from .Server_.Protocol import Protocol
			self._protocol = Protocol(self._core, self._base)
		return self._protocol

	@property
	def wsize(self):
		"""wsize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wsize'):
			from .Server_.Wsize import Wsize
			self._wsize = Wsize(self._core, self._base)
		return self._wsize

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Server_.Port import Port
			self._port = Port(self._core, self._base)
		return self._port

	def clone(self) -> 'Server':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Server(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
