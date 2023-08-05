from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uauthentication:
	"""Uauthentication commands group definition. 14 total commands, 1 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uauthentication", core, parent)

	@property
	def ipSec(self):
		"""ipSec commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipSec'):
			from .Uauthentication_.IpSec import IpSec
			self._ipSec = IpSec(self._core, self._base)
		return self._ipSec

	def get_puid(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:PUID \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_puid() \n
		No command help available \n
			:return: private_user_id: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:PUID?')
		return trim_str_response(response)

	def set_puid(self, private_user_id: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:PUID \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_puid(private_user_id = '1') \n
		No command help available \n
			:param private_user_id: No help available
		"""
		param = Conversions.value_to_quoted_str(private_user_id)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:PUID {param}')

	def get_key(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:KEY \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_key() \n
		No command help available \n
			:return: key: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:KEY?')
		return trim_str_response(response)

	def set_key(self, key: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:KEY \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_key(key = r1) \n
		No command help available \n
			:param key: No help available
		"""
		param = Conversions.value_to_str(key)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:KEY {param}')

	def get_rand(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:RAND \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_rand() \n
		No command help available \n
			:return: rand: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:RAND?')
		return trim_str_response(response)

	def set_rand(self, rand: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:RAND \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_rand(rand = r1) \n
		No command help available \n
			:param rand: No help available
		"""
		param = Conversions.value_to_str(rand)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:RAND {param}')

	# noinspection PyTypeChecker
	def get_algorithm(self) -> enums.AuthAlgorithm:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:ALGorithm \n
		Snippet: value: enums.AuthAlgorithm = driver.configure.data.control.ims.uauthentication.get_algorithm() \n
		No command help available \n
			:return: algorithm: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:ALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.AuthAlgorithm)

	def set_algorithm(self, algorithm: enums.AuthAlgorithm) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:ALGorithm \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_algorithm(algorithm = enums.AuthAlgorithm.MILenage) \n
		No command help available \n
			:param algorithm: No help available
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.AuthAlgorithm)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:ALGorithm {param}')

	def get_amf(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AMF \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_amf() \n
		No command help available \n
			:return: amf: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:AMF?')
		return trim_str_response(response)

	def set_amf(self, amf: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AMF \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_amf(amf = r1) \n
		No command help available \n
			:param amf: No help available
		"""
		param = Conversions.value_to_str(amf)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:AMF {param}')

	# noinspection PyTypeChecker
	def get_aka_version(self) -> enums.AkaVersion:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AKAVersion \n
		Snippet: value: enums.AkaVersion = driver.configure.data.control.ims.uauthentication.get_aka_version() \n
		No command help available \n
			:return: aka_version: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:AKAVersion?')
		return Conversions.str_to_scalar_enum(response, enums.AkaVersion)

	def set_aka_version(self, aka_version: enums.AkaVersion) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AKAVersion \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_aka_version(aka_version = enums.AkaVersion.AKA1) \n
		No command help available \n
			:param aka_version: No help available
		"""
		param = Conversions.enum_scalar_to_str(aka_version, enums.AkaVersion)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:AKAVersion {param}')

	# noinspection PyTypeChecker
	def get_ktype(self) -> enums.KeyType:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:KTYPe \n
		Snippet: value: enums.KeyType = driver.configure.data.control.ims.uauthentication.get_ktype() \n
		No command help available \n
			:return: key_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:KTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.KeyType)

	def set_ktype(self, key_type: enums.KeyType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:KTYPe \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_ktype(key_type = enums.KeyType.OP) \n
		No command help available \n
			:param key_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(key_type, enums.KeyType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:KTYPe {param}')

	def get_aop(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AOP \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_aop() \n
		No command help available \n
			:return: aop: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:AOP?')
		return trim_str_response(response)

	def set_aop(self, aop: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AOP \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_aop(aop = r1) \n
		No command help available \n
			:param aop: No help available
		"""
		param = Conversions.value_to_str(aop)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:AOP {param}')

	def get_aopc(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AOPC \n
		Snippet: value: str = driver.configure.data.control.ims.uauthentication.get_aopc() \n
		No command help available \n
			:return: aopc: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:AOPC?')
		return trim_str_response(response)

	def set_aopc(self, aopc: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:AOPC \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_aopc(aopc = r1) \n
		No command help available \n
			:param aopc: No help available
		"""
		param = Conversions.value_to_str(aopc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:AOPC {param}')

	def get_res_length(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:RESLength \n
		Snippet: value: int = driver.configure.data.control.ims.uauthentication.get_res_length() \n
		No command help available \n
			:return: res_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic:RESLength?')
		return Conversions.str_to_int(response)

	def set_res_length(self, res_length: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic:RESLength \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_res_length(res_length = 1) \n
		No command help available \n
			:param res_length: No help available
		"""
		param = Conversions.decimal_value_to_str(res_length)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic:RESLength {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic \n
		Snippet: value: bool = driver.configure.data.control.ims.uauthentication.get_value() \n
		No command help available \n
			:return: uauthentic: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:UAUThentic?')
		return Conversions.str_to_bool(response)

	def set_value(self, uauthentic: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:UAUThentic \n
		Snippet: driver.configure.data.control.ims.uauthentication.set_value(uauthentic = False) \n
		No command help available \n
			:param uauthentic: No help available
		"""
		param = Conversions.bool_to_str(uauthentic)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:UAUThentic {param}')

	def clone(self) -> 'Uauthentication':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uauthentication(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
