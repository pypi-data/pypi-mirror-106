from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VirtualSubscriber:
	"""VirtualSubscriber commands group definition. 82 total commands, 24 Sub-groups, 1 group commands
	Repeated Capability: VirtualSubscriber, default value after init: VirtualSubscriber.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("virtualSubscriber", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_virtualSubscriber_get', 'repcap_virtualSubscriber_set', repcap.VirtualSubscriber.Nr1)

	def repcap_virtualSubscriber_set(self, enum_value: repcap.VirtualSubscriber) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to VirtualSubscriber.Default
		Default value after init: VirtualSubscriber.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_virtualSubscriber_get(self) -> repcap.VirtualSubscriber:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def ecConfig(self):
		"""ecConfig commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ecConfig'):
			from .VirtualSubscriber_.EcConfig import EcConfig
			self._ecConfig = EcConfig(self._core, self._base)
		return self._ecConfig

	@property
	def fwdCall(self):
		"""fwdCall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fwdCall'):
			from .VirtualSubscriber_.FwdCall import FwdCall
			self._fwdCall = FwdCall(self._core, self._base)
		return self._fwdCall

	@property
	def session(self):
		"""session commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_session'):
			from .VirtualSubscriber_.Session import Session
			self._session = Session(self._core, self._base)
		return self._session

	@property
	def evs(self):
		"""evs commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_evs'):
			from .VirtualSubscriber_.Evs import Evs
			self._evs = Evs(self._core, self._base)
		return self._evs

	@property
	def conference(self):
		"""conference commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_conference'):
			from .VirtualSubscriber_.Conference import Conference
			self._conference = Conference(self._core, self._base)
		return self._conference

	@property
	def supported(self):
		"""supported commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_supported'):
			from .VirtualSubscriber_.Supported import Supported
			self._supported = Supported(self._core, self._base)
		return self._supported

	@property
	def pcapFile(self):
		"""pcapFile commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcapFile'):
			from .VirtualSubscriber_.PcapFile import PcapFile
			self._pcapFile = PcapFile(self._core, self._base)
		return self._pcapFile

	@property
	def mtFileTfr(self):
		"""mtFileTfr commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtFileTfr'):
			from .VirtualSubscriber_.MtFileTfr import MtFileTfr
			self._mtFileTfr = MtFileTfr(self._core, self._base)
		return self._mtFileTfr

	@property
	def audioBoard(self):
		"""audioBoard commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_audioBoard'):
			from .VirtualSubscriber_.AudioBoard import AudioBoard
			self._audioBoard = AudioBoard(self._core, self._base)
		return self._audioBoard

	@property
	def forceMoCall(self):
		"""forceMoCall commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_forceMoCall'):
			from .VirtualSubscriber_.ForceMoCall import ForceMoCall
			self._forceMoCall = ForceMoCall(self._core, self._base)
		return self._forceMoCall

	@property
	def bearer(self):
		"""bearer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bearer'):
			from .VirtualSubscriber_.Bearer import Bearer
			self._bearer = Bearer(self._core, self._base)
		return self._bearer

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .VirtualSubscriber_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	@property
	def behaviour(self):
		"""behaviour commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_behaviour'):
			from .VirtualSubscriber_.Behaviour import Behaviour
			self._behaviour = Behaviour(self._core, self._base)
		return self._behaviour

	@property
	def signalingType(self):
		"""signalingType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signalingType'):
			from .VirtualSubscriber_.SignalingType import SignalingType
			self._signalingType = SignalingType(self._core, self._base)
		return self._signalingType

	@property
	def adCodec(self):
		"""adCodec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adCodec'):
			from .VirtualSubscriber_.AdCodec import AdCodec
			self._adCodec = AdCodec(self._core, self._base)
		return self._adCodec

	@property
	def amr(self):
		"""amr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_amr'):
			from .VirtualSubscriber_.Amr import Amr
			self._amr = Amr(self._core, self._base)
		return self._amr

	@property
	def video(self):
		"""video commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_video'):
			from .VirtualSubscriber_.Video import Video
			self._video = Video(self._core, self._base)
		return self._video

	@property
	def mediaEndpoint(self):
		"""mediaEndpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mediaEndpoint'):
			from .VirtualSubscriber_.MediaEndpoint import MediaEndpoint
			self._mediaEndpoint = MediaEndpoint(self._core, self._base)
		return self._mediaEndpoint

	@property
	def forward(self):
		"""forward commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_forward'):
			from .VirtualSubscriber_.Forward import Forward
			self._forward = Forward(self._core, self._base)
		return self._forward

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .VirtualSubscriber_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .VirtualSubscriber_.Create import Create
			self._create = Create(self._core, self._base)
		return self._create

	@property
	def mtSms(self):
		"""mtSms commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtSms'):
			from .VirtualSubscriber_.MtSms import MtSms
			self._mtSms = MtSms(self._core, self._base)
		return self._mtSms

	@property
	def mtCall(self):
		"""mtCall commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtCall'):
			from .VirtualSubscriber_.MtCall import MtCall
			self._mtCall = MtCall(self._core, self._base)
		return self._mtCall

	@property
	def max(self):
		"""max commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_max'):
			from .VirtualSubscriber_.Max import Max
			self._max = Max(self._core, self._base)
		return self._max

	def delete(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:DELete \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.delete(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Deletes the virtual subscriber profile number <v>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:DELete')

	def delete_with_opc(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:DELete \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.delete_with_opc(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Deletes the virtual subscriber profile number <v>. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:DELete')

	def clone(self) -> 'VirtualSubscriber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VirtualSubscriber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
