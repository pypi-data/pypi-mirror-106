from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Authentication:
	"""Authentication commands group definition. 5 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("authentication", core, parent)

	@property
	def scheme(self):
		"""scheme commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scheme'):
			from .Authentication_.Scheme import Scheme
			self._scheme = Scheme(self._core, self._base)
		return self._scheme

	@property
	def algorithm(self):
		"""algorithm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_algorithm'):
			from .Authentication_.Algorithm import Algorithm
			self._algorithm = Algorithm(self._core, self._base)
		return self._algorithm

	@property
	def key(self):
		"""key commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_key'):
			from .Authentication_.Key import Key
			self._key = Key(self._core, self._base)
		return self._key

	@property
	def amf(self):
		"""amf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amf'):
			from .Authentication_.Amf import Amf
			self._amf = Amf(self._core, self._base)
		return self._amf

	@property
	def opc(self):
		"""opc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_opc'):
			from .Authentication_.Opc import Opc
			self._opc = Opc(self._core, self._base)
		return self._opc

	def clone(self) -> 'Authentication':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Authentication(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
