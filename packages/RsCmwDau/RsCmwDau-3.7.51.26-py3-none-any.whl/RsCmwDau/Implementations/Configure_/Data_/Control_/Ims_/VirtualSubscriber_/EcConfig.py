from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EcConfig:
	"""EcConfig commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ecConfig", core, parent)

	@property
	def actmypes(self):
		"""actmypes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_actmypes'):
			from .EcConfig_.Actmypes import Actmypes
			self._actmypes = Actmypes(self._core, self._base)
		return self._actmypes

	@property
	def acuris(self):
		"""acuris commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acuris'):
			from .EcConfig_.Acuris import Acuris
			self._acuris = Acuris(self._core, self._base)
		return self._acuris

	def clone(self) -> 'EcConfig':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EcConfig(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
