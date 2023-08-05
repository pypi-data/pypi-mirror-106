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
		"""SCPI: SOURce:DATA:CONTrol:EPDG:STATe \n
		Snippet: driver.source.data.control.epdg.state.set(control = False) \n
		Starts or stops the ePDG service. \n
			:param control: ON | OFF Switch the service ON or OFF
		"""
		param = Conversions.bool_to_str(control)
		self._core.io.write_with_opc(f'SOURce:DATA:CONTrol:EPDG:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DauState:
		"""SCPI: SOURce:DATA:CONTrol:EPDG:STATe \n
		Snippet: value: enums.DauState = driver.source.data.control.epdg.state.get() \n
		Starts or stops the ePDG service. \n
			:return: state: OFF | ON | PENDing OFF: service switched off ON: service switched on PEND: service activation or deactivation ongoing"""
		response = self._core.io.query_str_with_opc(f'SOURce:DATA:CONTrol:EPDG:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.DauState)
