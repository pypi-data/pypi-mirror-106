from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	# noinspection PyTypeChecker
	class ExtensionStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Filter_1_On_Off: bool: OFF | ON ON: filter line 1 enabled OFF: filter line 1 disabled
			- Filter_1_Type: enums.FilterType: FLOWid | IPADd | L4PR | L7PRotocol | APPL | CTRY | SRCP | DSTP Selects the property to be checked by filter line 1. FLOWid: flow IDs IPADd: IP addresses L4PR: L4 protocol L7PRotocol: L7 protocol APPL: application CTRY: country SRCP: source port DSTP: destination port
			- Filter_1_String: str: Single string, containing all filter criteria for filter line 1. For rules, see 'Filter expressions'.
			- Filter_2_On_Off: bool: OFF | ON ON: filter line 2 enabled OFF: filter line 2 disabled
			- Filter_2_Type: enums.FilterType: FLOWid | IPADd | L4PR | L7PRotocol | APPL | CTRY | SRCP | DSTP Selects the property to be checked by filter line 2.
			- Filter_2_String: str: Single string, containing all filter criteria for filter line 2.
			- Filter_3_On_Off: bool: OFF | ON ON: filter line 3 enabled OFF: filter line 3 disabled
			- Filter_3_Type: enums.FilterType: FLOWid | IPADd | L4PR | L7PRotocol | APPL | CTRY | SRCP | DSTP Selects the property to be checked by filter line 3.
			- Filter_3_String: str: Single string, containing all filter criteria for filter line 3.
			- Filter_4_On_Off: bool: OFF | ON ON: filter line 4 enabled OFF: filter line 4 disabled
			- Filter_4_Type: enums.FilterType: FLOWid | IPADd | L4PR | L7PRotocol | APPL | CTRY | SRCP | DSTP Selects the property to be checked by filter line 4.
			- Filter_4_String: str: Single string, containing all filter criteria for filter line 4."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Filter_1_On_Off'),
			ArgStruct.scalar_enum('Filter_1_Type', enums.FilterType),
			ArgStruct.scalar_str('Filter_1_String'),
			ArgStruct.scalar_bool('Filter_2_On_Off'),
			ArgStruct.scalar_enum('Filter_2_Type', enums.FilterType),
			ArgStruct.scalar_str('Filter_2_String'),
			ArgStruct.scalar_bool('Filter_3_On_Off'),
			ArgStruct.scalar_enum('Filter_3_Type', enums.FilterType),
			ArgStruct.scalar_str('Filter_3_String'),
			ArgStruct.scalar_bool('Filter_4_On_Off'),
			ArgStruct.scalar_enum('Filter_4_Type', enums.FilterType),
			ArgStruct.scalar_str('Filter_4_String')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filter_1_On_Off: bool = None
			self.Filter_1_Type: enums.FilterType = None
			self.Filter_1_String: str = None
			self.Filter_2_On_Off: bool = None
			self.Filter_2_Type: enums.FilterType = None
			self.Filter_2_String: str = None
			self.Filter_3_On_Off: bool = None
			self.Filter_3_Type: enums.FilterType = None
			self.Filter_3_String: str = None
			self.Filter_4_On_Off: bool = None
			self.Filter_4_Type: enums.FilterType = None
			self.Filter_4_String: str = None

	def get_extension(self) -> ExtensionStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPConnect:FILTer:EXTension \n
		Snippet: value: ExtensionStruct = driver.configure.data.measurement.ipAnalysis.ipConnect.filterPy.get_extension() \n
		Configures a flow filter for IP analysis results. For views supporting the filter, the evaluated set of flows is
		restricted according to the filter settings. The filter combines all enabled filter lines via AND. You can configure up
		to four filter lines. If you skip setting parameters, the related filter lines are not modified. A query returns all
		parameters, including the optional ones. \n
			:return: structure: for return value, see the help for ExtensionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:FILTer:EXTension?', self.__class__.ExtensionStruct())

	def set_extension(self, value: ExtensionStruct) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPConnect:FILTer:EXTension \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipConnect.filterPy.set_extension(value = ExtensionStruct()) \n
		Configures a flow filter for IP analysis results. For views supporting the filter, the evaluated set of flows is
		restricted according to the filter settings. The filter combines all enabled filter lines via AND. You can configure up
		to four filter lines. If you skip setting parameters, the related filter lines are not modified. A query returns all
		parameters, including the optional ones. \n
			:param value: see the help for ExtensionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:FILTer:EXTension', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Filter_Type: enums.FilterType: No parameter help available
			- Filter_String: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Filter_Type', enums.FilterType),
			ArgStruct.scalar_str('Filter_String')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filter_Type: enums.FilterType = None
			self.Filter_String: str = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPConnect:FILTer \n
		Snippet: value: ValueStruct = driver.configure.data.measurement.ipAnalysis.ipConnect.filterPy.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:FILTer?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPConnect:FILTer \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipConnect.filterPy.set_value(value = ValueStruct()) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:FILTer', value)
