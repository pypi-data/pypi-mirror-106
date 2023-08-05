from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ran:
	"""Ran commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ran", core, parent)

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Ran_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def get_cataloge(self) -> List[str]:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:CATaloge \n
		Snippet: value: List[str] = driver.configure.data.measurement.throughput.ran.get_cataloge() \n
		Lists all available signaling applications. You can use the returned strings in other commands to select a RAN. \n
			:return: ran: Comma-separated list of all supported values. Each value is represented as a string.
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:CATaloge?')
		return Conversions.str_to_str_list(response)

	def get_mcount(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:MCOunt \n
		Snippet: value: int = driver.configure.data.measurement.throughput.ran.get_mcount() \n
		Specifies the total number of RAN throughput results to be measured. \n
			:return: max_count: Range: 5 to 3600
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:MCOunt?')
		return Conversions.str_to_int(response)

	def set_mcount(self, max_count: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:MCOunt \n
		Snippet: driver.configure.data.measurement.throughput.ran.set_mcount(max_count = 1) \n
		Specifies the total number of RAN throughput results to be measured. \n
			:param max_count: Range: 5 to 3600
		"""
		param = Conversions.decimal_value_to_str(max_count)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:MCOunt {param}')

	def set(self, ran: str, slot=repcap.Slot.Nr1) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN<Index> \n
		Snippet: driver.configure.data.measurement.throughput.ran.set(ran = '1', slot = repcap.Slot.Nr1) \n
		Assigns a RAN to the RAN slot number <Index>. You can query a complete list of all supported strings via the command
		method RsCmwDau.Configure.Data.Measurement.Throughput.Ran.cataloge. \n
			:param ran: String parameter, selecting a signaling application instance
			:param slot: optional repeated capability selector. Default value: Nr1"""
		param = Conversions.value_to_quoted_str(ran)
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN{slot_cmd_val} {param}')

	def get(self, slot=repcap.Slot.Nr1) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN<Index> \n
		Snippet: value: str = driver.configure.data.measurement.throughput.ran.get(slot = repcap.Slot.Nr1) \n
		Assigns a RAN to the RAN slot number <Index>. You can query a complete list of all supported strings via the command
		method RsCmwDau.Configure.Data.Measurement.Throughput.Ran.cataloge. \n
			:param slot: optional repeated capability selector. Default value: Nr1
			:return: ran: String parameter, selecting a signaling application instance"""
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN{slot_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Ran':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ran(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
