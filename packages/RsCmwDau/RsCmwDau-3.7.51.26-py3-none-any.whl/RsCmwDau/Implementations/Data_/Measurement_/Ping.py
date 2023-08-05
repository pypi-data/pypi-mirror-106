from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ping:
	"""Ping commands group definition. 9 total commands, 3 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ping", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Ping_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def overall(self):
		"""overall commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_overall'):
			from .Ping_.Overall import Overall
			self._overall = Overall(self._core, self._base)
		return self._overall

	@property
	def nrCount(self):
		"""nrCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrCount'):
			from .Ping_.NrCount import NrCount
			self._nrCount = NrCount(self._core, self._base)
		return self._nrCount

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:PING')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:PING')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:PING')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:PING')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:PING')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:PING \n
		Snippet: driver.data.measurement.ping.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:PING')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Req_No: List[int]: Request label, 0 = last request, -1 = previous request, and so on Range: -1000 to 0
			- Timestamp: List[str]: Timestamp as string in the format 'hh:mm:ss'
			- Latency: List[float]: Round-trip time for sent packets (0 s = no reply) Range: 0 s to 10 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Req_No', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Latency', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Req_No: List[int] = None
			self.Timestamp: List[str] = None
			self.Latency: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:DATA:MEASurement<Instance>:PING \n
		Snippet: value: ResultData = driver.data.measurement.ping.read() \n
		Queries the measured ping characteristics. After the reliability indicator, three results are returned for each ping
		request: <Reliability>, {<ReqNo>, <Timestamp>, <Latency>}request 1, {...}request 2, ... The number of ping requests is
		specified by method RsCmwDau.Configure.Data.Measurement.Ping.pcount. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:DATA:MEASurement<MeasInstance>:PING?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:PING \n
		Snippet: value: ResultData = driver.data.measurement.ping.fetch() \n
		Queries the measured ping characteristics. After the reliability indicator, three results are returned for each ping
		request: <Reliability>, {<ReqNo>, <Timestamp>, <Latency>}request 1, {...}request 2, ... The number of ping requests is
		specified by method RsCmwDau.Configure.Data.Measurement.Ping.pcount. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:PING?', self.__class__.ResultData())

	def clone(self) -> 'Ping':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ping(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
