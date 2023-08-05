from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Forward:
	"""Forward commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("forward", core, parent)

	# noinspection PyTypeChecker
	class ForwardStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Ip_Address: str: IPv4 or IPv6 address of the media endpoint as string
			- Port: int: Port for RTP packet forwarding
			- Cmd_Port: int: Port for the command interface to the media endpoint
			- Amr_Align: enums.AlignMode: OCTetaligned | BANDwidtheff AMR alignment mode used by the media endpoint OCTetaligned: octet-aligned BANDwidtheff: bandwidth-efficient"""
		__meta_args_list = [
			ArgStruct.scalar_str('Ip_Address'),
			ArgStruct.scalar_int('Port'),
			ArgStruct.scalar_int('Cmd_Port'),
			ArgStruct.scalar_enum('Amr_Align', enums.AlignMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ip_Address: str = None
			self.Port: int = None
			self.Cmd_Port: int = None
			self.Amr_Align: enums.AlignMode = None

	def set(self, structure: ForwardStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:FORWard \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.forward.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures an external media endpoint. \n
			:param structure: for set value, see the help for ForwardStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:FORWard', structure)

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> ForwardStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:FORWard \n
		Snippet: value: ForwardStruct = driver.configure.data.control.ims.virtualSubscriber.forward.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures an external media endpoint. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: structure: for return value, see the help for ForwardStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:FORWard?', self.__class__.ForwardStruct())
