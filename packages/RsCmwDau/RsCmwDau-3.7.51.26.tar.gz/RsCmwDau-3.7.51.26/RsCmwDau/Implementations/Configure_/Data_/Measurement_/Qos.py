from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qos:
	"""Qos commands group definition. 18 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qos", core, parent)

	@property
	def filterPy(self):
		"""filterPy commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .Qos_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.QosMode:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:MODE \n
		Snippet: value: enums.QosMode = driver.configure.data.measurement.qos.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:QOS:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.QosMode)

	def set_mode(self, mode: enums.QosMode) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:MODE \n
		Snippet: driver.configure.data.measurement.qos.set_mode(mode = enums.QosMode.PRIO) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.QosMode)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:MODE {param}')

	def clone(self) -> 'Qos':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qos(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
