from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MendPoint:
	"""MendPoint commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mendPoint", core, parent)

	def get_port(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:PORT \n
		Snippet: value: int = driver.configure.data.control.ims.voice.mendPoint.get_port() \n
		No command help available \n
			:return: port: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, port: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:PORT \n
		Snippet: driver.configure.data.control.ims.voice.mendPoint.set_port(port = 1) \n
		No command help available \n
			:param port: No help available
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:PORT {param}')

	def get_ip_address(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:IPADdress \n
		Snippet: value: str = driver.configure.data.control.ims.voice.mendPoint.get_ip_address() \n
		No command help available \n
			:return: ip_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:IPADdress?')
		return trim_str_response(response)

	def set_ip_address(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:IPADdress \n
		Snippet: driver.configure.data.control.ims.voice.mendPoint.set_ip_address(ip_address = '1') \n
		No command help available \n
			:param ip_address: No help available
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:MENDpoint:IPADdress {param}')
