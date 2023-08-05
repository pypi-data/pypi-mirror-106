from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpConnection:
	"""DpConnection commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpConnection", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Rem_Destination: List[str]: IP address of the remote destination as string
			- Conn_Data: List[float]: Data transported via the connection, as absolute number Unit: byte
			- Conn_Percent: List[float]: Data transported via the connection, as percentage of total transported data Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Rem_Destination', DataType.StringList, None, False, True, 1),
			ArgStruct('Conn_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('Conn_Percent', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rem_Destination: List[str] = None
			self.Conn_Data: List[float] = None
			self.Conn_Percent: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPConnection \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.dpcp.dpConnection.fetch() \n
		Queries the 'Data per Connection' results. After the reliability indicator, three results are returned for each
		connection: <Reliability>, {<RemDestination>, <ConnData>, <ConnPercent>}conn 1, {...}conn 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPConnection?', self.__class__.FetchStruct())
