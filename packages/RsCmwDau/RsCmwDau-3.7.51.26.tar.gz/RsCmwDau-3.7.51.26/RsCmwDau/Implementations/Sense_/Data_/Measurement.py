from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 21 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	@property
	def ipAnalysis(self):
		"""ipAnalysis commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipAnalysis'):
			from .Measurement_.IpAnalysis import IpAnalysis
			self._ipAnalysis = IpAnalysis(self._core, self._base)
		return self._ipAnalysis

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_throughput'):
			from .Measurement_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def dnsRequests(self):
		"""dnsRequests commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dnsRequests'):
			from .Measurement_.DnsRequests import DnsRequests
			self._dnsRequests = DnsRequests(self._core, self._base)
		return self._dnsRequests

	@property
	def ipLogging(self):
		"""ipLogging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipLogging'):
			from .Measurement_.IpLogging import IpLogging
			self._ipLogging = IpLogging(self._core, self._base)
		return self._ipLogging

	@property
	def ipReplay(self):
		"""ipReplay commands group. 2 Sub-classes, 1 commands."""
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
