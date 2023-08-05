from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	def set(self, control: bool, ims=repcap.Ims.Default) -> None:
		"""SCPI: SOURce:DATA:CONTrol:IMS<Suffix>:STATe \n
		Snippet: driver.source.data.control.ims.state.set(control = False, ims = repcap.Ims.Default) \n
		Starts or stops the IMS service and the IMS server. \n
			:param control: ON | OFF Switch the service ON or OFF
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.bool_to_str(control)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write_with_opc(f'SOURce:DATA:CONTrol:IMS{ims_cmd_val}:STATe {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.DauState:
		"""SCPI: SOURce:DATA:CONTrol:IMS<Suffix>:STATe \n
		Snippet: value: enums.DauState = driver.source.data.control.ims.state.get(ims = repcap.Ims.Default) \n
		Starts or stops the IMS service and the IMS server. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: state: OFF | ON | PENDing OFF: service switched off ON: service switched on PEND: service activation or deactivation ongoing"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str_with_opc(f'SOURce:DATA:CONTrol:IMS{ims_cmd_val}:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.DauState)
