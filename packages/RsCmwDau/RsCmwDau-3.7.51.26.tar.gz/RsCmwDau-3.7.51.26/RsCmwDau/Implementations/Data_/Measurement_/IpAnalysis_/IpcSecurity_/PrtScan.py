from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrtScan:
	"""PrtScan commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prtScan", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Port: List[int]: Port number
			- Protocol: List[str]: Layer 4 protocol"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Port', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Protocol', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Port: List[int] = None
			self.Protocol: List[str] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.prtScan.fetch() \n
		Queries the results of a port scan. After the reliability indicator, two parameters are returned for each open port:
		<Reliability>, {<Port>, <Protocol>}1, ..., {<Port>, <Protocol>}n If there is no open port, you get: <Reliability>, INV,
		INV \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan?', self.__class__.FetchStruct())
