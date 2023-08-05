from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reverse:
	"""Reverse commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reverse", core, parent)

	def set(self, mode: bool, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:REVerse \n
		Snippet: driver.configure.data.measurement.iperf.client.reverse.set(mode = False, client = repcap.Client.Default) \n
		Enables the reverse mode for an iperf3 client instance. \n
			:param mode: OFF | ON ON: reverse mode OFF: normal mode
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.bool_to_str(mode)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:REVerse {param}')

	def get(self, client=repcap.Client.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:REVerse \n
		Snippet: value: bool = driver.configure.data.measurement.iperf.client.reverse.get(client = repcap.Client.Default) \n
		Enables the reverse mode for an iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: mode: OFF | ON ON: reverse mode OFF: normal mode"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:REVerse?')
		return Conversions.str_to_bool(response)
