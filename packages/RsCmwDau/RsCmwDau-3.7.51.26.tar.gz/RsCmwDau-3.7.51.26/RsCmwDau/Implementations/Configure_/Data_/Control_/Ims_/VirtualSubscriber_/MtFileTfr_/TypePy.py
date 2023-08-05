from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("typePy", core, parent)

	def set(self, file_transfer_type: enums.FileTransferType, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTFiletfr:TYPE \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtFileTfr.typePy.set(file_transfer_type = enums.FileTransferType.FILetransfer, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the transfer type for file transfers by virtual subscriber number <v>. \n
			:param file_transfer_type: FILetransfer | LARGe File transfer or file transfer large mode
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(file_transfer_type, enums.FileTransferType)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTFiletfr:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.FileTransferType:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTFiletfr:TYPE \n
		Snippet: value: enums.FileTransferType = driver.configure.data.control.ims.virtualSubscriber.mtFileTfr.typePy.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the transfer type for file transfers by virtual subscriber number <v>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: file_transfer_type: FILetransfer | LARGe File transfer or file transfer large mode"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTFiletfr:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FileTransferType)
