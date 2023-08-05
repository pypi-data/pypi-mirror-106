from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dns:
	"""Dns commands group definition. 7 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dns", core, parent)

	@property
	def current(self):
		"""current commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .Dns_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def local(self):
		"""local commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Dns_.Local import Local
			self._local = Local(self._core, self._base)
		return self._local

	@property
	def aservices(self):
		"""aservices commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aservices'):
			from .Dns_.Aservices import Aservices
			self._aservices = Aservices(self._core, self._base)
		return self._aservices

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_test'):
			from .Dns_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	def clone(self) -> 'Dns':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dns(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
