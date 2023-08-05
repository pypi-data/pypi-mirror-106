from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("delay", core, parent)

	def set(self, delay: float, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:DELay \n
		Snippet: driver.configure.data.measurement.qos.filterPy.delay.set(delay = 1.0, fltr = repcap.Fltr.Default) \n
		Specifies the delay for a QoS profile. \n
			:param delay: Range: 0 s to 10 s, Unit: s
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.decimal_value_to_str(delay)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:DELay {param}')

	def get(self, fltr=repcap.Fltr.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:DELay \n
		Snippet: value: float = driver.configure.data.measurement.qos.filterPy.delay.get(fltr = repcap.Fltr.Default) \n
		Specifies the delay for a QoS profile. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: delay: Range: 0 s to 10 s, Unit: s"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:DELay?')
		return Conversions.str_to_float(response)
