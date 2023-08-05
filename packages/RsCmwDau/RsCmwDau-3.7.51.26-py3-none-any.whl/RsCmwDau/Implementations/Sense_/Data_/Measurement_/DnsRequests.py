from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DnsRequests:
	"""DnsRequests commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dnsRequests", core, parent)

	def get_rcount(self) -> int:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:DNSRequests:RCOunt \n
		Snippet: value: int = driver.sense.data.measurement.dnsRequests.get_rcount() \n
		Queries the number of already monitored DNS requests. \n
			:return: req_count: Number of requests
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:DNSRequests:RCOunt?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Client_Ip: List[str]: String indicating the IP address of the client (DUT) that has sent the DNS request
			- Url: List[str]: String indicating the domain or application to be resolved
			- Ip: List[str]: String indicating the IP address or domain returned as answer to the DNS request
			- Timestamp: List[str]: Timestamp as string in the format 'hh:mm:ss'"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Client_Ip', DataType.StringList, None, False, True, 1),
			ArgStruct('Url', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip', DataType.StringList, None, False, True, 1),
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Client_Ip: List[str] = None
			self.Url: List[str] = None
			self.Ip: List[str] = None
			self.Timestamp: List[str] = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:DNSRequests \n
		Snippet: value: ValueStruct = driver.sense.data.measurement.dnsRequests.get_value() \n
		Queries information about the monitored DNS requests. After the reliability indicator, four results are returned for each
		DNS request: <Reliability>, {<ClientIP>, <URL>, <IP>, <Timestamp>}request 1, {...}request 2, ... To query the number of
		monitored requests, see method RsCmwDau.Sense.Data.Measurement.DnsRequests.rcount. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:MEASurement<MeasInstance>:DNSRequests?', self.__class__.ValueStruct())
