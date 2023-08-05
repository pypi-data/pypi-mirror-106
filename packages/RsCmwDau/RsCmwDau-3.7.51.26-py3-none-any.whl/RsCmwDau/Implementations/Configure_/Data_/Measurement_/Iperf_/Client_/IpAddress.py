from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)

	def set(self, ip_address: str, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:IPADdress \n
		Snippet: driver.configure.data.measurement.iperf.client.ipAddress.set(ip_address = '1', client = repcap.Client.Default) \n
		Specifies the IP address of the DUT for an iperf/iperf3 client instance. \n
			:param ip_address: String containing the IP address
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.value_to_quoted_str(ip_address)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:IPADdress {param}')

	def get(self, client=repcap.Client.Default) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:IPADdress \n
		Snippet: value: str = driver.configure.data.measurement.iperf.client.ipAddress.get(client = repcap.Client.Default) \n
		Specifies the IP address of the DUT for an iperf/iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: ip_address: String containing the IP address"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:IPADdress?')
		return trim_str_response(response)
