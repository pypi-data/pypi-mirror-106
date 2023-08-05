from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protocol:
	"""Protocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("protocol", core, parent)

	def set(self, protocol: enums.Protocol, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PROTocol \n
		Snippet: driver.configure.data.measurement.iperf.client.protocol.set(protocol = enums.Protocol.TCP, client = repcap.Client.Default) \n
		Selects the protocol type to be used for an iperf/iperf3 client instance. \n
			:param protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.enum_scalar_to_str(protocol, enums.Protocol)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PROTocol {param}')

	# noinspection PyTypeChecker
	def get(self, client=repcap.Client.Default) -> enums.Protocol:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.data.measurement.iperf.client.protocol.get(client = repcap.Client.Default) \n
		Selects the protocol type to be used for an iperf/iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)
