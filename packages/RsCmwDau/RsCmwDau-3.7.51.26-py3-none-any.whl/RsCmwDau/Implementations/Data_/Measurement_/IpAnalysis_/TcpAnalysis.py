from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpAnalysis:
	"""TcpAnalysis commands group definition. 5 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcpAnalysis", core, parent)

	@property
	def rtt(self):
		"""rtt commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtt'):
			from .TcpAnalysis_.Rtt import Rtt
			self._rtt = Rtt(self._core, self._base)
		return self._rtt

	@property
	def retransmiss(self):
		"""retransmiss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_retransmiss'):
			from .TcpAnalysis_.Retransmiss import Retransmiss
			self._retransmiss = Retransmiss(self._core, self._base)
		return self._retransmiss

	@property
	def wsize(self):
		"""wsize commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wsize'):
			from .TcpAnalysis_.Wsize import Wsize
			self._wsize = Wsize(self._core, self._base)
		return self._wsize

	@property
	def throughput(self):
		"""throughput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_throughput'):
			from .TcpAnalysis_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .TcpAnalysis_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def clone(self) -> 'TcpAnalysis':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TcpAnalysis(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
