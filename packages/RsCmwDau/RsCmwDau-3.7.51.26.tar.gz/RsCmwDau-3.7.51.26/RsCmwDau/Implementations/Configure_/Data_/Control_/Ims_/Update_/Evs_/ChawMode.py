from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChawMode:
	"""ChawMode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("chawMode", core, parent)

	def set(self, chaw_mode: enums.ChawMode, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:CHAWmode \n
		Snippet: driver.configure.data.control.ims.update.evs.chawMode.set(chaw_mode = enums.ChawMode.DIS, ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'ch-aw-recv' for the EVS codec, for a call update. \n
			:param chaw_mode: DIS | NUSed | TWO | THRee | FIVE | SEVen | NP Disabled, not used, 2, 3, 5, 7, not present
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(chaw_mode, enums.ChawMode)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:CHAWmode {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.ChawMode:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:CHAWmode \n
		Snippet: value: enums.ChawMode = driver.configure.data.control.ims.update.evs.chawMode.get(ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'ch-aw-recv' for the EVS codec, for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: chaw_mode: DIS | NUSed | TWO | THRee | FIVE | SEVen | NP Disabled, not used, 2, 3, 5, 7, not present"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:CHAWmode?')
		return Conversions.str_to_scalar_enum(response, enums.ChawMode)
