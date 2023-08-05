from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpApplic:
	"""DpApplic commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpApplic", core, parent)

	def get_app(self) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPAPplic:APP \n
		Snippet: value: str = driver.configure.data.measurement.ipAnalysis.dpcp.dpApplic.get_app() \n
		Selects a layer of the 'Data per Application' pie chart view. You can navigate from the current layer to the next lower
		or higher layer. The initial current layer is the application layer. The lower layers are layer 7, layer 4 and layer 3.
		To query the entries (strings) of the current layer, see method RsCmwDau.Data.Measurement.IpAnalysis.Dpcp.DpApplic.fetch. \n
			:return: app_selected: String with an entry of the current layer: Navigates to the next lower layer for this entry 'Back' or string unknown at the current layer: Navigates back to the next higher layer
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPAPplic:APP?')
		return trim_str_response(response)

	def set_app(self, app_selected: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:DPCP:DPAPplic:APP \n
		Snippet: driver.configure.data.measurement.ipAnalysis.dpcp.dpApplic.set_app(app_selected = '1') \n
		Selects a layer of the 'Data per Application' pie chart view. You can navigate from the current layer to the next lower
		or higher layer. The initial current layer is the application layer. The lower layers are layer 7, layer 4 and layer 3.
		To query the entries (strings) of the current layer, see method RsCmwDau.Data.Measurement.IpAnalysis.Dpcp.DpApplic.fetch. \n
			:param app_selected: String with an entry of the current layer: Navigates to the next lower layer for this entry 'Back' or string unknown at the current layer: Navigates back to the next higher layer
		"""
		param = Conversions.value_to_quoted_str(app_selected)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:DPCP:DPAPplic:APP {param}')
