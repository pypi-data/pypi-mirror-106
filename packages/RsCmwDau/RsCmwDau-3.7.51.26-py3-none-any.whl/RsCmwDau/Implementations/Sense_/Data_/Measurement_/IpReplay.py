from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpReplay:
	"""IpReplay commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipReplay", core, parent)

	@property
	def infoFile(self):
		"""infoFile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_infoFile'):
			from .IpReplay_.InfoFile import InfoFile
			self._infoFile = InfoFile(self._core, self._base)
		return self._infoFile

	@property
	def trafficFile(self):
		"""trafficFile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trafficFile'):
			from .IpReplay_.TrafficFile import TrafficFile
			self._trafficFile = TrafficFile(self._core, self._base)
		return self._trafficFile

	# noinspection PyTypeChecker
	class ProgressStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Filename: List[str]: File name as a string
			- Progress: List[int]: Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct('Filename', DataType.StringList, None, False, True, 1),
			ArgStruct('Progress', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filename: List[str] = None
			self.Progress: List[int] = None

	def get_progress(self) -> ProgressStruct:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPReplay:PROGress \n
		Snippet: value: ProgressStruct = driver.sense.data.measurement.ipReplay.get_progress() \n
		Queries the replay progress for all files in the playlist. The results are returned as follows: {<FileName>,
		<Progress>}file 1, {...}file 2, ..., {...}file n \n
			:return: structure: for return value, see the help for ProgressStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:MEASurement<MeasInstance>:IPReplay:PROGress?', self.__class__.ProgressStruct())

	def clone(self) -> 'IpReplay':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpReplay(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
