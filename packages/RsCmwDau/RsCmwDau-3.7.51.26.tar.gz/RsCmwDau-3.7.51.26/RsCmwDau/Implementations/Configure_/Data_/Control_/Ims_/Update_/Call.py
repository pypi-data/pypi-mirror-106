from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Call:
	"""Call commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("call", core, parent)

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Call_.Event import Event
			self._event = Event(self._core, self._base)
		return self._event

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Call_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .Call_.TypePy import TypePy
			self._typePy = TypePy(self._core, self._base)
		return self._typePy

	def clone(self) -> 'Call':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Call(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
