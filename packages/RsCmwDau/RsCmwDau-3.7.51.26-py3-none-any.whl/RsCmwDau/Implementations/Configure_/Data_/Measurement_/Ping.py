from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ping:
	"""Ping commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ping", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:TIMeout \n
		Snippet: value: float = driver.configure.data.measurement.ping.get_timeout() \n
		Specifies a timeout for ping requests. \n
			:return: timeout: Range: 1 s to 9 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:PING:TIMeout?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:TIMeout \n
		Snippet: driver.configure.data.measurement.ping.set_timeout(timeout = 1.0) \n
		Specifies a timeout for ping requests. \n
			:param timeout: Range: 1 s to 9 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:PING:TIMeout {param}')

	def get_dip_address(self) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:DIPaddress \n
		Snippet: value: str = driver.configure.data.measurement.ping.get_dip_address() \n
		Specifies the destination IP address for the ping command. \n
			:return: ip_address: IPv4 or IPv6 address as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:PING:DIPaddress?')
		return trim_str_response(response)

	def set_dip_address(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:DIPaddress \n
		Snippet: driver.configure.data.measurement.ping.set_dip_address(ip_address = '1') \n
		Specifies the destination IP address for the ping command. \n
			:param ip_address: IPv4 or IPv6 address as string
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:PING:DIPaddress {param}')

	def get_psize(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:PSIZe \n
		Snippet: value: int = driver.configure.data.measurement.ping.get_psize() \n
		Specifies the payload size of echo request packets. \n
			:return: packet_size: Range: 0 bytes to 65507 bytes , Unit: bytes
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:PING:PSIZe?')
		return Conversions.str_to_int(response)

	def set_psize(self, packet_size: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:PSIZe \n
		Snippet: driver.configure.data.measurement.ping.set_psize(packet_size = 1) \n
		Specifies the payload size of echo request packets. \n
			:param packet_size: Range: 0 bytes to 65507 bytes , Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(packet_size)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:PING:PSIZe {param}')

	def get_pcount(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:PCOunt \n
		Snippet: value: int = driver.configure.data.measurement.ping.get_pcount() \n
		Specifies the number of echo request packets to be sent. \n
			:return: ping_count: Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:PING:PCOunt?')
		return Conversions.str_to_int(response)

	def set_pcount(self, ping_count: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:PCOunt \n
		Snippet: driver.configure.data.measurement.ping.set_pcount(ping_count = 1) \n
		Specifies the number of echo request packets to be sent. \n
			:param ping_count: Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(ping_count)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:PING:PCOunt {param}')

	def get_interval(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:INTerval \n
		Snippet: value: float = driver.configure.data.measurement.ping.get_interval() \n
		Specifies the interval between two ping requests. \n
			:return: interval: Range: 0.2 s to 10 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:PING:INTerval?')
		return Conversions.str_to_float(response)

	def set_interval(self, interval: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:PING:INTerval \n
		Snippet: driver.configure.data.measurement.ping.set_interval(interval = 1.0) \n
		Specifies the interval between two ping requests. \n
			:param interval: Range: 0.2 s to 10 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:PING:INTerval {param}')
