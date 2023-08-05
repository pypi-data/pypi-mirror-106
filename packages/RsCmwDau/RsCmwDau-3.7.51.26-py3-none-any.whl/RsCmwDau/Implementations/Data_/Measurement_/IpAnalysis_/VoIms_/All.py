from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Con_Id: List[int]: Call ID
			- Flows_Ids: List[str]: String containing a comma-separated list of the flow IDs related to the call (example '1,2' or '128')
			- Type_Py: List[enums.AvTypeC]: AUDio | VIDeo | EMER | UNK Call type audio, video, emergency or unknown
			- Origin: List[enums.Origin]: MT | MO | UNK MT: mobile-terminating call MO: mobile-originating call UNK: unknown
			- State: List[enums.VoimState]: RING | EST | REL | HOLD | UNK RING: DUT ringing EST: call established REL: call released HOLD: call on hold UNK: unknown
			- Start_Time: List[str]: String indicating the time when the call setup was initiated
			- Setup_Time: List[float]: Duration of the call setup procedure Unit: s
			- Duration: List[float]: Duration of the call Unit: s
			- User_From: List[str]: String with the user ID or phone number of the calling party
			- User_To: List[str]: String with the user ID or phone number of the called party"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Con_Id', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Flows_Ids', DataType.StringList, None, False, True, 1),
			ArgStruct('Type_Py', DataType.EnumList, enums.AvTypeC, False, True, 1),
			ArgStruct('Origin', DataType.EnumList, enums.Origin, False, True, 1),
			ArgStruct('State', DataType.EnumList, enums.VoimState, False, True, 1),
			ArgStruct('Start_Time', DataType.StringList, None, False, True, 1),
			ArgStruct('Setup_Time', DataType.FloatList, None, False, True, 1),
			ArgStruct('Duration', DataType.FloatList, None, False, True, 1),
			ArgStruct('User_From', DataType.StringList, None, False, True, 1),
			ArgStruct('User_To', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Con_Id: List[int] = None
			self.Flows_Ids: List[str] = None
			self.Type_Py: List[enums.AvTypeC] = None
			self.Origin: List[enums.Origin] = None
			self.State: List[enums.VoimState] = None
			self.Start_Time: List[str] = None
			self.Setup_Time: List[float] = None
			self.Duration: List[float] = None
			self.User_From: List[str] = None
			self.User_To: List[str] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPANalysis:VOIMs:ALL \n
		Snippet: value: FetchStruct = driver.data.measurement.ipAnalysis.voIms.all.fetch() \n
		Queries the call table in the upper part of the 'Voice Over IMS' view. The results are returned row by row (call by call)
		: <Reliability>, {<ConID>, ..., <UserTo>}call 1, {...}call 2, ..., {...}call n \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:IPANalysis:VOIMs:ALL?', self.__class__.FetchStruct())
