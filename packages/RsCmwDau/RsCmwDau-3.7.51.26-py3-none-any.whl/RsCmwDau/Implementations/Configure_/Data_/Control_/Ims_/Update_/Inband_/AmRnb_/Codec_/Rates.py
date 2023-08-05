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

	def set(self, am_rnb_bitrate: enums.AmRnbBitrate, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:AMRNb:CODec:RATes \n
		Snippet: driver.configure.data.control.ims.update.inband.amRnb.codec.rates.set(am_rnb_bitrate = enums.AmRnbBitrate.NOReq, ims = repcap.Ims.Default) \n
		Configures an AMR narrowband codec rate to be requested via CMR. \n
			:param am_rnb_bitrate: R475 | R515 | R590 | R670 | R740 | R795 | R1020 | R1220 | NOReq R475 to R1220: 4.75 kbit/s to 12.20 kbit/s NOReq: no codec rate requirement (NO_REQ)
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(am_rnb_bitrate, enums.AmRnbBitrate)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:AMRNb:CODec:RATes {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.AmRnbBitrate:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:AMRNb:CODec:RATes \n
		Snippet: value: enums.AmRnbBitrate = driver.configure.data.control.ims.update.inband.amRnb.codec.rates.get(ims = repcap.Ims.Default) \n
		Configures an AMR narrowband codec rate to be requested via CMR. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: am_rnb_bitrate: R475 | R515 | R590 | R670 | R740 | R795 | R1020 | R1220 | NOReq R475 to R1220: 4.75 kbit/s to 12.20 kbit/s NOReq: no codec rate requirement (NO_REQ)"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:AMRNb:CODec:RATes?')
		return Conversions.str_to_scalar_enum(response, enums.AmRnbBitrate)
