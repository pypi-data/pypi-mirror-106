from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 6 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def ran(self):
		"""ran commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ran'):
			from .Throughput_.Ran import Ran
			self._ran = Ran(self._core, self._base)
		return self._ran

	def get_mcount(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:MCOunt \n
		Snippet: value: int = driver.configure.data.measurement.throughput.get_mcount() \n
		Specifies the total number of overall throughput results to be measured. \n
			:return: max_count: Range: 5 to 3600
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:MCOunt?')
		return Conversions.str_to_int(response)

	def set_mcount(self, max_count: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:MCOunt \n
		Snippet: driver.configure.data.measurement.throughput.set_mcount(max_count = 1) \n
		Specifies the total number of overall throughput results to be measured. \n
			:param max_count: Range: 5 to 3600
		"""
		param = Conversions.decimal_value_to_str(max_count)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:MCOunt {param}')

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
