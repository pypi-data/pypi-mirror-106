from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("event", core, parent)

	# noinspection PyTypeChecker
	class LogStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Timestamps: List[str]: Timestamp of the entry as string in the format 'hh:mm:ss'
			- Type_Py: List[enums.InfoType]: NONE | INFO | WARNing | ERRor Category of the entry NONE means that no category is assigned. If no entry at all is available, the answer is '',NONE,''.
			- Info: List[str]: Text string describing the event"""
		__meta_args_list = [
			ArgStruct('Timestamps', DataType.StringList, None, False, True, 1),
			ArgStruct('Type_Py', DataType.EnumList, enums.InfoType, False, True, 1),
			ArgStruct('Info', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamps: List[str] = None
			self.Type_Py: List[enums.InfoType] = None
			self.Info: List[str] = None

	def get_log(self) -> LogStruct:
		"""SCPI: SENSe:DATA:CONTrol:EPDG:EVENt:LOG \n
		Snippet: value: LogStruct = driver.sense.data.control.epdg.event.get_log() \n
		Queries all entries of the event log. For each entry, three parameters are returned, from oldest to latest entry:
		{<Timestamps>, <Type>, <Info>}entry 1, {<Timestamps>, <Type>, <Info>}entry 2, ... \n
			:return: structure: for return value, see the help for LogStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:EPDG:EVENt:LOG?', self.__class__.LogStruct())
