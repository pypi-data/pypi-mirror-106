from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bw:
	"""Bw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bw", core, parent)

	def set(self, send_bw: enums.Bandwidth, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SEND:BW \n
		Snippet: driver.configure.data.control.ims.update.evs.send.bw.set(send_bw = enums.Bandwidth.FB, ims = repcap.Ims.Default) \n
		Selects the codec bandwidths supported in the EVS primary mode in the downlink (send) direction, for a call update and
		separate configuration. \n
			:param send_bw: NB | WB | SWB | FB | NBWB | NBSWb | NBFB NB: narrowband only WB: wideband only SWB: super wideband only FB: fullband only NBWB: narrowband and wideband NBSWb: narrowband, wideband and super wideband NBFB: narrowband, wideband, super wideband and fullband
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(send_bw, enums.Bandwidth)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SEND:BW {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.Bandwidth:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SEND:BW \n
		Snippet: value: enums.Bandwidth = driver.configure.data.control.ims.update.evs.send.bw.get(ims = repcap.Ims.Default) \n
		Selects the codec bandwidths supported in the EVS primary mode in the downlink (send) direction, for a call update and
		separate configuration. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: send_bw: NB | WB | SWB | FB | NBWB | NBSWb | NBFB NB: narrowband only WB: wideband only SWB: super wideband only FB: fullband only NBWB: narrowband and wideband NBSWb: narrowband, wideband and super wideband NBFB: narrowband, wideband, super wideband and fullband"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SEND:BW?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)
