from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpAnalysis:
	"""TcpAnalysis commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcpAnalysis", core, parent)

	@property
	def flowId(self):
		"""flowId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_flowId'):
			from .TcpAnalysis_.FlowId import FlowId
			self._flowId = FlowId(self._core, self._base)
		return self._flowId

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .TcpAnalysis_.Details import Details
			self._details = Details(self._core, self._base)
		return self._details

	def clone(self) -> 'TcpAnalysis':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TcpAnalysis(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
