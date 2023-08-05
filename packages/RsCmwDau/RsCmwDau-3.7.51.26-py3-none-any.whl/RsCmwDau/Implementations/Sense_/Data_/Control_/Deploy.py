from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Deploy:
	"""Deploy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("deploy", core, parent)

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Msg_Type: int: No parameter help available
			- Msg_Code: int: No parameter help available
			- Msg_String: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Msg_Type'),
			ArgStruct.scalar_int('Msg_Code'),
			ArgStruct.scalar_str('Msg_String')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Msg_Type: int = None
			self.Msg_Code: int = None
			self.Msg_String: str = None

	def get_result(self) -> ResultStruct:
		"""SCPI: SENSe:DATA:CONTrol:DEPLoy:RESult \n
		Snippet: value: ResultStruct = driver.sense.data.control.deploy.get_result() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:DEPLoy:RESult?', self.__class__.ResultStruct())
