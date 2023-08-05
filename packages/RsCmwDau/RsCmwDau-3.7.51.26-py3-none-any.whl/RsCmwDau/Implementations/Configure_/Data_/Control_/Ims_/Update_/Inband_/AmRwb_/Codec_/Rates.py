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

	def set(self, am_rwb_bit_rate: enums.AmRwbBitRate, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:AMRWb:CODec:RATes \n
		Snippet: driver.configure.data.control.ims.update.inband.amRwb.codec.rates.set(am_rwb_bit_rate = enums.AmRwbBitRate.NOReq, ims = repcap.Ims.Default) \n
		Configures an AMR wideband codec rate to be requested via CMR. \n
			:param am_rwb_bit_rate: R660 | R885 | R1265 | R1425 | R1585 | R1825 | R1985 | R2305 | RA2385 | NOReq R660 to RA2385: 6.60 kbit/s to 23.85 kbit/s NOReq: no codec rate requirement (NO_REQ)
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(am_rwb_bit_rate, enums.AmRwbBitRate)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:AMRWb:CODec:RATes {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.AmRwbBitRate:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:AMRWb:CODec:RATes \n
		Snippet: value: enums.AmRwbBitRate = driver.configure.data.control.ims.update.inband.amRwb.codec.rates.get(ims = repcap.Ims.Default) \n
		Configures an AMR wideband codec rate to be requested via CMR. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: am_rwb_bit_rate: R660 | R885 | R1265 | R1425 | R1585 | R1825 | R1985 | R2305 | RA2385 | NOReq R660 to RA2385: 6.60 kbit/s to 23.85 kbit/s NOReq: no codec rate requirement (NO_REQ)"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:AMRWb:CODec:RATes?')
		return Conversions.str_to_scalar_enum(response, enums.AmRwbBitRate)
