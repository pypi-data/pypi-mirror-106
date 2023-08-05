from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PerdTx:
	"""PerdTx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("perdTx", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Per_Up: int: No parameter help available
			- Per_Down: int: No parameter help available
			- Dtx_Up: int: Discontinuous transmission rate in the uplink Range: 0 % to 100 %, Unit: %
			- Dtx_Down: int: Discontinuous transmission rate in the downlink Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Per_Up'),
			ArgStruct.scalar_int('Per_Down'),
			ArgStruct.scalar_int('Dtx_Up'),
			ArgStruct.scalar_int('Dtx_Down')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Per_Up: int = None
			self.Per_Down: int = None
			self.Dtx_Up: int = None
			self.Dtx_Down: int = None

	def get(self, con_id: float) -> GetStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:VOIMs:PERDtx \n
		Snippet: value: GetStruct = driver.sense.data.measurement.ipAnalysis.voIms.perdTx.get(con_id = 1.0) \n
		Queries the packets measurement results for a selected voice over IMS call. To get a list of all calls and their IDs, use
		method RsCmwDau.Data.Measurement.IpAnalysis.VoIms.All.fetch. \n
			:param con_id: Selects the call for which the results are queried
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(con_id)
		return self._core.io.query_struct(f'SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:VOIMs:PERDtx? {param}', self.__class__.GetStruct())
