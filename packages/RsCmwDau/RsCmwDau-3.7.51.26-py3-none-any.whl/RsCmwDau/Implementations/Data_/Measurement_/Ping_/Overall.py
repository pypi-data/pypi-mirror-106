from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Overall:
	"""Overall commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("overall", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Min_Ping: float: Minimum ping latency Range: 0 s to 10 s, Unit: s
			- Max_Ping: float: Maximum ping latency Range: 0 s to 10 s, Unit: s
			- Average_Ping: float: Average ping latency Range: 0 s to 10 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Min_Ping'),
			ArgStruct.scalar_float('Max_Ping'),
			ArgStruct.scalar_float('Average_Ping')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Min_Ping: float = None
			self.Max_Ping: float = None
			self.Average_Ping: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:PING:OVERall \n
		Snippet: value: FetchStruct = driver.data.measurement.ping.overall.fetch() \n
		Query the statistical ping results over all ping requests. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:PING:OVERall?', self.__class__.FetchStruct())
