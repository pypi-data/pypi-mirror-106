from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("layer", core, parent)

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.Protocol:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:LAYer:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.layer.get_protocol() \n
		Selects the protocol to be considered for the port scan. \n
			:return: lyr_protocol: TCP | UDP
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:LAYer:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)

	def set_protocol(self, lyr_protocol: enums.Protocol) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:LAYer:PROTocol \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.layer.set_protocol(lyr_protocol = enums.Protocol.TCP) \n
		Selects the protocol to be considered for the port scan. \n
			:param lyr_protocol: TCP | UDP
		"""
		param = Conversions.enum_scalar_to_str(lyr_protocol, enums.Protocol)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:LAYer:PROTocol {param}')
