from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcSecurity:
	"""IpcSecurity commands group definition. 10 total commands, 2 Sub-groups, 0 group commands"""

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
		"""prtScan commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_prtScan'):
			from .IpcSecurity_.PrtScan import PrtScan
			self._prtScan = PrtScan(self._core, self._base)
		return self._prtScan

	def clone(self) -> 'IpcSecurity':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpcSecurity(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
