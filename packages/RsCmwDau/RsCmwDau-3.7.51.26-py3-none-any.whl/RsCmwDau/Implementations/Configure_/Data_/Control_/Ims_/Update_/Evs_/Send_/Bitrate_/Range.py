from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Bitrate_Lower: enums.Bitrate: R59 | R72 | R80 | R96 | R132 | R164 | R244 | R320 | R480 | R640 | R960 | R1280 Lower end of the range, 5.9 kbit/s to 128 kbit/s
			- Bitrate_Higher: enums.Bitrate: R59 | R72 | R80 | R96 | R132 | R164 | R244 | R320 | R480 | R640 | R960 | R1280 Upper end of the range, 5.9 kbit/s to 128 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bitrate_Lower', enums.Bitrate),
			ArgStruct.scalar_enum('Bitrate_Higher', enums.Bitrate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bitrate_Lower: enums.Bitrate = None
			self.Bitrate_Higher: enums.Bitrate = None

	def set(self, structure: RangeStruct, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SEND:BITRate:RANGe \n
		Snippet: driver.configure.data.control.ims.update.evs.send.bitrate.range.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default) \n
		Selects the bit-rate range supported in the EVS primary mode in the downlink (send) direction, for a call update and
		separate configuration. \n
			:param structure: for set value, see the help for RangeStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SEND:BITRate:RANGe', structure)

	def get(self, ims=repcap.Ims.Default) -> RangeStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SEND:BITRate:RANGe \n
		Snippet: value: RangeStruct = driver.configure.data.control.ims.update.evs.send.bitrate.range.get(ims = repcap.Ims.Default) \n
		Selects the bit-rate range supported in the EVS primary mode in the downlink (send) direction, for a call update and
		separate configuration. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for RangeStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SEND:BITRate:RANGe?', self.__class__.RangeStruct())
