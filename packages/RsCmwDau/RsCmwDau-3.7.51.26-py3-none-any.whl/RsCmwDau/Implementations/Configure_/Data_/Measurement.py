from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 117 total commands, 12 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	@property
	def ipAnalysis(self):
		"""ipAnalysis commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipAnalysis'):
			from .Measurement_.IpAnalysis import IpAnalysis
			self._ipAnalysis = IpAnalysis(self._core, self._base)
		return self._ipAnalysis

	@property
	def throughput(self):
		"""throughput commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_throughput'):
			from .Measurement_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_select'):
			from .Measurement_.Select import Select
			self._select = Select(self._core, self._base)
		return self._select

	@property
	def ran(self):
		"""ran commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ran'):
			from .Measurement_.Ran import Ran
			self._ran = Ran(self._core, self._base)
		return self._ran

	@property
	def adelay(self):
		"""adelay commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_adelay'):
			from .Measurement_.Adelay import Adelay
			self._adelay = Adelay(self._core, self._base)
		return self._adelay

	@property
	def ping(self):
		"""ping commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_ping'):
			from .Measurement_.Ping import Ping
			self._ping = Ping(self._core, self._base)
		return self._ping

	@property
	def dnsRequests(self):
		"""dnsRequests commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dnsRequests'):
			from .Measurement_.DnsRequests import DnsRequests
			self._dnsRequests = DnsRequests(self._core, self._base)
		return self._dnsRequests

	@property
	def iperf(self):
		"""iperf commands group. 3 Sub-classes, 11 commands."""
		if not hasattr(self, '_iperf'):
			from .Measurement_.Iperf import Iperf
			self._iperf = Iperf(self._core, self._base)
		return self._iperf

	@property
	def ipLogging(self):
		"""ipLogging commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_ipLogging'):
			from .Measurement_.IpLogging import IpLogging
			self._ipLogging = IpLogging(self._core, self._base)
		return self._ipLogging

	@property
	def ipReplay(self):
		"""ipReplay commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipReplay'):
			from .Measurement_.IpReplay import IpReplay
			self._ipReplay = IpReplay(self._core, self._base)
		return self._ipReplay

	@property
	def nimpairments(self):
		"""nimpairments commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_nimpairments'):
			from .Measurement_.Nimpairments import Nimpairments
			self._nimpairments = Nimpairments(self._core, self._base)
		return self._nimpairments

	@property
	def qos(self):
		"""qos commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_qos'):
			from .Measurement_.Qos import Qos
			self._qos = Qos(self._core, self._base)
		return self._qos

	def get_ip_connect(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement:IPConn \n
		Snippet: value: bool = driver.configure.data.measurement.get_ip_connect() \n
		No command help available \n
			:return: ip_on: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement:IPConn?')
		return Conversions.str_to_bool(response)

	def set_ip_connect(self, ip_on: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement:IPConn \n
		Snippet: driver.configure.data.measurement.set_ip_connect(ip_on = False) \n
		No command help available \n
			:param ip_on: No help available
		"""
		param = Conversions.bool_to_str(ip_on)
		self._core.io.write(f'CONFigure:DATA:MEASurement:IPConn {param}')

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
