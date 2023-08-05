from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SbSize:
	"""SbSize commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sbSize", core, parent)

	def set(self, sb_size: float, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:SBSize \n
		Snippet: driver.configure.data.measurement.iperf.client.sbSize.set(sb_size = 1.0, client = repcap.Client.Default) \n
		Specifies the size of the socket buffer for an iperf/iperf3 client instance. \n
			:param sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.decimal_value_to_str(sb_size)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:SBSize {param}')

	def get(self, client=repcap.Client.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:SBSize \n
		Snippet: value: float = driver.configure.data.measurement.iperf.client.sbSize.get(client = repcap.Client.Default) \n
		Specifies the size of the socket buffer for an iperf/iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:SBSize?')
		return Conversions.str_to_float(response)
