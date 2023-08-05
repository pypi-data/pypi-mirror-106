from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Authentic:
	"""Authentic commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("authentic", core, parent)

	@property
	def key(self):
		"""key commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_key'):
			from .Authentic_.Key import Key
			self._key = Key(self._core, self._base)
		return self._key

	# noinspection PyTypeChecker
	def get_algorithm(self) -> enums.AuthAlgorithm:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:ALGorithm \n
		Snippet: value: enums.AuthAlgorithm = driver.configure.data.control.epdg.authentic.get_algorithm() \n
		Specifies the key generation algorithm set used by the SIM. \n
			:return: auth_alg: XOR | MILenage
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:ALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.AuthAlgorithm)

	def set_algorithm(self, auth_alg: enums.AuthAlgorithm) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:ALGorithm \n
		Snippet: driver.configure.data.control.epdg.authentic.set_algorithm(auth_alg = enums.AuthAlgorithm.MILenage) \n
		Specifies the key generation algorithm set used by the SIM. \n
			:param auth_alg: XOR | MILenage
		"""
		param = Conversions.enum_scalar_to_str(auth_alg, enums.AuthAlgorithm)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:ALGorithm {param}')

	def get_imsi(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:IMSI \n
		Snippet: value: str = driver.configure.data.control.epdg.authentic.get_imsi() \n
		Specifies the IMSI of the SIM card. \n
			:return: auth_imsi: String value, containing 15 digits
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:IMSI?')
		return trim_str_response(response)

	def set_imsi(self, auth_imsi: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:IMSI \n
		Snippet: driver.configure.data.control.epdg.authentic.set_imsi(auth_imsi = '1') \n
		Specifies the IMSI of the SIM card. \n
			:param auth_imsi: String value, containing 15 digits
		"""
		param = Conversions.value_to_quoted_str(auth_imsi)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:IMSI {param}')

	def get_rand(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:RAND \n
		Snippet: value: str = driver.configure.data.control.epdg.authentic.get_rand() \n
		Defines the random number RAND as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:return: auth_rand: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:RAND?')
		return trim_str_response(response)

	def set_rand(self, auth_rand: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:RAND \n
		Snippet: driver.configure.data.control.epdg.authentic.set_rand(auth_rand = r1) \n
		Defines the random number RAND as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:param auth_rand: Range: #H0 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(auth_rand)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:RAND {param}')

	def get_amf(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:AMF \n
		Snippet: value: str = driver.configure.data.control.epdg.authentic.get_amf() \n
		Specifies the authentication management field (AMF) as four-digit hexadecimal number. Leading zeros can be omitted. \n
			:return: auth_amf: Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:AMF?')
		return trim_str_response(response)

	def set_amf(self, auth_amf: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:AMF \n
		Snippet: driver.configure.data.control.epdg.authentic.set_amf(auth_amf = r1) \n
		Specifies the authentication management field (AMF) as four-digit hexadecimal number. Leading zeros can be omitted. \n
			:param auth_amf: Range: #H0 to #HFFFF
		"""
		param = Conversions.value_to_str(auth_amf)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:AMF {param}')

	def get_opc(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:OPC \n
		Snippet: value: str = driver.configure.data.control.epdg.authentic.get_opc() \n
		Specifies the key OPc as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:return: auth_opc: Range: #H00000000000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:AUTHentic:OPC?')
		return trim_str_response(response)

	def set_opc(self, auth_opc: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:AUTHentic:OPC \n
		Snippet: driver.configure.data.control.epdg.authentic.set_opc(auth_opc = r1) \n
		Specifies the key OPc as 32-digit hexadecimal number. Leading zeros can be omitted. \n
			:param auth_opc: Range: #H00000000000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.value_to_str(auth_opc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:AUTHentic:OPC {param}')

	def clone(self) -> 'Authentic':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Authentic(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
