from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Features:
	"""Features commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("features", core, parent)

	@property
	def fileTransfer(self):
		"""fileTransfer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fileTransfer'):
			from .Features_.FileTransfer import FileTransfer
			self._fileTransfer = FileTransfer(self._core, self._base)
		return self._fileTransfer

	@property
	def sessionMode(self):
		"""sessionMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sessionMode'):
			from .Features_.SessionMode import SessionMode
			self._sessionMode = SessionMode(self._core, self._base)
		return self._sessionMode

	@property
	def standalone(self):
		"""standalone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standalone'):
			from .Features_.Standalone import Standalone
			self._standalone = Standalone(self._core, self._base)
		return self._standalone

	@property
	def video(self):
		"""video commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_video'):
			from .Features_.Video import Video
			self._video = Video(self._core, self._base)
		return self._video

	def clone(self) -> 'Features':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Features(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
