from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlink:
	"""Dlink commands group definition. 2 total commands, 0 Sub-groups, 2 group commands
	Repeated Capability: Dlink, default value after init: Dlink.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dlink", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_dlink_get', 'repcap_dlink_set', repcap.Dlink.Ix1)

	def repcap_dlink_set(self, enum_value: repcap.Dlink) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Dlink.Default
		Default value after init: Dlink.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_dlink_get(self) -> repcap.Dlink:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Th_Curr_Dlink: float: Current throughput Unit: bit/s
			- Th_Min_Dlink: float: Minimum throughput Unit: bit/s
			- Th_Max_Dlink: float: Maximum throughput Unit: bit/s
			- Th_Avg_Dlink: float: Average throughput Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Th_Curr_Dlink'),
			ArgStruct.scalar_float('Th_Min_Dlink'),
			ArgStruct.scalar_float('Th_Max_Dlink'),
			ArgStruct.scalar_float('Th_Avg_Dlink')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Th_Curr_Dlink: float = None
			self.Th_Min_Dlink: float = None
			self.Th_Max_Dlink: float = None
			self.Th_Avg_Dlink: float = None

	def read(self, dlink=repcap.Dlink.Default) -> ResultData:
		"""SCPI: READ:DATA:MEASurement<Instance>:THRoughput:RAN:DLINk<Index> \n
		Snippet: value: ResultData = driver.data.measurement.throughput.ran.dlink.read(dlink = repcap.Dlink.Default) \n
		Query the statistical results of the throughput measurement for RAN slot number <Index> in downlink direction. \n
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		return self._core.io.query_struct(f'READ:DATA:MEASurement<MeasInstance>:THRoughput:RAN:DLINk{dlink_cmd_val}?', self.__class__.ResultData())

	def fetch(self, dlink=repcap.Dlink.Default) -> ResultData:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:THRoughput:RAN:DLINk<Index> \n
		Snippet: value: ResultData = driver.data.measurement.throughput.ran.dlink.fetch(dlink = repcap.Dlink.Default) \n
		Query the statistical results of the throughput measurement for RAN slot number <Index> in downlink direction. \n
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		return self._core.io.query_struct(f'FETCh:DATA:MEASurement<MeasInstance>:THRoughput:RAN:DLINk{dlink_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'Dlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
