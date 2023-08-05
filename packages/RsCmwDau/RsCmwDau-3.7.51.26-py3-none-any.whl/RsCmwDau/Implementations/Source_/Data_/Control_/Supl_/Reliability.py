from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reliability:
	"""Reliability commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reliability", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Reliability: int: No parameter help available
			- Reliability_Msg: str: No parameter help available
			- Reliability_Add_Info: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Reliability_Msg'),
			ArgStruct.scalar_str('Reliability_Add_Info')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Reliability_Msg: str = None
			self.Reliability_Add_Info: str = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:DATA:CONTrol:SUPL:RELiability:ALL \n
		Snippet: value: AllStruct = driver.source.data.control.supl.reliability.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:DATA:CONTrol:SUPL:RELiability:ALL?', self.__class__.AllStruct())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Reliability_Msg: str: No parameter help available
			- Reliability_Add_Info: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Reliability_Msg'),
			ArgStruct.scalar_str('Reliability_Add_Info')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Reliability_Msg: str = None
			self.Reliability_Add_Info: str = None

	def get(self, details: str = None) -> GetStruct:
		"""SCPI: SOURce:DATA:CONTrol:SUPL:RELiability \n
		Snippet: value: GetStruct = driver.source.data.control.supl.reliability.get(details = '1') \n
		No command help available \n
			:param details: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('details', details, DataType.String, True))
		return self._core.io.query_struct(f'SOURce:DATA:CONTrol:SUPL:RELiability? {param}'.rstrip(), self.__class__.GetStruct())
