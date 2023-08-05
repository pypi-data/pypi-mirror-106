from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpApplic:
	"""DpApplic commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpApplic", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- App: List[str]: String with the contents of column 'Application' (application or protocol)
			- App_Data: List[float]: Amount of transported data, as absolute value Unit: byte
			- App_Percent: List[float]: Amount of transported data, as percentage of total transported data Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('App', DataType.StringList, None, False, True, 1),
			ArgStruct('App_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('App_Percent', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.App: List[str] = None
			self.App_Data: List[float] = None
			self.App_Percent: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPAPplic \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.dpcp.dpApplic.fetch() \n
		Queries the 'Data per Application' results of the current layer. To navigate between the layers, see method RsCmwDau.
		Configure.Data.Measurement.IpAnalysis.Dpcp.DpApplic.app. After the reliability indicator, three values are returned for
		each result table row: <Reliability>, {<App>, <AppData>, <AppPercent>}row 1, {...}row 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPAPplic?', self.__class__.FetchStruct())
