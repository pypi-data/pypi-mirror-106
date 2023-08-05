from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subscriber:
	"""Subscriber commands group definition. 16 total commands, 9 Sub-groups, 1 group commands
	Repeated Capability: Subscriber, default value after init: Subscriber.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("subscriber", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_subscriber_get', 'repcap_subscriber_set', repcap.Subscriber.Nr1)

	def repcap_subscriber_set(self, enum_value: repcap.Subscriber) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Subscriber.Default
		Default value after init: Subscriber.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_subscriber_get(self) -> repcap.Subscriber:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def impu(self):
		"""impu commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_impu'):
			from .Subscriber_.Impu import Impu
			self._impu = Impu(self._core, self._base)
		return self._impu

	@property
	def chatQci(self):
		"""chatQci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chatQci'):
			from .Subscriber_.ChatQci import ChatQci
			self._chatQci = ChatQci(self._core, self._base)
		return self._chatQci

	@property
	def privateId(self):
		"""privateId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_privateId'):
			from .Subscriber_.PrivateId import PrivateId
			self._privateId = PrivateId(self._core, self._base)
		return self._privateId

	@property
	def authentication(self):
		"""authentication commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_authentication'):
			from .Subscriber_.Authentication import Authentication
			self._authentication = Authentication(self._core, self._base)
		return self._authentication

	@property
	def resLength(self):
		"""resLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resLength'):
			from .Subscriber_.ResLength import ResLength
			self._resLength = ResLength(self._core, self._base)
		return self._resLength

	@property
	def ipSec(self):
		"""ipSec commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSec'):
			from .Subscriber_.IpSec import IpSec
			self._ipSec = IpSec(self._core, self._base)
		return self._ipSec

	@property
	def publicUserId(self):
		"""publicUserId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_publicUserId'):
			from .Subscriber_.PublicUserId import PublicUserId
			self._publicUserId = PublicUserId(self._core, self._base)
		return self._publicUserId

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Subscriber_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .Subscriber_.Create import Create
			self._create = Create(self._core, self._base)
		return self._create

	def delete(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:DELete \n
		Snippet: driver.configure.data.control.ims.subscriber.delete(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Deletes the subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:DELete')

	def delete_with_opc(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:DELete \n
		Snippet: driver.configure.data.control.ims.subscriber.delete_with_opc(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Deletes the subscriber profile number <s>. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:DELete')

	def clone(self) -> 'Subscriber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subscriber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
