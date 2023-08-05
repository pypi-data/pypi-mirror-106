from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpLayer:
	"""DpLayer commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpLayer", core, parent)

	# noinspection PyTypeChecker
	def get_layer(self) -> enums.Layer:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPLayer:LAYer \n
		Snippet: value: enums.Layer = driver.configure.data.measurement.ipAnalysis.dpcp.dpLayer.get_layer() \n
		Selects an analysis layer for the 'Data per Layer' pie chart view. \n
			:return: layer: FEATure | APP | L7 | L4 | L3
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPLayer:LAYer?')
		return Conversions.str_to_scalar_enum(response, enums.Layer)

	def set_layer(self, layer: enums.Layer) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPLayer:LAYer \n
		Snippet: driver.configure.data.measurement.ipAnalysis.dpcp.dpLayer.set_layer(layer = enums.Layer.APP) \n
		Selects an analysis layer for the 'Data per Layer' pie chart view. \n
			:param layer: FEATure | APP | L7 | L4 | L3
		"""
		param = Conversions.enum_scalar_to_str(layer, enums.Layer)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPLayer:LAYer {param}')
