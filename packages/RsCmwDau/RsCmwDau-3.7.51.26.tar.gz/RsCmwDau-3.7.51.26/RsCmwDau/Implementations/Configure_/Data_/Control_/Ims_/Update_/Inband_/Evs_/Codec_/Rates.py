from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rates:
	"""Rates commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rates", core, parent)

	def set(self, evs_bitrate: enums.EvsBitrate, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:EVS:CODec:RATes \n
		Snippet: driver.configure.data.control.ims.update.inband.evs.codec.rates.set(evs_bitrate = enums.EvsBitrate.AW1265, ims = repcap.Ims.Default) \n
		Configures an EVS codec rate or bit rate to be requested via CMR. For BW=DEAC, you cannot set a rate. \n
			:param evs_bitrate: NOReq | AW66 | AW885 | AW1265 | AW1425 | AW1585 | AW1825 | AW1985 | AW2305 | AWB2385 | PR59 | PR72 | PR80 | PR96 | P132 | P164 | P244 | P320 | P480 | P640 | P960 | P1280 | SLO2 | SLO3 | SLO5 | SLO7 | SHO2 | SHO3 | SHO5 | SHO7 | WLO2 | WLO3 | WLO5 | WLO7 | WHO2 | WHO3 | WHO5 | WHO7 NOReq No codec rate requirement (NO_REQ) Only for BW=NOReq AW66 to AWB2385 AMR-WB IO mode, 6.6 kbit/s to 23.85 kbit/s Only for BW=IO PR59 to P1280 Primary mode, 5.9 kbit/s to 128.0 kbit/s For BW=NB: PR59 to P244 For BW=WB: PR59 to P1280 For BW=SWB: PR96 to P1280 For BW=FB: P164 to P1280 SLO2 to SLO7 SWB with channel-aware mode, CA-L-O2 to CA-L-O7 Only for BW=SWBCa SHO2 to SHO7 SWB with channel-aware mode, CA-H-O2 to CA-H-O7 Only for BW=SWBCa WLO2 to WLO7 WB with channel-aware mode, CA-L-O2 to CA-L-O7 Only for BW=WBCA WHO2 to WHO7 WB with channel-aware mode, CA-H-O2 to CA-H-O7 Only for BW=WBCA
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(evs_bitrate, enums.EvsBitrate)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:EVS:CODec:RATes {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.EvsBitrate:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:EVS:CODec:RATes \n
		Snippet: value: enums.EvsBitrate = driver.configure.data.control.ims.update.inband.evs.codec.rates.get(ims = repcap.Ims.Default) \n
		Configures an EVS codec rate or bit rate to be requested via CMR. For BW=DEAC, you cannot set a rate. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: evs_bitrate: NOReq | AW66 | AW885 | AW1265 | AW1425 | AW1585 | AW1825 | AW1985 | AW2305 | AWB2385 | PR59 | PR72 | PR80 | PR96 | P132 | P164 | P244 | P320 | P480 | P640 | P960 | P1280 | SLO2 | SLO3 | SLO5 | SLO7 | SHO2 | SHO3 | SHO5 | SHO7 | WLO2 | WLO3 | WLO5 | WLO7 | WHO2 | WHO3 | WHO5 | WHO7 NOReq No codec rate requirement (NO_REQ) Only for BW=NOReq AW66 to AWB2385 AMR-WB IO mode, 6.6 kbit/s to 23.85 kbit/s Only for BW=IO PR59 to P1280 Primary mode, 5.9 kbit/s to 128.0 kbit/s For BW=NB: PR59 to P244 For BW=WB: PR59 to P1280 For BW=SWB: PR96 to P1280 For BW=FB: P164 to P1280 SLO2 to SLO7 SWB with channel-aware mode, CA-L-O2 to CA-L-O7 Only for BW=SWBCa SHO2 to SHO7 SWB with channel-aware mode, CA-H-O2 to CA-H-O7 Only for BW=SWBCa WLO2 to WLO7 WB with channel-aware mode, CA-L-O2 to CA-L-O7 Only for BW=WBCA WHO2 to WHO7 WB with channel-aware mode, CA-H-O2 to CA-H-O7 Only for BW=WBCA"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:EVS:CODec:RATes?')
		return Conversions.str_to_scalar_enum(response, enums.EvsBitrate)
