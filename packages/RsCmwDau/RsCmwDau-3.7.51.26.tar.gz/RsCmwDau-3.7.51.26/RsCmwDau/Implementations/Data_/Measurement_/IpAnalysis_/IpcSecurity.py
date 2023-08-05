from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpcSecurity:
	"""IpcSecurity commands group definition. 14 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipcSecurity", core, parent)

	@property
	def capplication(self):
		"""capplication commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_capplication'):
			from .IpcSecurity_.Capplication import Capplication
			self._capplication = Capplication(self._core, self._base)
		return self._capplication

	@property
	def kyword(self):
		"""kyword commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_kyword'):
			from .IpcSecurity_.Kyword import Kyword
			self._kyword = Kyword(self._core, self._base)
		return self._kyword

	@property
	def prtScan(self):
		"""prtScan commands group. 0 Sub-classes, 1 commands."""
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
