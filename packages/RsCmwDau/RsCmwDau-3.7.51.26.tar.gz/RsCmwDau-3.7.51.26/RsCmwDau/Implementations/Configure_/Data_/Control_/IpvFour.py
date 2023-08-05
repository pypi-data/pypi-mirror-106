from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvFour:
	"""IpvFour commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvFour", core, parent)

	@property
	def address(self):
		"""address commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_address'):
			from .IpvFour_.Address import Address
			self._address = Address(self._core, self._base)
		return self._address

	@property
	def static(self):
		"""static commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_static'):
			from .IpvFour_.Static import Static
			self._static = Static(self._core, self._base)
		return self._static

	def clone(self) -> 'IpvFour':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpvFour(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
