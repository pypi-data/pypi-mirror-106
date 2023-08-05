from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Algorithm:
	"""Algorithm commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("algorithm", core, parent)

	@property
	def integrity(self):
		"""integrity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_integrity'):
			from .Algorithm_.Integrity import Integrity
			self._integrity = Integrity(self._core, self._base)
		return self._integrity

	@property
	def encryption(self):
		"""encryption commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_encryption'):
			from .Algorithm_.Encryption import Encryption
			self._encryption = Encryption(self._core, self._base)
		return self._encryption

	def clone(self) -> 'Algorithm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Algorithm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
