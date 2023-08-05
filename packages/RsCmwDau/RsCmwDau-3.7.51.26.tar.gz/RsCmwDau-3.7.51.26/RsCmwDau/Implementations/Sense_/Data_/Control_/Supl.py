from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Supl:
	"""Supl commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("supl", core, parent)

	@property
	def transmit(self):
		"""transmit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmit'):
			from .Supl_.Transmit import Transmit
			self._transmit = Transmit(self._core, self._base)
		return self._transmit

	# noinspection PyTypeChecker
	class ReceiveStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Receive_Status: enums.ReceiveStatusB: No parameter help available
			- Timestamp: int: No parameter help available
			- Message: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Receive_Status', enums.ReceiveStatusB),
			ArgStruct.scalar_int('Timestamp'),
			ArgStruct('Message', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Receive_Status: enums.ReceiveStatusB = None
			self.Timestamp: int = None
			self.Message: List[int] = None

	# noinspection PyTypeChecker
	def get_receive(self) -> ReceiveStruct:
		"""SCPI: SENSe:DATA:CONTrol:SUPL:RECeive \n
		Snippet: value: ReceiveStruct = driver.sense.data.control.supl.get_receive() \n
		No command help available \n
			:return: structure: for return value, see the help for ReceiveStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:SUPL:RECeive?', self.__class__.ReceiveStruct())

	def get_iface(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:SUPL:IFACe \n
		Snippet: value: str = driver.sense.data.control.supl.get_iface() \n
		No command help available \n
			:return: interface_version: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:SUPL:IFACe?')
		return trim_str_response(response)

	def clone(self) -> 'Supl':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Supl(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
