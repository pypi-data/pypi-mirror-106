from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Negotiated:
	"""Negotiated commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("negotiated", core, parent)

	@property
	def ecpFormats(self):
		"""ecpFormats commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecpFormats'):
			from .Negotiated_.EcpFormats import EcpFormats
			self._ecpFormats = EcpFormats(self._core, self._base)
		return self._ecpFormats

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Version_Id: str: Protocol version ID as hexadecimal value
			- Version_Name: str: Protocol version as string
			- Cipher_Suite_Id: str: Cipher suite ID as hexadecimal value
			- Cipher_Suite_Name: str: Cipher suite name as string
			- Compression_Id: str: Compression method ID as hexadecimal value
			- Compression_Name: str: Compression method name as string
			- Register_Type: enums.RegisterType: IANA | OID Type of the register used for the signature hash algorithm pair If the value is IANA, the fields SignatureAlgoHashID and SignaHashAlgoSignID are filled with the ID values. If the value is OID, the field OID is filled with a single combined ID value for the signature hash algorithm pair. In both cases, the fields SignatureAlgoHashName and SignaHashAlgoSignName are filled with the names as strings.
			- Oid: str: Signature hash algorithm ID as string
			- Sign_Alg_Hash_Id: str: Hash algorithm ID as hexadecimal value
			- Sign_Alg_Hash_Name: str: Hash algorithm name as string
			- Sign_Alg_Sign_Id: str: Signature algorithm ID as hexadecimal value
			- Sign_Alg_Sign_Name: str: Signature algorithm name as string
			- Ecurve_Id: str: Elliptic curve ID as hexadecimal value
			- Ec_Name: str: Elliptic curve name as string
			- Ec_Type_Id: str: Elliptic curve type ID as hexadecimal value
			- Ec_Type_Name: str: Elliptic curve type name as string
			- Ecp_Format_Id: str: Elliptic curve point format ID as hexadecimal value - no longer supported
			- Ecp_Format_Name: str: Elliptic curve point format name as string - no longer supported
			- Sign_Length: int: Length of the server signature in bits
			- Public_Length: int: Length of the public key of the server in bits"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Version_Id'),
			ArgStruct.scalar_str('Version_Name'),
			ArgStruct.scalar_raw_str('Cipher_Suite_Id'),
			ArgStruct.scalar_str('Cipher_Suite_Name'),
			ArgStruct.scalar_raw_str('Compression_Id'),
			ArgStruct.scalar_str('Compression_Name'),
			ArgStruct.scalar_enum('Register_Type', enums.RegisterType),
			ArgStruct.scalar_str('Oid'),
			ArgStruct.scalar_raw_str('Sign_Alg_Hash_Id'),
			ArgStruct.scalar_str('Sign_Alg_Hash_Name'),
			ArgStruct.scalar_raw_str('Sign_Alg_Sign_Id'),
			ArgStruct.scalar_str('Sign_Alg_Sign_Name'),
			ArgStruct.scalar_raw_str('Ecurve_Id'),
			ArgStruct.scalar_str('Ec_Name'),
			ArgStruct.scalar_raw_str('Ec_Type_Id'),
			ArgStruct.scalar_str('Ec_Type_Name'),
			ArgStruct.scalar_raw_str('Ecp_Format_Id'),
			ArgStruct.scalar_str('Ecp_Format_Name'),
			ArgStruct.scalar_int('Sign_Length'),
			ArgStruct.scalar_int('Public_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Version_Id: str = None
			self.Version_Name: str = None
			self.Cipher_Suite_Id: str = None
			self.Cipher_Suite_Name: str = None
			self.Compression_Id: str = None
			self.Compression_Name: str = None
			self.Register_Type: enums.RegisterType = None
			self.Oid: str = None
			self.Sign_Alg_Hash_Id: str = None
			self.Sign_Alg_Hash_Name: str = None
			self.Sign_Alg_Sign_Id: str = None
			self.Sign_Alg_Sign_Name: str = None
			self.Ecurve_Id: str = None
			self.Ec_Name: str = None
			self.Ec_Type_Id: str = None
			self.Ec_Type_Name: str = None
			self.Ecp_Format_Id: str = None
			self.Ecp_Format_Name: str = None
			self.Sign_Length: int = None
			self.Public_Length: int = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:NEGotiated \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.handshake.negotiated.fetch(flow_id = 1) \n
		Queries the negotiated handshake results for a specific connection. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:NEGotiated? {param}', self.__class__.FetchStruct())

	def clone(self) -> 'Negotiated':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Negotiated(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
