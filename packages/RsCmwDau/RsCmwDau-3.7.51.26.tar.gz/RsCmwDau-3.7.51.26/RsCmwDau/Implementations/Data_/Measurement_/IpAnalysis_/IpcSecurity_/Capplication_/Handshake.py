from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handshake:
	"""Handshake commands group definition. 9 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handshake", core, parent)

	@property
	def negotiated(self):
		"""negotiated commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_negotiated'):
			from .Handshake_.Negotiated import Negotiated
			self._negotiated = Negotiated(self._core, self._base)
		return self._negotiated

	@property
	def offered(self):
		"""offered commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_offered'):
			from .Handshake_.Offered import Offered
			self._offered = Offered(self._core, self._base)
		return self._offered

	def clone(self) -> 'Handshake':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Handshake(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
