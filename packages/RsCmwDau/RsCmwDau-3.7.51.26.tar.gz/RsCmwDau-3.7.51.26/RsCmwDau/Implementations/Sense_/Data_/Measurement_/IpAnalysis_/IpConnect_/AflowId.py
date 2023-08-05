from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AflowId:
	"""AflowId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aflowId", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- App: str: Application name as string
			- Feature: str: Feature name as string (for example: audio, video, SMS)"""
		__meta_args_list = [
			ArgStruct.scalar_str('App'),
			ArgStruct.scalar_str('Feature')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.App: str = None
			self.Feature: str = None

	def get(self, flow_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPConnect:AFLowid \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.ipConnect.aflowId.get(flow_id = 1.0) \n
		Queries 'IP Connectivity' results for a specific connection, selected via its flow ID. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:AFLowid? {param}', self.__class__.GetStruct())
