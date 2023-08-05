from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crate:
	"""Crate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("crate", core, parent)

	def set(self, corrupt_rate: float, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:CRATe \n
		Snippet: driver.configure.data.measurement.qos.filterPy.crate.set(corrupt_rate = 1.0, fltr = repcap.Fltr.Default) \n
		Specifies the percentage of packets to be corrupted. \n
			:param corrupt_rate: Range: 0 % to 100 %, Unit: %
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.decimal_value_to_str(corrupt_rate)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:CRATe {param}')

	def get(self, fltr=repcap.Fltr.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:CRATe \n
		Snippet: value: float = driver.configure.data.measurement.qos.filterPy.crate.get(fltr = repcap.Fltr.Default) \n
		Specifies the percentage of packets to be corrupted. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: corrupt_rate: Range: 0 % to 100 %, Unit: %"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:CRATe?')
		return Conversions.str_to_float(response)
