from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("start", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Flow_Id: List[str]: Flow ID of the opened connection as string
			- Time_Elapsed: List[float]: X-axis value of the 'open' event"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Flow_Id', DataType.StringList, None, False, True, 1),
			ArgStruct('Time_Elapsed', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Flow_Id: List[str] = None
			self.Time_Elapsed: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:FTTRigger:TRIGger:STARt \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ftTrigger.trigger.start.fetch() \n
		Queries the event trigger trace for 'open' events. After the reliability indicator, two values are returned per 'open'
		event: <Reliability>, {<FlowID>, <TimeElapsed>}event 1, {<FlowID>, <TimeElapsed>}event 2, ... The trace is returned from
		right to left (last to first event) . \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:FTTRigger:TRIGger:STARt?', self.__class__.FetchStruct())
