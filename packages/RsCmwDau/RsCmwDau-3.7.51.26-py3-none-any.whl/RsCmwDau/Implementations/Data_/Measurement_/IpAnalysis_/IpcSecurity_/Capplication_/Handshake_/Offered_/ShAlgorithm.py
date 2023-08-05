from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ShAlgorithm:
	"""ShAlgorithm commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("shAlgorithm", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Algorithm_Hash_Id: List[str]: Hash algorithm ID as hexadecimal value
			- Algorithm_Sign_Id: List[str]: Signature algorithm ID as hexadecimal value
			- Algo_Hash_Name: List[str]: Hash algorithm name as string
			- Algo_Sign_Name: List[str]: Signature algorithm name as string"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Algorithm_Hash_Id', DataType.RawStringList, None, False, True, 1),
			ArgStruct('Algorithm_Sign_Id', DataType.RawStringList, None, False, True, 1),
			ArgStruct('Algo_Hash_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Algo_Sign_Name', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Algorithm_Hash_Id: List[str] = None
			self.Algorithm_Sign_Id: List[str] = None
			self.Algo_Hash_Name: List[str] = None
			self.Algo_Sign_Name: List[str] = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:SHALgorithm \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.handshake.offered.shAlgorithm.fetch(flow_id = 1) \n
		Queries information about the hash algorithms and signature algorithms offered during the handshake for a specific
		connection. After the reliability indicator, four results are returned for each pair of algorithms: <Reliability>,
		{<AlgorithmHashID>, <AlgorithmSignID>, <AlgoHashName>, <AlgoSignName>}1, {...}2, ... \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:SHALgorithm? {param}', self.__class__.FetchStruct())
