from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrtScan:
	"""PrtScan commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prtScan", core, parent)

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .PrtScan_.Event import Event
			self._event = Event(self._core, self._base)
		return self._event

	def get_status(self) -> bool:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:STATus \n
		Snippet: value: bool = driver.sense.data.measurement.ipAnalysis.ipcSecurity.prtScan.get_status() \n
		Queries whether a port scan is running or not. \n
			:return: scan_trigger: OFF | ON
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:STATus?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'PrtScan':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrtScan(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
