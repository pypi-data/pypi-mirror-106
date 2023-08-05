from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Search:
	"""Search commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("search", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Keyword: List[str]: Found keyword as string
			- Count: List[int]: How often the keyword was found
			- Dst_Ip: List[str]: IP address of the destination as string
			- Fqdn: List[str]: FQDN of the destination as string
			- Application: List[str]: Application using the connection, as string
			- Direction: List[enums.DirectionA]: DL | UL | UNKN Direction of the transmission - downlink, uplink or unknown"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Keyword', DataType.StringList, None, False, True, 1),
			ArgStruct('Count', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Dst_Ip', DataType.StringList, None, False, True, 1),
			ArgStruct('Fqdn', DataType.StringList, None, False, True, 1),
			ArgStruct('Application', DataType.StringList, None, False, True, 1),
			ArgStruct('Direction', DataType.EnumList, enums.DirectionA, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Keyword: List[str] = None
			self.Count: List[int] = None
			self.Dst_Ip: List[str] = None
			self.Fqdn: List[str] = None
			self.Application: List[str] = None
			self.Direction: List[enums.DirectionA] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:KYWord:SEARch \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.kyword.search.fetch() \n
		Queries the keyword search results. After the reliability indicator, six results are returned for each found keyword:
		<Reliability>, {<Keyword>, <Count>, <DstIP>, <FQDN>, <Application>, <Direction>}1, {...}2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:KYWord:SEARch?', self.__class__.FetchStruct())
