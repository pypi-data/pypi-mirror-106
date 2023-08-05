from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtFileTfr:
	"""MtFileTfr commands group definition. 5 total commands, 4 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mtFileTfr", core, parent)

	@property
	def chunkSize(self):
		"""chunkSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chunkSize'):
			from .MtFileTfr_.ChunkSize import ChunkSize
			self._chunkSize = ChunkSize(self._core, self._base)
		return self._chunkSize

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .MtFileTfr_.File import File
			self._file = File(self._core, self._base)
		return self._file

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .MtFileTfr_.TypePy import TypePy
			self._typePy = TypePy(self._core, self._base)
		return self._typePy

	@property
	def destination(self):
		"""destination commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_destination'):
			from .MtFileTfr_.Destination import Destination
			self._destination = Destination(self._core, self._base)
		return self._destination

	def send(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTFiletfr:SEND \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtFileTfr.send(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Initiates a file transfer from virtual subscriber number <v> to the DUT. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTFiletfr:SEND')

	def send_with_opc(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTFiletfr:SEND \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtFileTfr.send_with_opc(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Initiates a file transfer from virtual subscriber number <v> to the DUT. \n
		Same as send, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTFiletfr:SEND')

	def clone(self) -> 'MtFileTfr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MtFileTfr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
