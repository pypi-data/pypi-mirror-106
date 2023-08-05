from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EcpFormats:
	"""EcpFormats commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ecpFormats", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ecp_Format_Id: List[str]: Elliptic curve point format ID as hexadecimal value
			- Ecp_Format_Name: List[str]: Elliptic curve point format name as string"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Ecp_Format_Id', DataType.RawStringList, None, False, True, 1),
			ArgStruct('Ecp_Format_Name', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ecp_Format_Id: List[str] = None
			self.Ecp_Format_Name: List[str] = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:NEGotiated:ECPFormats \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.handshake.negotiated.ecpFormats.fetch(flow_id = 1) \n
		Queries information about the elliptic curve point formats negotiated for a specific connection. After the reliability
		indicator, two results are returned for each format: <Reliability>, {<ECPFormatID>, <ECPFormatName>}Format 1, {...}Format
		2, ... \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:NEGotiated:ECPFormats? {param}', self.__class__.FetchStruct())
