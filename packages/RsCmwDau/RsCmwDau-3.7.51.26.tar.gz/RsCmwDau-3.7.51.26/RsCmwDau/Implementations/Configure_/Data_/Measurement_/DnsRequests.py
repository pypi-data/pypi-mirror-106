from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DnsRequests:
	"""DnsRequests commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dnsRequests", core, parent)

	def get_mi_count(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<inst>:DNSRequests:MICount \n
		Snippet: value: int = driver.configure.data.measurement.dnsRequests.get_mi_count() \n
		Specifies the maximum length of the result list for DNS requests measurements. The result list is stored in a ring buffer.
		When it is full, the first result line is deleted whenever a new result line is added to the end. \n
			:return: max_index_count: Maximum number of DNS requests in the result list Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:DNSRequests:MICount?')
		return Conversions.str_to_int(response)

	def set_mi_count(self, max_index_count: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<inst>:DNSRequests:MICount \n
		Snippet: driver.configure.data.measurement.dnsRequests.set_mi_count(max_index_count = 1) \n
		Specifies the maximum length of the result list for DNS requests measurements. The result list is stored in a ring buffer.
		When it is full, the first result line is deleted whenever a new result line is added to the end. \n
			:param max_index_count: Maximum number of DNS requests in the result list Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(max_index_count)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:DNSRequests:MICount {param}')
