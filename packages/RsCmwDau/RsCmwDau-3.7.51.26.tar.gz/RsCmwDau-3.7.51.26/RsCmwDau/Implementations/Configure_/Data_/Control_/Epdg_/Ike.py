from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ike:
	"""Ike commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ike", core, parent)

	@property
	def rekey(self):
		"""rekey commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rekey'):
			from .Ike_.Rekey import Rekey
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
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:ENCRyption \n
		Snippet: value: EncryptionStruct = driver.configure.data.control.epdg.ike.get_encryption() \n
		Selects the supported encryption algorithms for the IKEv2 protocol. \n
			:return: structure: for return value, see the help for EncryptionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:IKE:ENCRyption?', self.__class__.EncryptionStruct())

	def set_encryption(self, value: EncryptionStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:ENCRyption \n
		Snippet: driver.configure.data.control.epdg.ike.set_encryption(value = EncryptionStruct()) \n
		Selects the supported encryption algorithms for the IKEv2 protocol. \n
			:param value: see the help for EncryptionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:IKE:ENCRyption', value)

	# noinspection PyTypeChecker
	class PrfStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Prfmd_5: bool: OFF | ON PRF_HMAC_MD5
			- Prfsha_1: bool: OFF | ON PRF_HMAC_SHA1
			- Sha_2256: bool: OFF | ON PRF_HMAC_SHA2_256
			- Sha_2384: bool: OFF | ON PRF_HMAC_SHA2_384
			- Sha_2512: bool: OFF | ON PRF_HMAC_SHA2_512"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Prfmd_5'),
			ArgStruct.scalar_bool('Prfsha_1'),
			ArgStruct.scalar_bool('Sha_2256'),
			ArgStruct.scalar_bool('Sha_2384'),
			ArgStruct.scalar_bool('Sha_2512')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Prfmd_5: bool = None
			self.Prfsha_1: bool = None
			self.Sha_2256: bool = None
			self.Sha_2384: bool = None
			self.Sha_2512: bool = None

	def get_prf(self) -> PrfStruct:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:PRF \n
		Snippet: value: PrfStruct = driver.configure.data.control.epdg.ike.get_prf() \n
		Selects the supported pseudorandom functions for the IKEv2 protocol. \n
			:return: structure: for return value, see the help for PrfStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:IKE:PRF?', self.__class__.PrfStruct())

	def set_prf(self, value: PrfStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:PRF \n
		Snippet: driver.configure.data.control.epdg.ike.set_prf(value = PrfStruct()) \n
		Selects the supported pseudorandom functions for the IKEv2 protocol. \n
			:param value: see the help for PrfStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:IKE:PRF', value)

	# noinspection PyTypeChecker
	class IntegrityStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hmac_Md_596: bool: OFF | ON AUTH_HMAC_MD5_96
			- Hmac_Shai_96: bool: OFF | ON AUTH_HMAC_SHA1_96
			- Aes_Xcb_96: bool: OFF | ON AUTH_AES_XCBC_96
			- Sha_2256128: bool: OFF | ON AUTH_HMAC_SHA2_256_128
			- Sha_2384192: bool: OFF | ON AUTH_HMAC_SHA2_384_192
			- Sha_2512256: bool: OFF | ON AUTH_HMAC_SHA2_512_256"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Hmac_Md_596'),
			ArgStruct.scalar_bool('Hmac_Shai_96'),
			ArgStruct.scalar_bool('Aes_Xcb_96'),
			ArgStruct.scalar_bool('Sha_2256128'),
			ArgStruct.scalar_bool('Sha_2384192'),
			ArgStruct.scalar_bool('Sha_2512256')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hmac_Md_596: bool = None
			self.Hmac_Shai_96: bool = None
			self.Aes_Xcb_96: bool = None
			self.Sha_2256128: bool = None
			self.Sha_2384192: bool = None
			self.Sha_2512256: bool = None

	def get_integrity(self) -> IntegrityStruct:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:INTegrity \n
		Snippet: value: IntegrityStruct = driver.configure.data.control.epdg.ike.get_integrity() \n
		Selects the supported integrity protection algorithms for the IKEv2 protocol. \n
			:return: structure: for return value, see the help for IntegrityStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:IKE:INTegrity?', self.__class__.IntegrityStruct())

	def set_integrity(self, value: IntegrityStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:INTegrity \n
		Snippet: driver.configure.data.control.epdg.ike.set_integrity(value = IntegrityStruct()) \n
		Selects the supported integrity protection algorithms for the IKEv2 protocol. \n
			:param value: see the help for IntegrityStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:IKE:INTegrity', value)

	# noinspection PyTypeChecker
	class DhGroupStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Dh_Group_1: bool: OFF | ON
			- Dh_Group_2: bool: OFF | ON
			- Dh_Group_5: bool: OFF | ON
			- Dh_Group_14: bool: OFF | ON
			- Dh_Group_15: bool: OFF | ON
			- Dh_Group_16: bool: OFF | ON
			- Dh_Group_17: bool: OFF | ON
			- Dh_Group_18: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Dh_Group_1'),
			ArgStruct.scalar_bool('Dh_Group_2'),
			ArgStruct.scalar_bool('Dh_Group_5'),
			ArgStruct.scalar_bool('Dh_Group_14'),
			ArgStruct.scalar_bool('Dh_Group_15'),
			ArgStruct.scalar_bool('Dh_Group_16'),
			ArgStruct.scalar_bool('Dh_Group_17'),
			ArgStruct.scalar_bool('Dh_Group_18')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dh_Group_1: bool = None
			self.Dh_Group_2: bool = None
			self.Dh_Group_5: bool = None
			self.Dh_Group_14: bool = None
			self.Dh_Group_15: bool = None
			self.Dh_Group_16: bool = None
			self.Dh_Group_17: bool = None
			self.Dh_Group_18: bool = None

	def get_dh_group(self) -> DhGroupStruct:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:DHGRoup \n
		Snippet: value: DhGroupStruct = driver.configure.data.control.epdg.ike.get_dh_group() \n
		Selects the supported Diffie-Hellman groups for the IKEv2 protocol. \n
			:return: structure: for return value, see the help for DhGroupStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:CONTrol:EPDG:IKE:DHGRoup?', self.__class__.DhGroupStruct())

	def set_dh_group(self, value: DhGroupStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:DHGRoup \n
		Snippet: driver.configure.data.control.epdg.ike.set_dh_group(value = DhGroupStruct()) \n
		Selects the supported Diffie-Hellman groups for the IKEv2 protocol. \n
			:param value: see the help for DhGroupStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:EPDG:IKE:DHGRoup', value)

	def get_lifetime(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:LIFetime \n
		Snippet: value: int = driver.configure.data.control.epdg.ike.get_lifetime() \n
		No command help available \n
			:return: ikesa_lifetime: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:IKE:LIFetime?')
		return Conversions.str_to_int(response)

	def set_lifetime(self, ikesa_lifetime: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:LIFetime \n
		Snippet: driver.configure.data.control.epdg.ike.set_lifetime(ikesa_lifetime = 1) \n
		No command help available \n
			:param ikesa_lifetime: No help available
		"""
		param = Conversions.decimal_value_to_str(ikesa_lifetime)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:IKE:LIFetime {param}')

	def clone(self) -> 'Ike':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ike(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
