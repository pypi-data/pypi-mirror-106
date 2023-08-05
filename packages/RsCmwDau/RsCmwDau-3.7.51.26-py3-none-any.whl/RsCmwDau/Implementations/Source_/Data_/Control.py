from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 12 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("control", core, parent)

	@property
	def udp(self):
		"""udp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_udp'):
			from .Control_.Udp import Udp
			self._udp = Udp(self._core, self._base)
		return self._udp

	@property
	def supl(self):
		"""supl commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_supl'):
			from .Control_.Supl import Supl
			self._supl = Supl(self._core, self._base)
		return self._supl

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Control_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def dns(self):
		"""dns commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dns'):
			from .Control_.Dns import Dns
			self._dns = Dns(self._core, self._base)
		return self._dns

	@property
	def ftp(self):
		"""ftp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftp'):
			from .Control_.Ftp import Ftp
			self._ftp = Ftp(self._core, self._base)
		return self._ftp

	@property
	def http(self):
		"""http commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_http'):
			from .Control_.Http import Http
			self._http = Http(self._core, self._base)
		return self._http

	@property
	def ims(self):
		"""ims commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ims'):
			from .Control_.Ims import Ims
			self._ims = Ims(self._core, self._base)
		return self._ims

	@property
	def epdg(self):
		"""epdg commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epdg'):
			from .Control_.Epdg import Epdg
			self._epdg = Epdg(self._core, self._base)
		return self._epdg

	def clone(self) -> 'Control':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Control(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
