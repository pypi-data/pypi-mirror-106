from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("id", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.IdType:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ID:TYPE \n
		Snippet: value: enums.IdType = driver.configure.data.control.epdg.id.get_type_py() \n
		Configures the type of the ePDG identification. \n
			:return: id_type: IPVF | FQDN | RFC | IPVS | KEY IPVF: ID_IPv4_ADDR FQDN: ID_FQDN RFC: ID_RFC822_ADDR IPVS: ID_IPV6_ADDR KEY: ID_KEY_ID
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:ID:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IdType)

	def set_type_py(self, id_type: enums.IdType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ID:TYPE \n
		Snippet: driver.configure.data.control.epdg.id.set_type_py(id_type = enums.IdType.ASND) \n
		Configures the type of the ePDG identification. \n
			:param id_type: IPVF | FQDN | RFC | IPVS | KEY IPVF: ID_IPv4_ADDR FQDN: ID_FQDN RFC: ID_RFC822_ADDR IPVS: ID_IPV6_ADDR KEY: ID_KEY_ID
		"""
		param = Conversions.enum_scalar_to_str(id_type, enums.IdType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:ID:TYPE {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ID:VALue \n
		Snippet: value: str = driver.configure.data.control.epdg.id.get_value() \n
		Configures the value of the ePDG identification. \n
			:return: id_value: Identification as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:ID:VALue?')
		return trim_str_response(response)

	def set_value(self, id_value: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ID:VALue \n
		Snippet: driver.configure.data.control.epdg.id.set_value(id_value = '1') \n
		Configures the value of the ePDG identification. \n
			:param id_value: Identification as string
		"""
		param = Conversions.value_to_quoted_str(id_value)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:ID:VALue {param}')
