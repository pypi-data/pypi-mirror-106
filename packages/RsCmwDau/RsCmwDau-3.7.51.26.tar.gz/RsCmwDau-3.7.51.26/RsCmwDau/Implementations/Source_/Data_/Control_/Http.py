from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Http:
	"""Http commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("http", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Http_.State import State
			self._state = State(self._core, self._base)
		return self._state

	# noinspection PyTypeChecker
	class ReliabilityStruct(StructBase):
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

	def get_reliability(self) -> ReliabilityStruct:
		"""SCPI: SOURce:DATA:CONTrol:HTTP:RELiability \n
		Snippet: value: ReliabilityStruct = driver.source.data.control.http.get_reliability() \n
		No command help available \n
			:return: structure: for return value, see the help for ReliabilityStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:DATA:CONTrol:HTTP:RELiability?', self.__class__.ReliabilityStruct())

	def clone(self) -> 'Http':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Http(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
