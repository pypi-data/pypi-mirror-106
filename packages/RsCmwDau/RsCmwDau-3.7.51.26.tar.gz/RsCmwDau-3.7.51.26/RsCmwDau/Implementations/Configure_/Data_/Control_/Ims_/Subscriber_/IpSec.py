from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpSec:
	"""IpSec commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipSec", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .IpSec_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def algorithm(self):
		"""algorithm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_algorithm'):
			from .IpSec_.Algorithm import Algorithm
			self._algorithm = Algorithm(self._core, self._base)
		return self._algorithm

	def clone(self) -> 'IpSec':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpSec(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
