from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("address", core, parent)

	def get_ipv_four(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVFour \n
		Snippet: value: str = driver.configure.data.control.epdg.address.get_ipv_four() \n
		Specifies the IPv4 address of the ePDG. \n
			:return: ip_v_4_addressess: IPv4 address string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVFour?')
		return trim_str_response(response)

	def set_ipv_four(self, ip_v_4_addressess: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVFour \n
		Snippet: driver.configure.data.control.epdg.address.set_ipv_four(ip_v_4_addressess = '1') \n
		Specifies the IPv4 address of the ePDG. \n
			:param ip_v_4_addressess: IPv4 address string
		"""
		param = Conversions.value_to_quoted_str(ip_v_4_addressess)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVFour {param}')

	def get_ipv_six(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVSix \n
		Snippet: value: str = driver.configure.data.control.epdg.address.get_ipv_six() \n
		Specifies the IPv6 address of the ePDG. \n
			:return: ip_v_6_addressess: IPv6 address string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVSix?')
		return trim_str_response(response)

	def set_ipv_six(self, ip_v_6_addressess: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVSix \n
		Snippet: driver.configure.data.control.epdg.address.set_ipv_six(ip_v_6_addressess = '1') \n
		Specifies the IPv6 address of the ePDG. \n
			:param ip_v_6_addressess: IPv6 address string
		"""
		param = Conversions.value_to_quoted_str(ip_v_6_addressess)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:ADDRess:IPVSix {param}')
