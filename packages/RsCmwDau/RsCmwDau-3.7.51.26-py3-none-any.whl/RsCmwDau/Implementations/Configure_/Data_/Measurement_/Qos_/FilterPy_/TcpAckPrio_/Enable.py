from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:TCPackprio:ENABle \n
		Snippet: driver.configure.data.measurement.qos.filterPy.tcpAckPrio.enable.set(enable = False, fltr = repcap.Fltr.Default) \n
		Enables the prioritization of TCP acknowledgments over other packets. \n
			:param enable: OFF | ON
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.bool_to_str(enable)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:TCPackprio:ENABle {param}')

	def get(self, fltr=repcap.Fltr.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:TCPackprio:ENABle \n
		Snippet: value: bool = driver.configure.data.measurement.qos.filterPy.tcpAckPrio.enable.get(fltr = repcap.Fltr.Default) \n
		Enables the prioritization of TCP acknowledgments over other packets. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: enable: OFF | ON"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:TCPackprio:ENABle?')
		return Conversions.str_to_bool(response)
