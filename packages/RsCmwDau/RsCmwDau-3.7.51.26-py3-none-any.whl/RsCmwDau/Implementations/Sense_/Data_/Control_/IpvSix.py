from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvSix:
	"""IpvSix commands group definition. 6 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvSix", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .IpvSix_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def automatic(self):
		"""automatic commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_automatic'):
			from .IpvSix_.Automatic import Automatic
			self._automatic = Automatic(self._core, self._base)
		return self._automatic

	@property
	def static(self):
		"""static commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_static'):
			from .IpvSix_.Static import Static
			self._static = Static(self._core, self._base)
		return self._static

	@property
	def dhcp(self):
		"""dhcp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dhcp'):
			from .IpvSix_.Dhcp import Dhcp
			self._dhcp = Dhcp(self._core, self._base)
		return self._dhcp

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
