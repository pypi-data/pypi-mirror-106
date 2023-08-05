from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAnalysis:
	"""IpAnalysis commands group definition. 33 total commands, 7 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAnalysis", core, parent)

	@property
	def ipcSecurity(self):
		"""ipcSecurity commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipcSecurity'):
			from .IpAnalysis_.IpcSecurity import IpcSecurity
			self._ipcSecurity = IpcSecurity(self._core, self._base)
		return self._ipcSecurity

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .IpAnalysis_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def dpcp(self):
		"""dpcp commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpcp'):
			from .IpAnalysis_.Dpcp import Dpcp
			self._dpcp = Dpcp(self._core, self._base)
		return self._dpcp

	@property
	def ipConnect(self):
		"""ipConnect commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnect'):
			from .IpAnalysis_.IpConnect import IpConnect
			self._ipConnect = IpConnect(self._core, self._base)
		return self._ipConnect

	@property
	def tcpAnalysis(self):
		"""tcpAnalysis commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcpAnalysis'):
			from .IpAnalysis_.TcpAnalysis import TcpAnalysis
			self._tcpAnalysis = TcpAnalysis(self._core, self._base)
		return self._tcpAnalysis

	@property
	def ftTrigger(self):
		"""ftTrigger commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftTrigger'):
			from .IpAnalysis_.FtTrigger import FtTrigger
			self._ftTrigger = FtTrigger(self._core, self._base)
		return self._ftTrigger

	@property
	def voIms(self):
		"""voIms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_voIms'):
			from .IpAnalysis_.VoIms import VoIms
			self._voIms = VoIms(self._core, self._base)
		return self._voIms

	def initiate(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:DATA:MEASurement<MeasInstance>:IPANalysis')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:DATA:MEASurement<MeasInstance>:IPANalysis')

	def stop(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:DATA:MEASurement<MeasInstance>:IPANalysis')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:DATA:MEASurement<MeasInstance>:IPANalysis')

	def abort(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:DATA:MEASurement<MeasInstance>:IPANalysis')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:DATA:MEASurement<Instance>:IPANalysis \n
		Snippet: driver.data.measurement.ipAnalysis.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:DATA:MEASurement<MeasInstance>:IPANalysis')

	def clone(self) -> 'IpAnalysis':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAnalysis(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
