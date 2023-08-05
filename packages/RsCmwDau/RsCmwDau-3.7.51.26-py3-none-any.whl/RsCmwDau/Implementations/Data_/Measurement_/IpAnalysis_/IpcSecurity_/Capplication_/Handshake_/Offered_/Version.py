from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Version:
	"""Version commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("version", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Version_String: str: Protocol version as string
			- Version_Id: str: Protocol version ID as hexadecimal value"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Version_String'),
			ArgStruct.scalar_raw_str('Version_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Version_String: str = None
			self.Version_Id: str = None

	def fetch(self, flow_id: int) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:VERSion \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.ipcSecurity.capplication.handshake.offered.version.fetch(flow_id = 1) \n
		Queries the protocol version offered during the handshake for a specific connection. \n
			:param flow_id: Selects the connection for which information is queried
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = Conversions.decimal_value_to_str(flow_id)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:CAPPlication:HANDshake:OFFered:VERSion? {param}', self.__class__.FetchStruct())
