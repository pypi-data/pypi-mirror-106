from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("select", core, parent)

	def set(self, bw_range: enums.BwRange, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:SYNCh:SELect \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.evs.synch.select.set(bw_range = enums.BwRange.COMMon, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects a configuration mode for the bandwidth and bit-rate settings of the EVS primary mode. The uplink (receive) and
		the downlink (send) can be configured together (COMMon) or separately (SENDrx) . \n
			:param bw_range: COMMon | SENDrx COMMon The following commands apply: method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.BwCommon.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Common.Bitrate.Range.set SENDrx The following commands apply: method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Send.Bw.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Send.Bitrate.Range.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Receive.Bw.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Receive.Bitrate.Range.set
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(bw_range, enums.BwRange)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:SYNCh:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.BwRange:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:SYNCh:SELect \n
		Snippet: value: enums.BwRange = driver.configure.data.control.ims.virtualSubscriber.evs.synch.select.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects a configuration mode for the bandwidth and bit-rate settings of the EVS primary mode. The uplink (receive) and
		the downlink (send) can be configured together (COMMon) or separately (SENDrx) . \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: bw_range: COMMon | SENDrx COMMon The following commands apply: method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.BwCommon.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Common.Bitrate.Range.set SENDrx The following commands apply: method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Send.Bw.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Send.Bitrate.Range.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Receive.Bw.set method RsCmwDau.Configure.Data.Control.Ims.VirtualSubscriber.Evs.Receive.Bitrate.Range.set"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:SYNCh:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.BwRange)
