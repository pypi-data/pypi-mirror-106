from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("video", core, parent)

	@property
	def codec(self):
		"""codec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_codec'):
			from .Video_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	@property
	def attributes(self):
		"""attributes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attributes'):
			from .Video_.Attributes import Attributes
			self._attributes = Attributes(self._core, self._base)
		return self._attributes

	def clone(self) -> 'Video':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Video(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
