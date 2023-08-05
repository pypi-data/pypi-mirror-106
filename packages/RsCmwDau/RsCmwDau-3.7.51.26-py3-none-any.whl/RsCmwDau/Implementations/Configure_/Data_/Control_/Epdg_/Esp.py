from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Esp:
	"""Esp commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esp", core, parent)

	@property
	def rekey(self):
		"""rekey commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rekey'):
			from .Esp_.Rekey import Rekey
			self._rekey = Rekey(self._core, self._base)
		return self._rekey

	# noinspection PyTypeChecker
	class EncryptionStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Aescbc: bool: OFF | ON ENCR_AES_CBC
			- Encr_3_Des: bool: OFF | ON ENCR_3DES"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Aescbc'),
			ArgStruct.scalar_bool('Encr_3_Des')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aescbc: bool = None
			self.Encr_3_Des: bool = None

	def get_encryption(self) -> EncryptionStruct:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:ENCRyption \n
		Snippet: value: EncryptionStruct = driver.configure.data.control.epdg.esp.get_encryption() \n
		Selects the supported encryption algorithms for the ESP protocol. \n
			:return: structure: for return value, see the help for EncryptionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:ESP:ENCRyption?', self.__class__.EncryptionStruct())

	def set_encryption(self, value: EncryptionStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:ENCRyption \n
		Snippet: driver.configure.data.control.epdg.esp.set_encryption(value = EncryptionStruct()) \n
		Selects the supported encryption algorithms for the ESP protocol. \n
			:param value: see the help for EncryptionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:ESP:ENCRyption', value)

	# noinspection PyTypeChecker
	class IntegrityStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Md_596: bool: OFF | ON AUTH_HMAC_MD5_96
			- Shai_96: bool: OFF | ON AUTH_HMAC_SHA1_96
			- Xcbc_96: bool: OFF | ON AUTH_AES_XCBC_96
			- Sha_256: bool: OFF | ON AUTH_HMAC_SHA2_256_128
			- Sha_384: bool: OFF | ON AUTH_HMAC_SHA2_384_192
			- Sha_512: bool: OFF | ON AUTH_HMAC_SHA2_512_256"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Md_596'),
			ArgStruct.scalar_bool('Shai_96'),
			ArgStruct.scalar_bool('Xcbc_96'),
			ArgStruct.scalar_bool('Sha_256'),
			ArgStruct.scalar_bool('Sha_384'),
			ArgStruct.scalar_bool('Sha_512')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Md_596: bool = None
			self.Shai_96: bool = None
			self.Xcbc_96: bool = None
			self.Sha_256: bool = None
			self.Sha_384: bool = None
			self.Sha_512: bool = None

	def get_integrity(self) -> IntegrityStruct:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:INTegrity \n
		Snippet: value: IntegrityStruct = driver.configure.data.control.epdg.esp.get_integrity() \n
		Selects the supported integrity protection algorithms for the ESP protocol. \n
			:return: structure: for return value, see the help for IntegrityStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:ESP:INTegrity?', self.__class__.IntegrityStruct())

	def set_integrity(self, value: IntegrityStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:INTegrity \n
		Snippet: driver.configure.data.control.epdg.esp.set_integrity(value = IntegrityStruct()) \n
		Selects the supported integrity protection algorithms for the ESP protocol. \n
			:param value: see the help for IntegrityStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:ESP:INTegrity', value)

	def get_lifetime(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:LIFetime \n
		Snippet: value: int = driver.configure.data.control.epdg.esp.get_lifetime() \n
		No command help available \n
			:return: espsa_lifetime: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:ESP:LIFetime?')
		return Conversions.str_to_int(response)

	def set_lifetime(self, espsa_lifetime: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:ESP:LIFetime \n
		Snippet: driver.configure.data.control.epdg.esp.set_lifetime(espsa_lifetime = 1) \n
		No command help available \n
			:param espsa_lifetime: No help available
		"""
		param = Conversions.decimal_value_to_str(espsa_lifetime)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:ESP:LIFetime {param}')

	def clone(self) -> 'Esp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Esp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
