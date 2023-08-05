from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("select", core, parent)

	# noinspection PyTypeChecker
	def get_app(self) -> enums.ApplicationType:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:SELect:APP \n
		Snippet: value: enums.ApplicationType = driver.configure.data.measurement.select.get_app() \n
		Selects the measurement tab to be displayed. \n
			:return: application_type: OVERview | PING | IPERf | THRoughput | DNSReq | IPLogging | IPANalysis | IPReplay | AUDiodelay
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:SELect:APP?')
		return Conversions.str_to_scalar_enum(response, enums.ApplicationType)

	def set_app(self, application_type: enums.ApplicationType) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:SELect:APP \n
		Snippet: driver.configure.data.measurement.select.set_app(application_type = enums.ApplicationType.AUDiodelay) \n
		Selects the measurement tab to be displayed. \n
			:param application_type: OVERview | PING | IPERf | THRoughput | DNSReq | IPLogging | IPANalysis | IPReplay | AUDiodelay
		"""
		param = Conversions.enum_scalar_to_str(application_type, enums.ApplicationType)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:SELect:APP {param}')

	# noinspection PyTypeChecker
	def get_throughput(self) -> enums.ThroughputType:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:SELect:THRoughput \n
		Snippet: value: enums.ThroughputType = driver.configure.data.measurement.select.get_throughput() \n
		Selects the overall throughput tab or the RAN throughput tab for display at the GUI. This command is useful for taking
		screenshots via remote commands. \n
			:return: throughput_type: OVERall | RAN
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:SELect:THRoughput?')
		return Conversions.str_to_scalar_enum(response, enums.ThroughputType)

	def set_throughput(self, throughput_type: enums.ThroughputType) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:SELect:THRoughput \n
		Snippet: driver.configure.data.measurement.select.set_throughput(throughput_type = enums.ThroughputType.OVERall) \n
		Selects the overall throughput tab or the RAN throughput tab for display at the GUI. This command is useful for taking
		screenshots via remote commands. \n
			:param throughput_type: OVERall | RAN
		"""
		param = Conversions.enum_scalar_to_str(throughput_type, enums.ThroughputType)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:SELect:THRoughput {param}')
