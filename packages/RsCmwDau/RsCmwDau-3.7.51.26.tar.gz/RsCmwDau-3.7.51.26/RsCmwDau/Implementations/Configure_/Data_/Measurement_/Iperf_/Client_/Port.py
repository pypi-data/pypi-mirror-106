from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("port", core, parent)

	def set(self, port: int, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PORT \n
		Snippet: driver.configure.data.measurement.iperf.client.port.set(port = 1, client = repcap.Client.Default) \n
		Defines the LAN DAU port number for an iperf/iperf3 client instance. \n
			:param port: Range: 0 to 65535
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.decimal_value_to_str(port)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PORT {param}')

	def get(self, client=repcap.Client.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PORT \n
		Snippet: value: int = driver.configure.data.measurement.iperf.client.port.get(client = repcap.Client.Default) \n
		Defines the LAN DAU port number for an iperf/iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: port: Range: 0 to 65535"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PORT?')
		return Conversions.str_to_int(response)
