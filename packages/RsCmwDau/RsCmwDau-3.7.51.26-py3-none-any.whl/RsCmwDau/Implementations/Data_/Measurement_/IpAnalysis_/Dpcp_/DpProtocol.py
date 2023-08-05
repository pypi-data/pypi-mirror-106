from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpProtocol:
	"""DpProtocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpProtocol", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Protocol: List[str]: Used protocol as string
			- Prot_Data: List[float]: Data transported via the protocol, as absolute number Unit: byte
			- Prot_Percent: List[float]: Data transported via the protocol, as percentage of total transported data Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Protocol', DataType.StringList, None, False, True, 1),
			ArgStruct('Prot_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('Prot_Percent', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Protocol: List[str] = None
			self.Prot_Data: List[float] = None
			self.Prot_Percent: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPPRotocol \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.dpcp.dpProtocol.fetch() \n
		Queries the 'Data per Protocol' results. After the reliability indicator, three results are returned for each protocol:
		<Reliability>, {<Protocol>, <ProtData>, <ProtPercent>}protocol 1, {...}protocol 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPPRotocol?', self.__class__.FetchStruct())
