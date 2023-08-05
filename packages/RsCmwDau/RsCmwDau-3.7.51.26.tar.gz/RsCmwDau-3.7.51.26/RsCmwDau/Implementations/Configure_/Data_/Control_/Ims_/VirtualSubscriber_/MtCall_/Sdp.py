from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sdp:
	"""Sdp commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sdp", core, parent)

	# noinspection PyTypeChecker
	class SdpStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Sdp_Enable: bool: No parameter help available
			- Sdp_File_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Sdp_Enable'),
			ArgStruct.scalar_str('Sdp_File_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sdp_Enable: bool = None
			self.Sdp_File_Name: str = None

	def set(self, structure: SdpStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTCall:SDP \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtCall.sdp.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param structure: for set value, see the help for SdpStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTCall:SDP', structure)

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> SdpStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTCall:SDP \n
		Snippet: value: SdpStruct = driver.configure.data.control.ims.virtualSubscriber.mtCall.sdp.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: structure: for return value, see the help for SdpStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTCall:SDP?', self.__class__.SdpStruct())
