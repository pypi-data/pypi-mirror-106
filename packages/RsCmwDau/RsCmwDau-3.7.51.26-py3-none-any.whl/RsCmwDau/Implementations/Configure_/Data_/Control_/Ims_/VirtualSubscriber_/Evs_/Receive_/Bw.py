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

	def set(self, rx_bw: enums.Bandwidth, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:RECeive:BW \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.evs.receive.bw.set(rx_bw = enums.Bandwidth.FB, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the codec bandwidths supported in the EVS primary mode in the uplink (receive) direction. The setting applies
		only if the uplink and the downlink are configured separately, see method RsCmwDau.Configure.Data.Control.Ims.
		VirtualSubscriber.Evs.Synch.Select.set. \n
			:param rx_bw: NB | WB | SWB | FB | NBWB | NBSWb | NBFB NB: narrowband only WB: wideband only SWB: super wideband only FB: fullband only NBWB: narrowband and wideband NBSWb: narrowband, wideband and super wideband NBFB: narrowband, wideband, super wideband and fullband
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(rx_bw, enums.Bandwidth)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:RECeive:BW {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.Bandwidth:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:RECeive:BW \n
		Snippet: value: enums.Bandwidth = driver.configure.data.control.ims.virtualSubscriber.evs.receive.bw.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the codec bandwidths supported in the EVS primary mode in the uplink (receive) direction. The setting applies
		only if the uplink and the downlink are configured separately, see method RsCmwDau.Configure.Data.Control.Ims.
		VirtualSubscriber.Evs.Synch.Select.set. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: rx_bw: NB | WB | SWB | FB | NBWB | NBSWb | NBFB NB: narrowband only WB: wideband only SWB: super wideband only FB: fullband only NBWB: narrowband and wideband NBSWb: narrowband, wideband and super wideband NBFB: narrowband, wideband, super wideband and fullband"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:RECeive:BW?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)
