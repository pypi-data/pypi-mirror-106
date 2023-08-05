from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	def set(self, control: bool) -> None:
		"""SCPI: SOURce:DATA:CONTrol:STATe \n
		Snippet: driver.source.data.control.state.set(control = False) \n
		Switches the DAU on or off. These actions are irrelevant for normal operation of the DAU. For troubleshooting, a reboot
		of the DAU can be initiated by switching if off and on again. \n
			:param control: ON | OFF Switch DAU ON or OFF
		"""
		param = Conversions.bool_to_str(control)
		self._core.io.write_with_opc(f'SOURce:DATA:CONTrol:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DauState:
		"""SCPI: SOURce:DATA:CONTrol:STATe \n
		Snippet: value: enums.DauState = driver.source.data.control.state.get() \n
		Switches the DAU on or off. These actions are irrelevant for normal operation of the DAU. For troubleshooting, a reboot
		of the DAU can be initiated by switching if off and on again. \n
			:return: dau_state: OFF | PENDing | ON OFF: DAU switched off PEND: DAU has been switched on and is booting ON: DAU switched on and ready for operation"""
		response = self._core.io.query_str_with_opc(f'SOURce:DATA:CONTrol:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.DauState)
