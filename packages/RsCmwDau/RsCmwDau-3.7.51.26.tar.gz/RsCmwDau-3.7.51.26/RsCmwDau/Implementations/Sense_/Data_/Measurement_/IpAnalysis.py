from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAnalysis:
	"""IpAnalysis commands group definition. 14 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAnalysis", core, parent)

	@property
	def ipcSecurity(self):
		"""ipcSecurity commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipcSecurity'):
			from .IpAnalysis_.IpcSecurity import IpcSecurity
			self._ipcSecurity = IpcSecurity(self._core, self._base)
		return self._ipcSecurity

	@property
	def export(self):
		"""export commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_export'):
			from .IpAnalysis_.Export import Export
			self._export = Export(self._core, self._base)
		return self._export

	@property
	def ipConnect(self):
		"""ipConnect commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipConnect'):
			from .IpAnalysis_.IpConnect import IpConnect
			self._ipConnect = IpConnect(self._core, self._base)
		return self._ipConnect

	@property
	def tcpAnalysis(self):
		"""tcpAnalysis commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcpAnalysis'):
			from .IpAnalysis_.TcpAnalysis import TcpAnalysis
			self._tcpAnalysis = TcpAnalysis(self._core, self._base)
		return self._tcpAnalysis

	@property
	def voIms(self):
		"""voIms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_voIms'):
			from .IpAnalysis_.VoIms import VoIms
			self._voIms = VoIms(self._core, self._base)
		return self._voIms

	def clone(self) -> 'IpAnalysis':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAnalysis(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
