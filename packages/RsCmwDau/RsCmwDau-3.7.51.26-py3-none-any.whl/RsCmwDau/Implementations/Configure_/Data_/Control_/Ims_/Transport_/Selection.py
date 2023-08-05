from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selection:
	"""Selection commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("selection", core, parent)

	def set(self, transport_selection: enums.TransportSel, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:TRANsport:SELection \n
		Snippet: driver.configure.data.control.ims.transport.selection.set(transport_selection = enums.TransportSel.CUSTom, ims = repcap.Ims.Default) \n
		Configures whether TCP or UDP is used by the internal IMS server. \n
			:param transport_selection: DEFault | TCP | UDP | CUSTom DEFault: Fixed threshold as defined in RFC 3261 TCP: Only TCP is used UDP: Only UDP is used CUSTom: UDP for short messages, TCP for long messages, threshold configurable via method RsCmwDau.Configure.Data.Control.Ims.Threshold.Value.set
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(transport_selection, enums.TransportSel)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:TRANsport:SELection {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.TransportSel:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:TRANsport:SELection \n
		Snippet: value: enums.TransportSel = driver.configure.data.control.ims.transport.selection.get(ims = repcap.Ims.Default) \n
		Configures whether TCP or UDP is used by the internal IMS server. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: transport_selection: DEFault | TCP | UDP | CUSTom DEFault: Fixed threshold as defined in RFC 3261 TCP: Only TCP is used UDP: Only UDP is used CUSTom: UDP for short messages, TCP for long messages, threshold configurable via method RsCmwDau.Configure.Data.Control.Ims.Threshold.Value.set"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:TRANsport:SELection?')
		return Conversions.str_to_scalar_enum(response, enums.TransportSel)
