from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Jitter:
	"""Jitter commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("jitter", core, parent)

	def set(self, jitter: float, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:JITTer \n
		Snippet: driver.configure.data.measurement.qos.filterPy.jitter.set(jitter = 1.0, fltr = repcap.Fltr.Default) \n
		Specifies the jitter for a QoS profile. The jitter must be smaller than or equal to the configured delay. \n
			:param jitter: Range: 0 s to 10 s, Unit: s
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.decimal_value_to_str(jitter)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:JITTer {param}')

	def get(self, fltr=repcap.Fltr.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:JITTer \n
		Snippet: value: float = driver.configure.data.measurement.qos.filterPy.jitter.get(fltr = repcap.Fltr.Default) \n
		Specifies the jitter for a QoS profile. The jitter must be smaller than or equal to the configured delay. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: jitter: Range: 0 s to 10 s, Unit: s"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:JITTer?')
		return Conversions.str_to_float(response)
