from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Codec:
	"""Codec commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("codec", core, parent)

	def set(self, video_codec: enums.VideoCodec, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:VIDeo:CODec \n
		Snippet: driver.configure.data.control.ims.update.video.codec.set(video_codec = enums.VideoCodec.H263, ims = repcap.Ims.Default) \n
		Selects the video codec for a call update. \n
			:param video_codec: H263 | H264 H.263 or H.264 codec
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(video_codec, enums.VideoCodec)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:VIDeo:CODec {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.VideoCodec:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:VIDeo:CODec \n
		Snippet: value: enums.VideoCodec = driver.configure.data.control.ims.update.video.codec.get(ims = repcap.Ims.Default) \n
		Selects the video codec for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: video_codec: H263 | H264 H.263 or H.264 codec"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:VIDeo:CODec?')
		return Conversions.str_to_scalar_enum(response, enums.VideoCodec)
