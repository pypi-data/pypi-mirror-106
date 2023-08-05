from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvSix:
	"""IpvSix commands group definition. 10 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvSix", core, parent)

	@property
	def prefixes(self):
		"""prefixes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prefixes'):
			from .IpvSix_.Prefixes import Prefixes
			self._prefixes = Prefixes(self._core, self._base)
		return self._prefixes

	@property
	def address(self):
		"""address commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_address'):
			from .IpvSix_.Address import Address
			self._address = Address(self._core, self._base)
		return self._address

	@property
	def static(self):
		"""static commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_static'):
			from .IpvSix_.Static import Static
			self._static = Static(self._core, self._base)
		return self._static

	@property
	def mobile(self):
		"""mobile commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mobile'):
			from .IpvSix_.Mobile import Mobile
			self._mobile = Mobile(self._core, self._base)
		return self._mobile

	@property
	def routing(self):
		"""routing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_routing'):
			from .IpvSix_.Routing import Routing
			self._routing = Routing(self._core, self._base)
		return self._routing

	@property
	def manual(self):
		"""manual commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_manual'):
			from .IpvSix_.Manual import Manual
			self._manual = Manual(self._core, self._base)
		return self._manual

	def clone(self) -> 'IpvSix':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpvSix(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
