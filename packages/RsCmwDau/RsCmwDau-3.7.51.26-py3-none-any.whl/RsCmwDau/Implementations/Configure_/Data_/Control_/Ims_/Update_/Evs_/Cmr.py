from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmr:
	"""Cmr commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmr", core, parent)

	def set(self, cmr: enums.Cmr, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:CMR \n
		Snippet: driver.configure.data.control.ims.update.evs.cmr.set(cmr = enums.Cmr.DISable, ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'cmr' for the EVS codec, for a call update. \n
			:param cmr: DISable | ENABle | PRESent | NP Disable, enable, present all, not present
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(cmr, enums.Cmr)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:CMR {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.Cmr:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:CMR \n
		Snippet: value: enums.Cmr = driver.configure.data.control.ims.update.evs.cmr.get(ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'cmr' for the EVS codec, for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: cmr: DISable | ENABle | PRESent | NP Disable, enable, present all, not present"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:CMR?')
		return Conversions.str_to_scalar_enum(response, enums.Cmr)
