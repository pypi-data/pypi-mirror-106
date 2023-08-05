from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpLogging:
	"""IpLogging commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipLogging", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.LoggingType:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:TYPE \n
		Snippet: value: enums.LoggingType = driver.configure.data.measurement.ipLogging.get_type_py() \n
		Selects the interface to be monitored. \n
			:return: logging_type: UPIP | UPPP | LANDau | UPMulti | UIPClient UPIP: IP unicast traffic from/to the DUT UPPP: PPP encapsulated IP traffic from/to the DUT LANDau: IP traffic at the LAN DAU connector UPMulti: IP multicast traffic to the DUT UIPClient: IP traffic from/to the DUT with the DAU as client
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.LoggingType)

	def set_type_py(self, logging_type: enums.LoggingType) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:TYPE \n
		Snippet: driver.configure.data.measurement.ipLogging.set_type_py(logging_type = enums.LoggingType.LANDau) \n
		Selects the interface to be monitored. \n
			:param logging_type: UPIP | UPPP | LANDau | UPMulti | UIPClient UPIP: IP unicast traffic from/to the DUT UPPP: PPP encapsulated IP traffic from/to the DUT LANDau: IP traffic at the LAN DAU connector UPMulti: IP multicast traffic to the DUT UIPClient: IP traffic from/to the DUT with the DAU as client
		"""
		param = Conversions.enum_scalar_to_str(logging_type, enums.LoggingType)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:TYPE {param}')

	def get_fsize(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:FSIZe \n
		Snippet: value: float = driver.configure.data.measurement.ipLogging.get_fsize() \n
		Configures the maximum log file size. When this file size is reached, logging stops. The default value 0 bytes means that
		no limit is defined. \n
			:return: file_size: Range: 0 bytes to 1E+9 bytes, Unit: bytes
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:FSIZe?')
		return Conversions.str_to_float(response)

	def set_fsize(self, file_size: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:FSIZe \n
		Snippet: driver.configure.data.measurement.ipLogging.set_fsize(file_size = 1.0) \n
		Configures the maximum log file size. When this file size is reached, logging stops. The default value 0 bytes means that
		no limit is defined. \n
			:param file_size: Range: 0 bytes to 1E+9 bytes, Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(file_size)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:FSIZe {param}')

	def get_pcounter(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:PCOunter \n
		Snippet: value: int = driver.configure.data.measurement.ipLogging.get_pcounter() \n
		Configures the maximum number of IP packets to be logged. When this number of packets is reached, logging stops.
		The default value 0 means that no limit is defined. \n
			:return: packet_counter: Range: 0 to 1E+6
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:PCOunter?')
		return Conversions.str_to_int(response)

	def set_pcounter(self, packet_counter: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:PCOunter \n
		Snippet: driver.configure.data.measurement.ipLogging.set_pcounter(packet_counter = 1) \n
		Configures the maximum number of IP packets to be logged. When this number of packets is reached, logging stops.
		The default value 0 means that no limit is defined. \n
			:param packet_counter: Range: 0 to 1E+6
		"""
		param = Conversions.decimal_value_to_str(packet_counter)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:PCOunter {param}')

	def get_ps_length(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:PSLength \n
		Snippet: value: int = driver.configure.data.measurement.ipLogging.get_ps_length() \n
		Configures the maximum number of bytes to be logged for each IP packet. If the packet is longer, only the specified
		number of bytes is logged. The remaining bytes of the packet are ignored. The default value 0 means that no limit is
		defined. \n
			:return: pkt_snap_length: Range: 0 bytes to 65565 bytes, Unit: bytes
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:PSLength?')
		return Conversions.str_to_int(response)

	def set_ps_length(self, pkt_snap_length: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPLogging:PSLength \n
		Snippet: driver.configure.data.measurement.ipLogging.set_ps_length(pkt_snap_length = 1) \n
		Configures the maximum number of bytes to be logged for each IP packet. If the packet is longer, only the specified
		number of bytes is logged. The remaining bytes of the packet are ignored. The default value 0 means that no limit is
		defined. \n
			:param pkt_snap_length: Range: 0 bytes to 65565 bytes, Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(pkt_snap_length)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPLogging:PSLength {param}')
