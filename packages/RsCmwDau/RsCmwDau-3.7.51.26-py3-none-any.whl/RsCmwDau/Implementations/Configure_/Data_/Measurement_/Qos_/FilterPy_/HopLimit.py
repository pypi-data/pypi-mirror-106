from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HopLimit:
	"""HopLimit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hopLimit", core, parent)

	def set(self, hop_limit: int, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:HOPLmt \n
		Snippet: driver.configure.data.measurement.qos.filterPy.hopLimit.set(hop_limit = 1, fltr = repcap.Fltr.Default) \n
		Sets the hop limit of packets matching the filter criteria. The setting 0 means that the hop limit of the packets is left
		unchanged. \n
			:param hop_limit: Range: 0 to 255
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.decimal_value_to_str(hop_limit)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:HOPLmt {param}')

	def get(self, fltr=repcap.Fltr.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:HOPLmt \n
		Snippet: value: int = driver.configure.data.measurement.qos.filterPy.hopLimit.get(fltr = repcap.Fltr.Default) \n
		Sets the hop limit of packets matching the filter criteria. The setting 0 means that the hop limit of the packets is left
		unchanged. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: hop_limit: Range: 0 to 255"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:HOPLmt?')
		return Conversions.str_to_int(response)
