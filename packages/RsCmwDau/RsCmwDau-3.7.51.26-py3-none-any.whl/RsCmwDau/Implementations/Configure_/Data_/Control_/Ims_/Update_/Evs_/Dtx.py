from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtx:
	"""Dtx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dtx", core, parent)

	def set(self, dtx: enums.DtxRecv, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:DTX \n
		Snippet: driver.configure.data.control.ims.update.evs.dtx.set(dtx = enums.DtxRecv.DISable, ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'dtx' for a call update. \n
			:param dtx: DISable | ENABle | NP Disable, enable, not present
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(dtx, enums.DtxRecv)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:DTX {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.DtxRecv:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:DTX \n
		Snippet: value: enums.DtxRecv = driver.configure.data.control.ims.update.evs.dtx.get(ims = repcap.Ims.Default) \n
		Specifies the SDP parameter 'dtx' for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: dtx: DISable | ENABle | NP Disable, enable, not present"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:DTX?')
		return Conversions.str_to_scalar_enum(response, enums.DtxRecv)
