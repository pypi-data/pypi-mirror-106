from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 60 total commands, 12 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("control", core, parent)

	@property
	def services(self):
		"""services commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_services'):
			from .Control_.Services import Services
			self._services = Services(self._core, self._base)
		return self._services

	@property
	def udp(self):
		"""udp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_udp'):
			from .Control_.Udp import Udp
			self._udp = Udp(self._core, self._base)
		return self._udp

	@property
	def deploy(self):
		"""deploy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deploy'):
			from .Control_.Deploy import Deploy
			self._deploy = Deploy(self._core, self._base)
		return self._deploy

	@property
	def ims(self):
		"""ims commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_ims'):
			from .Control_.Ims import Ims
			self._ims = Ims(self._core, self._base)
		return self._ims

	@property
	def supl(self):
		"""supl commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_supl'):
			from .Control_.Supl import Supl
			self._supl = Supl(self._core, self._base)
		return self._supl

	@property
	def lan(self):
		"""lan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lan'):
			from .Control_.Lan import Lan
			self._lan = Lan(self._core, self._base)
		return self._lan

	@property
	def ipvFour(self):
		"""ipvFour commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Control_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	@property
	def ipvSix(self):
		"""ipvSix commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Control_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	@property
	def dns(self):
		"""dns commands group. 4 Sub-classes, 0 commands."""
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
		"""http commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_http'):
			from .Control_.Http import Http
			self._http = Http(self._core, self._base)
		return self._http

	@property
	def epdg(self):
		"""epdg commands group. 2 Sub-classes, 0 commands."""
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
