from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Key:
	"""Key commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("key", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.KeyType:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY:TYPE \n
		Snippet: value: enums.KeyType = driver.configure.data.control.epdg.authentic.key.get_type_py() \n
		Selects the key type to be used with the MILENAGE algorithm set. Currently, only OPc is supported. \n
			:return: auth_key_type: OPC
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.KeyType)

	def set_type_py(self, auth_key_type: enums.KeyType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY:TYPE \n
		Snippet: driver.configure.data.control.epdg.authentic.key.set_type_py(auth_key_type = enums.KeyType.OP) \n
		Selects the key type to be used with the MILENAGE algorithm set. Currently, only OPc is supported. \n
			:param auth_key_type: OPC
		"""
		param = Conversions.enum_scalar_to_str(auth_key_type, enums.KeyType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY:TYPE {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY \n
		Snippet: value: str = driver.configure.data.control.epdg.authentic.key.get_value() \n
		Defines the secret key K as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:return: auth_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY?')
		return trim_str_response(response)

	def set_value(self, auth_key: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY \n
		Snippet: driver.configure.data.control.epdg.authentic.key.set_value(auth_key = r1) \n
		Defines the secret key K as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:param auth_key: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(auth_key)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:KEY {param}')
