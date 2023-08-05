from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmRwb:
	"""AmRwb commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("amRwb", core, parent)

	@property
	def codec(self):
		"""codec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_codec'):
			from .AmRwb_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	def clone(self) -> 'AmRwb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmRwb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
