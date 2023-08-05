from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpReplay:
	"""IpReplay commands group definition. 6 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipReplay", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .IpReplay_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def fileList(self):
		"""fileList commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fileList'):
			from .IpReplay_.FileList import FileList
			self._fileList = FileList(self._core, self._base)
		return self._fileList

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:IPReplay')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:IPReplay')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:IPReplay')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:IPReplay')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:IPReplay')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPReplay \n
		Snippet: driver.data.measurement.ipReplay.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:IPReplay')

	def clone(self) -> 'IpReplay':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpReplay(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
