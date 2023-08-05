from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bitrate:
	"""Bitrate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bitrate", core, parent)

	def set(self, qos_bitrate: int or bool, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:BITRate \n
		Snippet: driver.configure.data.measurement.qos.filterPy.bitrate.set(qos_bitrate = 1, fltr = repcap.Fltr.Default) \n
		Specifies the maximum bit rate for a QoS profile. \n
			:param qos_bitrate: Range: 0 bit/s to 100E+9 bit/s, Unit: bit/s Additional values: OFF | ON (disables | enables the bit-rate limitation)
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.decimal_or_bool_value_to_str(qos_bitrate)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:BITRate {param}')

	def get(self, fltr=repcap.Fltr.Default) -> int or bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:BITRate \n
		Snippet: value: int or bool = driver.configure.data.measurement.qos.filterPy.bitrate.get(fltr = repcap.Fltr.Default) \n
		Specifies the maximum bit rate for a QoS profile. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: qos_bitrate: Range: 0 bit/s to 100E+9 bit/s, Unit: bit/s Additional values: OFF | ON (disables | enables the bit-rate limitation)"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:BITRate?')
		return Conversions.str_to_int_or_bool(response)
