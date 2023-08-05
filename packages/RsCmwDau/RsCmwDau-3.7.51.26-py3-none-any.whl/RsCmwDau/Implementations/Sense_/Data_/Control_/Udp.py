from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Udp:
	"""Udp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udp", core, parent)

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Result: enums.Result: No parameter help available
			- Timestamp: int: No parameter help available
			- Message: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Result', enums.Result),
			ArgStruct.scalar_int('Timestamp'),
			ArgStruct.scalar_str('Message')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Result: enums.Result = None
			self.Timestamp: int = None
			self.Message: str = None

	# noinspection PyTypeChecker
	def get_result(self) -> ResultStruct:
		"""SCPI: SENSe:DATA:CONTrol:UDP:RESult \n
		Snippet: value: ResultStruct = driver.sense.data.control.udp.get_result() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:UDP:RESult?', self.__class__.ResultStruct())

	# noinspection PyTypeChecker
	class ReceiveStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Receive_Status: enums.ReceiveStatusA: No parameter help available
			- Timestamp: int: No parameter help available
			- Src_Addr: str: No parameter help available
			- Src_Port: int: No parameter help available
			- Dst_Addr: str: No parameter help available
			- Dst_Port: int: No parameter help available
			- Packet: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Receive_Status', enums.ReceiveStatusA),
			ArgStruct.scalar_int('Timestamp'),
			ArgStruct.scalar_str('Src_Addr'),
			ArgStruct.scalar_int('Src_Port'),
			ArgStruct.scalar_str('Dst_Addr'),
			ArgStruct.scalar_int('Dst_Port'),
			ArgStruct('Packet', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Receive_Status: enums.ReceiveStatusA = None
			self.Timestamp: int = None
			self.Src_Addr: str = None
			self.Src_Port: int = None
			self.Dst_Addr: str = None
			self.Dst_Port: int = None
			self.Packet: List[int] = None

	# noinspection PyTypeChecker
	def get_receive(self) -> ReceiveStruct:
		"""SCPI: SENSe:DATA:CONTrol:UDP:RECeive \n
		Snippet: value: ReceiveStruct = driver.sense.data.control.udp.get_receive() \n
		No command help available \n
			:return: structure: for return value, see the help for ReceiveStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:UDP:RECeive?', self.__class__.ReceiveStruct())
