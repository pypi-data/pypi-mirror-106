from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpConnect:
	"""IpConnect commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipConnect", core, parent)

	@property
	def aflowId(self):
		"""aflowId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aflowId'):
			from .IpConnect_.AflowId import AflowId
			self._aflowId = AflowId(self._core, self._base)
		return self._aflowId

	@property
	def flowId(self):
		"""flowId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_flowId'):
			from .IpConnect_.FlowId import FlowId
			self._flowId = FlowId(self._core, self._base)
		return self._flowId

	# noinspection PyTypeChecker
	class StatisticsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- No_Of_Conn: int: Total number of connections
			- No_Of_Open_Conn: int: Number of open connections
			- No_Of_Closed_Conn: int: Number of closed connections
			- Open_Tcpc: int: Number of open TCP connections
			- Closed_Tcpc: int: Number of closed TCP connections
			- Open_Udpc: int: Number of open UDP connections
			- Closed_Udpc: int: Number of closed UDP connections"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Of_Conn'),
			ArgStruct.scalar_int('No_Of_Open_Conn'),
			ArgStruct.scalar_int('No_Of_Closed_Conn'),
			ArgStruct.scalar_int('Open_Tcpc'),
			ArgStruct.scalar_int('Closed_Tcpc'),
			ArgStruct.scalar_int('Open_Udpc'),
			ArgStruct.scalar_int('Closed_Udpc')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Of_Conn: int = None
			self.No_Of_Open_Conn: int = None
			self.No_Of_Closed_Conn: int = None
			self.Open_Tcpc: int = None
			self.Closed_Tcpc: int = None
			self.Open_Udpc: int = None
			self.Closed_Udpc: int = None

	def get_statistics(self) -> StatisticsStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPConnect:STATistics \n
		Snippet: value: StatisticsStruct = driver.sense.data.measurement.ipAnalysis.ipConnect.get_statistics() \n
		Queries the statistical information provided by the 'IP Connectivity' view. \n
			:return: structure: for return value, see the help for StatisticsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPConnect:STATistics?', self.__class__.StatisticsStruct())

	def clone(self) -> 'IpConnect':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpConnect(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
