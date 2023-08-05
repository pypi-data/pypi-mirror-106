from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 29 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Throughput_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Throughput_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def overall(self):
		"""overall commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_overall'):
			from .Throughput_.Overall import Overall
			self._overall = Overall(self._core, self._base)
		return self._overall

	@property
	def ran(self):
		"""ran commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ran'):
			from .Throughput_.Ran import Ran
			self._ran = Ran(self._core, self._base)
		return self._ran

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:THRoughput')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:THRoughput')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:THRoughput')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:THRoughput')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:THRoughput')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:THRoughput \n
		Snippet: driver.data.measurement.throughput.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:THRoughput')

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
