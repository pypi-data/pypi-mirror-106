from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adelay:
	"""Adelay commands group definition. 25 total commands, 7 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("adelay", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Adelay_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def ulink(self):
		"""ulink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulink'):
			from .Adelay_.Ulink import Ulink
			self._ulink = Ulink(self._core, self._base)
		return self._ulink

	@property
	def dlink(self):
		"""dlink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlink'):
			from .Adelay_.Dlink import Dlink
			self._dlink = Dlink(self._core, self._base)
		return self._dlink

	@property
	def loopback(self):
		"""loopback commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_loopback'):
			from .Adelay_.Loopback import Loopback
			self._loopback = Loopback(self._core, self._base)
		return self._loopback

	@property
	def tauLink(self):
		"""tauLink commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tauLink'):
			from .Adelay_.TauLink import TauLink
			self._tauLink = TauLink(self._core, self._base)
		return self._tauLink

	@property
	def taLoopback(self):
		"""taLoopback commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_taLoopback'):
			from .Adelay_.TaLoopback import TaLoopback
			self._taLoopback = TaLoopback(self._core, self._base)
		return self._taLoopback

	@property
	def trace(self):
		"""trace commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Adelay_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:ADELay')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:ADELay')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:ADELay')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:ADELay')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:ADELay')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:ADELay \n
		Snippet: driver.data.measurement.adelay.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:ADELay')

	def clone(self) -> 'Adelay':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Adelay(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
