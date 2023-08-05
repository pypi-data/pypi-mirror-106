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

	def set(self, protocol: enums.Protocol, server=repcap.Server.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:PROTocol \n
		Snippet: driver.configure.data.measurement.iperf.server.protocol.set(protocol = enums.Protocol.TCP, server = repcap.Server.Default) \n
		Selects the protocol type to be used for an iperf server instance. \n
			:param protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')"""
		param = Conversions.enum_scalar_to_str(protocol, enums.Protocol)
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:PROTocol {param}')

	# noinspection PyTypeChecker
	def get(self, server=repcap.Server.Default) -> enums.Protocol:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.data.measurement.iperf.server.protocol.get(server = repcap.Server.Default) \n
		Selects the protocol type to be used for an iperf server instance. \n
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')
			:return: protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol"""
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)
