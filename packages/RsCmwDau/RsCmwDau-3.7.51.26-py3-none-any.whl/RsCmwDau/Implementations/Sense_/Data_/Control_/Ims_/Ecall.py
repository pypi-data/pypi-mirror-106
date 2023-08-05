from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ecall:
	"""Ecall commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ecall", core, parent)

	@property
	def msd(self):
		"""msd commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_msd'):
			from .Ecall_.Msd import Msd
			self._msd = Msd(self._core, self._base)
		return self._msd

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .Ecall_.TypePy import TypePy
			self._typePy = TypePy(self._core, self._base)
		return self._typePy

	@property
	def callId(self):
		"""callId commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_callId'):
			from .Ecall_.CallId import CallId
			self._callId = CallId(self._core, self._base)
		return self._callId

	def clone(self) -> 'Ecall':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ecall(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
