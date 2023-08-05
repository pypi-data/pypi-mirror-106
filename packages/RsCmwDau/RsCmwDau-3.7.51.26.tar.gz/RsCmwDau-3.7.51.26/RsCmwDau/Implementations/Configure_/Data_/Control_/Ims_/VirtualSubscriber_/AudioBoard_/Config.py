from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("config", core, parent)

	# noinspection PyTypeChecker
	class ConfigStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Instance: enums.AudioInstance: INST1 | INST2 Audio software instance 1 or 2
			- Dtx_Enable: bool: OFF | ON Enable comfort noise in the downlink for AMR codecs
			- Force_Mode_Nb: enums.ForceModeNb: ZERO | ONE | TWO | THRE | FOUR | FIVE | SIX | SEVN | FREE Index of the codec rate to be used if the AMR narrowband codec is active FREE means that no specific codec rate is forced
			- Force_Mode_Wb: enums.ForceModeWb: ZERO | ONE | TWO | THRE | FOUR | FIVE | SIX | SEVN | EIGH | FREE Index of the codec rate to be used if the AMR wideband codec is active FREE means that no specific codec rate is forced
			- Force_Mode_Evs: enums.ForceModeEvs: SDP | P28 | P72 | P80 | P96 | P132 | P164 | P244 | P320 | P480 | P640 | P960 | P1280 | A660 | A885 | A1265 | A1425 | A1585 | A1825 | A1985 | A2305 | A2385 Start mode and rate to be used if the EVS codec is active SDP: no specific codec rate forced P28 to P1280: EVS primary mode, 2.8 kbit/s to 128 kbit/s A660 to A2385: AMR-WB IO mode, 6.6 kbit/s to 23.85 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Instance', enums.AudioInstance),
			ArgStruct.scalar_bool('Dtx_Enable'),
			ArgStruct.scalar_enum('Force_Mode_Nb', enums.ForceModeNb),
			ArgStruct.scalar_enum('Force_Mode_Wb', enums.ForceModeWb),
			ArgStruct.scalar_enum('Force_Mode_Evs', enums.ForceModeEvs)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Instance: enums.AudioInstance = None
			self.Dtx_Enable: bool = None
			self.Force_Mode_Nb: enums.ForceModeNb = None
			self.Force_Mode_Wb: enums.ForceModeWb = None
			self.Force_Mode_Evs: enums.ForceModeEvs = None

	def set(self, structure: ConfigStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AUDioboard:CONFig \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.audioBoard.config.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the audio board.
			INTRO_CMD_HELP: A query returns only the values that are relevant for the active codec: \n
			- NB AMR: <Instance>, <DTXEnable>, <ForceModeNB>
			- WB AMR: <Instance>, <DTXEnable>, <ForceModeWB>
			- EVS: <Instance>, <ForceModeEVS> \n
			:param structure: for set value, see the help for ConfigStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AUDioboard:CONFig', structure)

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> ConfigStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AUDioboard:CONFig \n
		Snippet: value: ConfigStruct = driver.configure.data.control.ims.virtualSubscriber.audioBoard.config.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the audio board.
			INTRO_CMD_HELP: A query returns only the values that are relevant for the active codec: \n
			- NB AMR: <Instance>, <DTXEnable>, <ForceModeNB>
			- WB AMR: <Instance>, <DTXEnable>, <ForceModeWB>
			- EVS: <Instance>, <ForceModeEVS> \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: structure: for return value, see the help for ConfigStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AUDioboard:CONFig?', self.__class__.ConfigStruct())
