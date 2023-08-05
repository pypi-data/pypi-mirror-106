from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpAnalysis:
	"""TcpAnalysis commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcpAnalysis", core, parent)

	def get_rtt_threshold(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:RTTThreshold \n
		Snippet: value: int = driver.configure.data.measurement.ipAnalysis.tcpAnalysis.get_rtt_threshold() \n
		Defines a threshold (upper limit) for the round-trip time (RTT) . \n
			:return: threshold: Range: 0 ms to 200 ms, Unit: ms
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:RTTThreshold?')
		return Conversions.str_to_int(response)

	def set_rtt_threshold(self, threshold: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:RTTThreshold \n
		Snippet: driver.configure.data.measurement.ipAnalysis.tcpAnalysis.set_rtt_threshold(threshold = 1) \n
		Defines a threshold (upper limit) for the round-trip time (RTT) . \n
			:param threshold: Range: 0 ms to 200 ms, Unit: ms
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:RTTThreshold {param}')

	def get_to_threshold(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TOTHreshold \n
		Snippet: value: float = driver.configure.data.measurement.ipAnalysis.tcpAnalysis.get_to_threshold() \n
		No command help available \n
			:return: threshold: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TOTHreshold?')
		return Conversions.str_to_float(response)

	def set_to_threshold(self, threshold: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TOTHreshold \n
		Snippet: driver.configure.data.measurement.ipAnalysis.tcpAnalysis.set_to_threshold(threshold = 1.0) \n
		No command help available \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TOTHreshold {param}')

	def get_tr_threshold(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TRTHreshold \n
		Snippet: value: float = driver.configure.data.measurement.ipAnalysis.tcpAnalysis.get_tr_threshold() \n
		Defines a threshold (upper limit) for TCP retransmissions as percentage of all transmissions. \n
			:return: threshold: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TRTHreshold?')
		return Conversions.str_to_float(response)

	def set_tr_threshold(self, threshold: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TRTHreshold \n
		Snippet: driver.configure.data.measurement.ipAnalysis.tcpAnalysis.set_tr_threshold(threshold = 1.0) \n
		Defines a threshold (upper limit) for TCP retransmissions as percentage of all transmissions. \n
			:param threshold: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TRTHreshold {param}')

	def get_tws_threshold(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TWSThreshold \n
		Snippet: value: float = driver.configure.data.measurement.ipAnalysis.tcpAnalysis.get_tws_threshold() \n
		Defines a threshold (upper limit) for the current TCP window size as percentage of the negotiated maximum window size. \n
			:return: threshold: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TWSThreshold?')
		return Conversions.str_to_float(response)

	def set_tws_threshold(self, threshold: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:TCPanalysis:TWSThreshold \n
		Snippet: driver.configure.data.measurement.ipAnalysis.tcpAnalysis.set_tws_threshold(threshold = 1.0) \n
		Defines a threshold (upper limit) for the current TCP window size as percentage of the negotiated maximum window size. \n
			:param threshold: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:TCPanalysis:TWSThreshold {param}')
