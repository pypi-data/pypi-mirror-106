from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Certificate:
	"""Certificate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("certificate", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Subject_Certificate_Name: List[str]: No parameter help available
			- Subject_Organization: List[str]: No parameter help available
			- Subject_Oraganizational_Unit: List[str]: No parameter help available
			- Subject_Country_Name: List[str]: No parameter help available
			- Public_Key_Algorithm: List[str]: No parameter help available
			- Public_Key_Length: List[int]: No parameter help available
			- Sign_Algo_Id: List[str]: No parameter help available
			- Sign_Algo_Name: List[str]: No parameter help available
			- Signature_Key_Length: List[int]: No parameter help available
			- Validitynotbefore: List[str]: No parameter help available
			- Validitynot_After: List[str]: No parameter help available
			- Revocation_Method: List[str]: No parameter help available
			- Revocation_Status: List[str]: No parameter help available
			- Perform_Date_Time: List[str]: No parameter help available
			- Self_Signed: List[bool]: No parameter help available
			- Trust_Store: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Subject_Certificate_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Subject_Organization', DataType.StringList, None, False, True, 1),
			ArgStruct('Subject_Oraganizational_Unit', DataType.StringList, None, False, True, 1),
			ArgStruct('Subject_Country_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Public_Key_Algorithm', DataType.StringList, None, False, True, 1),
			ArgStruct('Public_Key_Length', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Sign_Algo_Id', DataType.RawStringList, None, False, True, 1),
			ArgStruct('Sign_Algo_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Signature_Key_Length', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Validitynotbefore', DataType.StringList, None, False, True, 1),
			ArgStruct('Validitynot_After', DataType.StringList, None, False, True, 1),
			ArgStruct('Revocation_Method', DataType.StringList, None, False, True, 1),
			ArgStruct('Revocation_Status', DataType.StringList, None, False, True, 1),
			ArgStruct('Perform_Date_Time', DataType.StringList, None, False, True, 1),
			ArgStruct('Self_Signed', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Trust_Store', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Subject_Certificate_Name: List[str] = None
			self.Subject_Organization: List[str] = None
			self.Subject_Oraganizational_Unit: List[str] = None
			self.Subject_Country_Name: List[str] = None
			self.Public_Key_Algorithm: List[str] = None
			self.Public_Key_Length: List[int] = None
			self.Sign_Algo_Id: List[str] = None
			self.Sign_Algo_Name: List[str] = None
			self.Signature_Key_Length: List[int] = None
			self.Validitynotbefore: List[str] = None
			self.Validitynot_After: List[str] = None
			self.Revocation_Method: List[str] = None
			self.Revocation_Status: List[str] = None
			self.Perform_Date_Time: List[str] = None
			self.Self_Signed: List[bool] = None
			self.Trust_Store: List[str] = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:CERTificate \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.certificate.fetch(flow_id = 1) \n
		No command help available \n
			:param flow_id: No help available
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:CERTificate? {param}', self.__class__.FetchStruct())
