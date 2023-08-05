from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 10 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def ulink(self):
		"""ulink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulink'):
			from .Trace_.Ulink import Ulink
			self._ulink = Ulink(self._core, self._base)
		return self._ulink

	@property
	def dlink(self):
		"""dlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dlink'):
			from .Trace_.Dlink import Dlink
			self._dlink = Dlink(self._core, self._base)
		return self._dlink

	@property
	def loopback(self):
		"""loopback commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_loopback'):
			from .Trace_.Loopback import Loopback
			self._loopback = Loopback(self._core, self._base)
		return self._loopback

	@property
	def tauLink(self):
		"""tauLink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tauLink'):
			from .Trace_.TauLink import TauLink
			self._tauLink = TauLink(self._core, self._base)
		return self._tauLink

	@property
	def taLoopback(self):
		"""taLoopback commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_taLoopback'):
			from .Trace_.TaLoopback import TaLoopback
			self._taLoopback = TaLoopback(self._core, self._base)
		return self._taLoopback

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
