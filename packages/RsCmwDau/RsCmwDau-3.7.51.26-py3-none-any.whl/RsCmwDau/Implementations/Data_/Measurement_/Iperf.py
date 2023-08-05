from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iperf:
	"""Iperf commands group definition. 13 total commands, 5 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iperf", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Iperf_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def packetLoss(self):
		"""packetLoss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_packetLoss'):
			from .Iperf_.PacketLoss import PacketLoss
			self._packetLoss = PacketLoss(self._core, self._base)
		return self._packetLoss

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .Iperf_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def server(self):
		"""server commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_server'):
			from .Iperf_.Server import Server
			self._server = Server(self._core, self._base)
		return self._server

	@property
	def client(self):
		"""client commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_client'):
			from .Iperf_.Client import Client
			self._client = Client(self._core, self._base)
		return self._client

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:IPERf')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:IPERf')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:IPERf')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:IPERf')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:IPERf')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPERf \n
		Snippet: driver.data.measurement.iperf.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:IPERf')

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Up_Bandwidth: float: No parameter help available
			- Down_Bandwidth: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Up_Bandwidth'),
			ArgStruct.scalar_float('Down_Bandwidth')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Up_Bandwidth: float = None
			self.Down_Bandwidth: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:DATA:MEASurement<Instance>:IPERf \n
		Snippet: value: ResultData = driver.data.measurement.iperf.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:DATA:MEASurement<MeasInstance>:IPERf?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPERf \n
		Snippet: value: ResultData = driver.data.measurement.iperf.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPERf?', self.__class__.ResultData())

	def clone(self) -> 'Iperf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iperf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
