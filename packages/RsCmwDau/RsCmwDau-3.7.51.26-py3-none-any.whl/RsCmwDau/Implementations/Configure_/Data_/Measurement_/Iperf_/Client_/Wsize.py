from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wsize:
	"""Wsize commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("wsize", core, parent)

	def set(self, window_size: float, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:WSIZe \n
		Snippet: driver.configure.data.measurement.iperf.client.wsize.set(window_size = 1.0, client = repcap.Client.Default) \n
		No command help available \n
			:param window_size: No help available
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.decimal_value_to_str(window_size)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:WSIZe {param}')

	def get(self, client=repcap.Client.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:WSIZe \n
		Snippet: value: float = driver.configure.data.measurement.iperf.client.wsize.get(client = repcap.Client.Default) \n
		No command help available \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: window_size: No help available"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:WSIZe?')
		return Conversions.str_to_float(response)
