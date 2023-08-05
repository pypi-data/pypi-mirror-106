from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcSecurity:
	"""IpcSecurity commands group definition. 4 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipcSecurity", core, parent)

	@property
	def kyword(self):
		"""kyword commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_kyword'):
			from .IpcSecurity_.Kyword import Kyword
			self._kyword = Kyword(self._core, self._base)
		return self._kyword

	@property
	def prtScan(self):
		"""prtScan commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtScan'):
			from .IpcSecurity_.PrtScan import PrtScan
			self._prtScan = PrtScan(self._core, self._base)
		return self._prtScan

	def get_applications(self) -> List[str]:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:APPLications \n
		Snippet: value: List[str] = driver.sense.data.measurement.ipAnalysis.ipcSecurity.get_applications() \n
		Queries the list of applications resulting from the IP packet analysis on the application layer. \n
			:return: applications: Comma-separated list of strings, one string per application
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:APPLications?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'IpcSecurity':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpcSecurity(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
