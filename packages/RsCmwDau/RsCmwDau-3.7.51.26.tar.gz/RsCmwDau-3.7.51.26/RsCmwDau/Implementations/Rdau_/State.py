from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	def set(self, control: bool, serial_number: int) -> None:
		"""SCPI: RDAU:STATe \n
		Snippet: driver.rdau.state.set(control = False, serial_number = 1) \n
		No command help available \n
			:param control: No help available
			:param serial_number: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('control', control, DataType.Boolean), ArgSingle('serial_number', serial_number, DataType.Integer))
		self._core.io.write_with_opc(f'RDAU:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- State: enums.DauState: No parameter help available
			- Serial_Number: int: No parameter help available
			- Ip_Address: str: No parameter help available
			- Ref_Count: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('State', enums.DauState),
			ArgStruct.scalar_int('Serial_Number'),
			ArgStruct.scalar_str('Ip_Address'),
			ArgStruct.scalar_int('Ref_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.State: enums.DauState = None
			self.Serial_Number: int = None
			self.Ip_Address: str = None
			self.Ref_Count: int = None

	def get(self) -> GetStruct:
		"""SCPI: RDAU:STATe \n
		Snippet: value: GetStruct = driver.rdau.state.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct_with_opc(f'RDAU:STATe?', self.__class__.GetStruct())
