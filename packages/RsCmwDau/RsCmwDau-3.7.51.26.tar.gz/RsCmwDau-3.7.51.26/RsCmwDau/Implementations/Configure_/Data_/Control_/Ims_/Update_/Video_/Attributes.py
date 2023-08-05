from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attributes:
	"""Attributes commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("attributes", core, parent)

	def set(self, video_attributes: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:VIDeo:ATTRibutes \n
		Snippet: driver.configure.data.control.ims.update.video.attributes.set(video_attributes = '1', ims = repcap.Ims.Default) \n
		Configures video codec attributes for a call update. \n
			:param video_attributes: Codec attributes as string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(video_attributes)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:VIDeo:ATTRibutes {param}')

	def get(self, ims=repcap.Ims.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:VIDeo:ATTRibutes \n
		Snippet: value: str = driver.configure.data.control.ims.update.video.attributes.get(ims = repcap.Ims.Default) \n
		Configures video codec attributes for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: video_attributes: Codec attributes as string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:VIDeo:ATTRibutes?')
		return trim_str_response(response)
