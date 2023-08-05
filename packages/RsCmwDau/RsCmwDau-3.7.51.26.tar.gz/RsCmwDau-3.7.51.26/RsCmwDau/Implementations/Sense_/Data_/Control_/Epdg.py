from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Epdg:
	"""Epdg commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("epdg", core, parent)

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Epdg_.Event import Event
			self._event = Event(self._core, self._base)
		return self._event

	@property
	def connections(self):
		"""connections commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connections'):
			from .Epdg_.Connections import Connections
			self._connections = Connections(self._core, self._base)
		return self._connections

	def clone(self) -> 'Epdg':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Epdg(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
