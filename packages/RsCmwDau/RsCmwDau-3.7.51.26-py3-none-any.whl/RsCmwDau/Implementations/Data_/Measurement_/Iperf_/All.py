from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Server_Result_Counter: List[int]: No parameter help available
			- Client_Result_Counter: List[int]: No parameter help available
			- Up_Bandwidth: List[float]: No parameter help available
			- Pack_Err_Rate: List[float]: Percentage of lost packets Range: 0 % to 100 %, Unit: %
			- Down_Bandwidth: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Server_Result_Counter', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Client_Result_Counter', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Up_Bandwidth', DataType.FloatList, None, False, True, 1),
			ArgStruct('Pack_Err_Rate', DataType.FloatList, None, False, True, 1),
			ArgStruct('Down_Bandwidth', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Server_Result_Counter: List[int] = None
			self.Client_Result_Counter: List[int] = None
			self.Up_Bandwidth: List[float] = None
			self.Pack_Err_Rate: List[float] = None
			self.Down_Bandwidth: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPERf:ALL \n
		Snippet: value: FetchStruct = driver.data.measurement.iperf.all.fetch() \n
		Queries all client and server results of the iperf measurement. For each server/client instance five results are returned,
		from instance 1 to instance 8: <Reliability>, {<ServerCounter>, <ClientCounter>, <ServerBW>, <PackErrRate>,
		<ClientBW>}instance 1, {...}instance 2, ..., {...}instance 8 Iperf results are often queried within a loop, to monitor
		the results over some time. Iperf delivers new results once per second. If your loop is faster, several consecutive
		queries deliver the same results. Use the <ServerCounter> and <ClientCounter> to identify redundant results and discard
		them. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPERf:ALL?', self.__class__.FetchStruct())
