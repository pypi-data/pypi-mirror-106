from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MediaEndpoint:
	"""MediaEndpoint commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mediaEndpoint", core, parent)

	def set(self, media_endpoint: enums.MediaEndpoint, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MEDiaendpoin \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mediaEndpoint.set(media_endpoint = enums.MediaEndpoint.AUDioboard, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the media endpoint. \n
			:param media_endpoint: LOOPback | FORWard | AUDioboard | PCAP LOOPback: Loop back to the DUT FORWard: Route to an external media endpoint AUDioboard: Route to the speech codec of the audio board PCAP: Play a PCAP file
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(media_endpoint, enums.MediaEndpoint)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MEDiaendpoin {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.MediaEndpoint:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MEDiaendpoin \n
		Snippet: value: enums.MediaEndpoint = driver.configure.data.control.ims.virtualSubscriber.mediaEndpoint.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the media endpoint. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: media_endpoint: LOOPback | FORWard | AUDioboard | PCAP LOOPback: Loop back to the DUT FORWard: Route to an external media endpoint AUDioboard: Route to the speech codec of the audio board PCAP: Play a PCAP file"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MEDiaendpoin?')
		return Conversions.str_to_scalar_enum(response, enums.MediaEndpoint)
