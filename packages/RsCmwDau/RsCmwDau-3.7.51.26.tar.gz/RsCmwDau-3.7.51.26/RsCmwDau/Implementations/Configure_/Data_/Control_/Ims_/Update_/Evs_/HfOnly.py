from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HfOnly:
	"""HfOnly commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hfOnly", core, parent)

	def set(self, hf: enums.HfOnly, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:HFONly \n
		Snippet: driver.configure.data.control.ims.update.evs.hfOnly.set(hf = enums.HfOnly.BOTH, ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'hf-only' for a call update. \n
			:param hf: BOTH | HEADfull | NP Both, header-full only, not present
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(hf, enums.HfOnly)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:HFONly {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.HfOnly:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:HFONly \n
		Snippet: value: enums.HfOnly = driver.configure.data.control.ims.update.evs.hfOnly.get(ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'hf-only' for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: hf: BOTH | HEADfull | NP Both, header-full only, not present"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:HFONly?')
		return Conversions.str_to_scalar_enum(response, enums.HfOnly)
