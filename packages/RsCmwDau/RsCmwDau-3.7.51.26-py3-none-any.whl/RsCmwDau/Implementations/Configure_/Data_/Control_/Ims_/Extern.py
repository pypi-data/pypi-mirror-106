from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extern:
	"""Extern commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extern", core, parent)

	@property
	def pcscf(self):
		"""pcscf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcscf'):
			from .Extern_.Pcscf import Pcscf
			self._pcscf = Pcscf(self._core, self._base)
		return self._pcscf

	def clone(self) -> 'Extern':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Extern(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
