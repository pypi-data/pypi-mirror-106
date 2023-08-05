from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.StructBase import StructBase
from ...........Internal.ArgStruct import ArgStruct
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Bitrate_Lower: enums.Bitrate: No parameter help available
			- Bitrate_Higher: enums.Bitrate: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bitrate_Lower', enums.Bitrate),
			ArgStruct.scalar_enum('Bitrate_Higher', enums.Bitrate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bitrate_Lower: enums.Bitrate = None
			self.Bitrate_Higher: enums.Bitrate = None

	def set(self, structure: RangeStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTCall:EVS:COMMon:BITRate:RANGe \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtCall.evs.common.bitrate.range.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param structure: for set value, see the help for RangeStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTCall:EVS:COMMon:BITRate:RANGe', structure)

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> RangeStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTCall:EVS:COMMon:BITRate:RANGe \n
		Snippet: value: RangeStruct = driver.configure.data.control.ims.virtualSubscriber.mtCall.evs.common.bitrate.range.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: structure: for return value, see the help for RangeStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTCall:EVS:COMMon:BITRate:RANGe?', self.__class__.RangeStruct())
