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

	def set(self, bw: enums.EvsBw, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:EVS:BW \n
		Snippet: driver.configure.data.control.ims.update.inband.evs.bw.set(bw = enums.EvsBw.DEAC, ims = repcap.Ims.Default) \n
		Configures the EVS codec bandwidth to be requested via CMR. \n
			:param bw: NB | IO | WB | SWB | FB | WBCA | SWBCa | NOReq | DEAC IO: AMR-WB IO mode NB: primary, narrowband WB: primary, wideband SWB: primary, super wideband FB: primary, fullband WBCA: primary, WB, channel-aware mode SWBCa: primary, SWB, channel-aware mode NOReq: NO_REQ, no codec rate requirement DEAC: CMR byte removed from header
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(bw, enums.EvsBw)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:EVS:BW {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.EvsBw:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:EVS:BW \n
		Snippet: value: enums.EvsBw = driver.configure.data.control.ims.update.inband.evs.bw.get(ims = repcap.Ims.Default) \n
		Configures the EVS codec bandwidth to be requested via CMR. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: bw: NB | IO | WB | SWB | FB | WBCA | SWBCa | NOReq | DEAC IO: AMR-WB IO mode NB: primary, narrowband WB: primary, wideband SWB: primary, super wideband FB: primary, fullband WBCA: primary, WB, channel-aware mode SWBCa: primary, SWB, channel-aware mode NOReq: NO_REQ, no codec rate requirement DEAC: CMR byte removed from header"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:EVS:BW?')
		return Conversions.str_to_scalar_enum(response, enums.EvsBw)
