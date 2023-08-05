from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transmit:
	"""Transmit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("transmit", core, parent)

	# noinspection PyTypeChecker
	class StatusStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Delivery_Status: enums.ReceiveStatusB: No parameter help available
			- Timestamp: int: No parameter help available
			- Message: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Delivery_Status', enums.ReceiveStatusB),
			ArgStruct.scalar_int('Timestamp'),
			ArgStruct.scalar_str('Message')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Delivery_Status: enums.ReceiveStatusB = None
			self.Timestamp: int = None
			self.Message: str = None

	# noinspection PyTypeChecker
	def get_status(self) -> StatusStruct:
		"""SCPI: SENSe:DATA:CONTrol:SUPL:TRANsmit:STATus \n
		Snippet: value: StatusStruct = driver.sense.data.control.supl.transmit.get_status() \n
		No command help available \n
			:return: structure: for return value, see the help for StatusStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:SUPL:TRANsmit:STATus?', self.__class__.StatusStruct())
