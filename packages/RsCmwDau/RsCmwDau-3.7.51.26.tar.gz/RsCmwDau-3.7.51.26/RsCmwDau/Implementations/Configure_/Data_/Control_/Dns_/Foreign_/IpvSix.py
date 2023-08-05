from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvSix:
	"""IpvSix commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvSix", core, parent)

	@property
	def primary(self):
		"""primary commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_primary'):
			from .IpvSix_.Primary import Primary
			self._primary = Primary(self._core, self._base)
		return self._primary

	@property
	def secondary(self):
		"""secondary commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_secondary'):
			from .IpvSix_.Secondary import Secondary
			self._secondary = Secondary(self._core, self._base)
		return self._secondary

	def clone(self) -> 'IpvSix':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpvSix(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
