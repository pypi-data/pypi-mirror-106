from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("test", core, parent)

	def get_domain(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:TEST:DOMain \n
		Snippet: value: str = driver.configure.data.control.dns.test.get_domain() \n
		Specifies the domain to be resolved during a test of the foreign DNS server. \n
			:return: domain: String specifying the URL of the domain
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:TEST:DOMain?')
		return trim_str_response(response)

	def set_domain(self, domain: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:TEST:DOMain \n
		Snippet: driver.configure.data.control.dns.test.set_domain(domain = '1') \n
		Specifies the domain to be resolved during a test of the foreign DNS server. \n
			:param domain: String specifying the URL of the domain
		"""
		param = Conversions.value_to_quoted_str(domain)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:TEST:DOMain {param}')

	def start(self) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:TEST:STARt \n
		Snippet: driver.configure.data.control.dns.test.start() \n
		Starts a test of the foreign DNS server. \n
		"""
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:TEST:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:TEST:STARt \n
		Snippet: driver.configure.data.control.dns.test.start_with_opc() \n
		Starts a test of the foreign DNS server. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:DNS:TEST:STARt')
