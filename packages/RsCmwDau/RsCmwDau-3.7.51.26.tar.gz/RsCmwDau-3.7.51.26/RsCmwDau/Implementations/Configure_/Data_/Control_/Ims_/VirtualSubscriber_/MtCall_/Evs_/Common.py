from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Common:
	"""Common commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("common", core, parent)

	@property
	def bitrate(self):
		"""bitrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bitrate'):
			from .Common_.Bitrate import Bitrate
			self._bitrate = Bitrate(self._core, self._base)
		return self._bitrate

	def clone(self) -> 'Common':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Common(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
