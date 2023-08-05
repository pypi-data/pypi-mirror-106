from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Certificate:
	"""Certificate commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("certificate", core, parent)

	def get_key(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:KEY \n
		Snippet: value: str = driver.configure.data.control.epdg.certificate.get_key() \n
		Selects the server key file to be used for SSL. \n
			:return: certificate_key_file: Filename as string, without path
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:CERTificate:KEY?')
		return trim_str_response(response)

	def set_key(self, certificate_key_file: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:KEY \n
		Snippet: driver.configure.data.control.epdg.certificate.set_key(certificate_key_file = '1') \n
		Selects the server key file to be used for SSL. \n
			:param certificate_key_file: Filename as string, without path
		"""
		param = Conversions.value_to_quoted_str(certificate_key_file)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:CERTificate:KEY {param}')

	def get_enable(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:ENABle \n
		Snippet: value: str = driver.configure.data.control.epdg.certificate.get_enable() \n
		Enables the usage of certificates for SSL. \n
			:return: certificate_key_enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:CERTificate:ENABle?')
		return trim_str_response(response)

	def set_enable(self, certificate_key_enable: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:ENABle \n
		Snippet: driver.configure.data.control.epdg.certificate.set_enable(certificate_key_enable = '1') \n
		Enables the usage of certificates for SSL. \n
			:param certificate_key_enable: OFF | ON
		"""
		param = Conversions.value_to_quoted_str(certificate_key_enable)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:CERTificate:ENABle {param}')

	def get_certificate(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:CERTificate \n
		Snippet: value: str = driver.configure.data.control.epdg.certificate.get_certificate() \n
		Selects the server certificate file to be used for SSL. \n
			:return: certificate_server_file: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:CERTificate:CERTificate?')
		return trim_str_response(response)

	def set_certificate(self, certificate_server_file: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CERTificate:CERTificate \n
		Snippet: driver.configure.data.control.epdg.certificate.set_certificate(certificate_server_file = '1') \n
		Selects the server certificate file to be used for SSL. \n
			:param certificate_server_file: Filename as string, without path
		"""
		param = Conversions.value_to_quoted_str(certificate_server_file)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:CERTificate:CERTificate {param}')
