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

	def set(self, bitrate: float, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:BITRate \n
		Snippet: driver.configure.data.measurement.iperf.client.bitrate.set(bitrate = 1.0, client = repcap.Client.Default) \n
		Defines the maximum bit rate for an iperf/iperf3 client instance. \n
			:param bitrate: Maximum bit rate to be transferred Range: 0 bit/s to 4E+9 bit/s, Unit: bit/s
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.decimal_value_to_str(bitrate)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:BITRate {param}')

	def get(self, client=repcap.Client.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:BITRate \n
		Snippet: value: float = driver.configure.data.measurement.iperf.client.bitrate.get(client = repcap.Client.Default) \n
		Defines the maximum bit rate for an iperf/iperf3 client instance. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: bitrate: Maximum bit rate to be transferred Range: 0 bit/s to 4E+9 bit/s, Unit: bit/s"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:BITRate?')
		return Conversions.str_to_float(response)
