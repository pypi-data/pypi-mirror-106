from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("config", core, parent)

	def set(self, evs_io_mode_cnfg: enums.EvsIoModeCnfg, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:IO:MODE:CONFig \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.evs.io.mode.config.set(evs_io_mode_cnfg = enums.EvsIoModeCnfg.AMRWb, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the speech packet type to be sent from the audio board to the DUT for the EVS AMR-WB IO mode. \n
			:param evs_io_mode_cnfg: EVSamrwb | AMRWb AMRWb: AMR-WB encoded packets EVSamrwb: EVS AMR-WB IO encoded packets
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(evs_io_mode_cnfg, enums.EvsIoModeCnfg)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:IO:MODE:CONFig {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.EvsIoModeCnfg:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:IO:MODE:CONFig \n
		Snippet: value: enums.EvsIoModeCnfg = driver.configure.data.control.ims.virtualSubscriber.evs.io.mode.config.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the speech packet type to be sent from the audio board to the DUT for the EVS AMR-WB IO mode. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: evs_io_mode_cnfg: EVSamrwb | AMRWb AMRWb: AMR-WB encoded packets EVSamrwb: EVS AMR-WB IO encoded packets"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:IO:MODE:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.EvsIoModeCnfg)
