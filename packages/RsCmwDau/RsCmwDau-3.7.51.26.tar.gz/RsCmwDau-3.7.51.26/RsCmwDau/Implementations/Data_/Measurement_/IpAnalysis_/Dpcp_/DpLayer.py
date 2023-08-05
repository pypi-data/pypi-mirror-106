from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpLayer:
	"""DpLayer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpLayer", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Layer: List[str]: String with the contents of column 'Layer' (feature, application or protocol)
			- Layer_Data: List[float]: Amount of transported data, as absolute value Unit: byte
			- Layer_Percent: List[float]: Amount of transported data, as percentage of total transported data Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Layer', DataType.StringList, None, False, True, 1),
			ArgStruct('Layer_Data', DataType.FloatList, None, False, True, 1),
			ArgStruct('Layer_Percent', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Layer: List[str] = None
			self.Layer_Data: List[float] = None
			self.Layer_Percent: List[float] = None

	def fetch(self, layer_depth: enums.Layer) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPLayer \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.dpcp.dpLayer.fetch(layer_depth = enums.Layer.APP) \n
		Queries the 'Data per Layer' results. After the reliability indicator, three values are returned for each result table
		row: <Reliability>, {<Layer>, <LayerData>, <LayerPercent>}row 1, {...}row 2, ... \n
			:param layer_depth: FEATure | APP | L7 | L4 | L3 Selects the highest layer at which the packets are analyzed
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(layer_depth, enums.Layer)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPLayer? {param}', self.__class__.FetchStruct())
