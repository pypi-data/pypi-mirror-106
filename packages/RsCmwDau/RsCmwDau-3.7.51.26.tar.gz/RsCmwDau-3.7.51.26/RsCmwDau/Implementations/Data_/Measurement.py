from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 125 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	@property
	def ipAnalysis(self):
		"""ipAnalysis commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipAnalysis'):
			from .Measurement_.IpAnalysis import IpAnalysis
			self._ipAnalysis = IpAnalysis(self._core, self._base)
		return self._ipAnalysis

	@property
	def adelay(self):
		"""adelay commands group. 7 Sub-classes, 3 commands."""
		if not hasattr(self, '_adelay'):
			from .Measurement_.Adelay import Adelay
			self._adelay = Adelay(self._core, self._base)
		return self._adelay

	@property
	def throughput(self):
		"""throughput commands group. 4 Sub-classes, 3 commands."""
		if not hasattr(self, '_throughput'):
			from .Measurement_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def ping(self):
		"""ping commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_ping'):
			from .Measurement_.Ping import Ping
			self._ping = Ping(self._core, self._base)
		return self._ping

	@property
	def dnsRequests(self):
		"""dnsRequests commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_dnsRequests'):
			from .Measurement_.DnsRequests import DnsRequests
			self._dnsRequests = DnsRequests(self._core, self._base)
		return self._dnsRequests

	@property
	def iperf(self):
		"""iperf commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_iperf'):
			from .Measurement_.Iperf import Iperf
			self._iperf = Iperf(self._core, self._base)
		return self._iperf

	@property
	def ipLogging(self):
		"""ipLogging commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipLogging'):
			from .Measurement_.IpLogging import IpLogging
			self._ipLogging = IpLogging(self._core, self._base)
		return self._ipLogging

	@property
	def ipReplay(self):
		"""ipReplay commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipReplay'):
			from .Measurement_.IpReplay import IpReplay
			self._ipReplay = IpReplay(self._core, self._base)
		return self._ipReplay

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
