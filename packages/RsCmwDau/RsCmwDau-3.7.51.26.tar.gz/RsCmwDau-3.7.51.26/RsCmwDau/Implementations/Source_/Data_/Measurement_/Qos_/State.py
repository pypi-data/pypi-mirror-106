from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	def set(self, control: bool) -> None:
		"""SCPI: SOURce:DATA:MEASurement<Instance>:QOS:STATe \n
		Snippet: driver.source.data.measurement.qos.state.set(control = False) \n
		Switches the QoS feature on or off. To enable QoS profiles, see method RsCmwDau.Configure.Data.Measurement.Qos.FilterPy.
		Enable.set. \n
			:param control: ON | OFF Switch the QoS feature on or off
		"""
		param = Conversions.bool_to_str(control)
		self._core.io.write_with_opc(f'SOURce:DATA:MEASurement<MeasInstance>:QOS:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DauState:
		"""SCPI: SOURce:DATA:MEASurement<Instance>:QOS:STATe \n
		Snippet: value: enums.DauState = driver.source.data.measurement.qos.state.get() \n
		Switches the QoS feature on or off. To enable QoS profiles, see method RsCmwDau.Configure.Data.Measurement.Qos.FilterPy.
		Enable.set. \n
			:return: ni_state: OFF | PENDing | ON OFF: QoS feature switched off PEND: switching on/off is ongoing ON: QoS feature switched on"""
		response = self._core.io.query_str_with_opc(f'SOURce:DATA:MEASurement<MeasInstance>:QOS:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.DauState)
