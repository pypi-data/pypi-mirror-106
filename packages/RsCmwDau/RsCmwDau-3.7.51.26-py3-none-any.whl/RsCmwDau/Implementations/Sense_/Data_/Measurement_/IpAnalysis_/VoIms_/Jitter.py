from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Jitter:
	"""Jitter commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("jitter", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Jitter_Max_Up: float: Maximum jitter in the uplink Unit: s
			- Jitter_Avg_Up: float: Average jitter in the uplink Unit: s
			- Jitter_Min_Up: float: Minimum jitter in the uplink Unit: s
			- Jitter_Max_Down: float: Maximum jitter in the downlink Unit: s
			- Jitter_Avg_Down: float: Average jitter in the downlink Unit: s
			- Jitter_Min_Down: float: Minimum jitter in the downlink Unit: s
			- Jitter_Curr_Up: float: Current jitter in the uplink Unit: s
			- Jitter_Curr_Down: float: Current jitter in the downlink Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Jitter_Max_Up'),
			ArgStruct.scalar_float('Jitter_Avg_Up'),
			ArgStruct.scalar_float('Jitter_Min_Up'),
			ArgStruct.scalar_float('Jitter_Max_Down'),
			ArgStruct.scalar_float('Jitter_Avg_Down'),
			ArgStruct.scalar_float('Jitter_Min_Down'),
			ArgStruct.scalar_float('Jitter_Curr_Up'),
			ArgStruct.scalar_float('Jitter_Curr_Down')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Jitter_Max_Up: float = None
			self.Jitter_Avg_Up: float = None
			self.Jitter_Min_Up: float = None
			self.Jitter_Max_Down: float = None
			self.Jitter_Avg_Down: float = None
			self.Jitter_Min_Down: float = None
			self.Jitter_Curr_Up: float = None
			self.Jitter_Curr_Down: float = None

	def get(self, con_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:VOIMs:JITTer \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.voIms.jitter.get(con_id = 1.0) \n
		Queries the jitter results for a selected voice over IMS call. To get a list of all calls and their IDs, use method
		RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch. \n
			:param con_id: Selects the call for which the results are queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(con_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:VOIMs:JITTer? {param}', self.__class__.GetStruct())
