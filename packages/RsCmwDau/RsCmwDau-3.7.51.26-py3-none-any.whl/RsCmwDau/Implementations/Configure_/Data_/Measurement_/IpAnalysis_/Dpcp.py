from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcp:
	"""Dpcp commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpcp", core, parent)

	@property
	def dpLayer(self):
		"""dpLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpLayer'):
			from .Dpcp_.DpLayer import DpLayer
			self._dpLayer = DpLayer(self._core, self._base)
		return self._dpLayer

	@property
	def dpApplic(self):
		"""dpApplic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpApplic'):
			from .Dpcp_.DpApplic import DpApplic
			self._dpApplic = DpApplic(self._core, self._base)
		return self._dpApplic

	def clone(self) -> 'Dpcp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpcp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
