from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAnalysis:
	"""IpAnalysis commands group definition. 28 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAnalysis", core, parent)

	@property
	def ipcSecurity(self):
		"""ipcSecurity commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipcSecurity'):
			from .IpAnalysis_.IpcSecurity import IpcSecurity
			self._ipcSecurity = IpcSecurity(self._core, self._base)
		return self._ipcSecurity

	@property
	def tcpAnalysis(self):
		"""tcpAnalysis commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_tcpAnalysis'):
			from .IpAnalysis_.TcpAnalysis import TcpAnalysis
			self._tcpAnalysis = TcpAnalysis(self._core, self._base)
		return self._tcpAnalysis

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .IpAnalysis_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def ipConnect(self):
		"""ipConnect commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnect'):
			from .IpAnalysis_.IpConnect import IpConnect
			self._ipConnect = IpConnect(self._core, self._base)
		return self._ipConnect

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_result'):
			from .IpAnalysis_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def ftTrigger(self):
		"""ftTrigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftTrigger'):
			from .IpAnalysis_.FtTrigger import FtTrigger
			self._ftTrigger = FtTrigger(self._core, self._base)
		return self._ftTrigger

	@property
	def exportDb(self):
		"""exportDb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exportDb'):
			from .IpAnalysis_.ExportDb import ExportDb
			self._exportDb = ExportDb(self._core, self._base)
		return self._exportDb

	@property
	def dpcp(self):
		"""dpcp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpcp'):
			from .IpAnalysis_.Dpcp import Dpcp
			self._dpcp = Dpcp(self._core, self._base)
		return self._dpcp

	def clone(self) -> 'IpAnalysis':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAnalysis(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
