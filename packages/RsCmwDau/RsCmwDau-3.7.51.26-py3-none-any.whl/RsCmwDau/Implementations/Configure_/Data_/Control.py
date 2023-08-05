from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 271 total commands, 11 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("control", core, parent)

	@property
	def udp(self):
		"""udp commands group. 2 Sub-classes, 1 commands."""
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
		"""ims commands group. 19 Sub-classes, 0 commands."""
		if not hasattr(self, '_ims'):
			from .Control_.Ims import Ims
			self._ims = Ims(self._core, self._base)
		return self._ims

	@property
	def supl(self):
		"""supl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_supl'):
			from .Control_.Supl import Supl
			self._supl = Supl(self._core, self._base)
		return self._supl

	@property
	def ipvSix(self):
		"""ipvSix commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvSix'):
			from .Control_.IpvSix import IpvSix
			self._ipvSix = IpvSix(self._core, self._base)
		return self._ipvSix

	@property
	def advanced(self):
		"""advanced commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_advanced'):
			from .Control_.Advanced import Advanced
			self._advanced = Advanced(self._core, self._base)
		return self._advanced

	@property
	def ipvFour(self):
		"""ipvFour commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipvFour'):
			from .Control_.IpvFour import IpvFour
			self._ipvFour = IpvFour(self._core, self._base)
		return self._ipvFour

	@property
	def dns(self):
		"""dns commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_dns'):
			from .Control_.Dns import Dns
			self._dns = Dns(self._core, self._base)
		return self._dns

	@property
	def ftp(self):
		"""ftp commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_ftp'):
			from .Control_.Ftp import Ftp
			self._ftp = Ftp(self._core, self._base)
		return self._ftp

	@property
	def http(self):
		"""http commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_http'):
			from .Control_.Http import Http
			self._http = Http(self._core, self._base)
		return self._http

	@property
	def epdg(self):
		"""epdg commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_epdg'):
			from .Control_.Epdg import Epdg
			self._epdg = Epdg(self._core, self._base)
		return self._epdg

	def get_mtu(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:MTU \n
		Snippet: value: int = driver.configure.data.control.get_mtu() \n
		Specifies the MTU, that is the maximum IP packet size that can be transmitted without fragmentation. \n
			:return: max_trans_unit: Range: 552 bytes to 4096 bytes, Unit: bytes
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:MTU?')
		return Conversions.str_to_int(response)

	def set_mtu(self, max_trans_unit: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:MTU \n
		Snippet: driver.configure.data.control.set_mtu(max_trans_unit = 1) \n
		Specifies the MTU, that is the maximum IP packet size that can be transmitted without fragmentation. \n
			:param max_trans_unit: Range: 552 bytes to 4096 bytes, Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(max_trans_unit)
		self._core.io.write(f'CONFigure:DATA:CONTrol:MTU {param}')

	def clone(self) -> 'Control':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Control(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
