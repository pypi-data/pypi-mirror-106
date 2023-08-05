from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, codec_use: bool, codec=repcap.Codec.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:CODec<codecIdx>:ENABle \n
		Snippet: driver.configure.data.control.ims.voice.codec.enable.set(codec_use = False, codec = repcap.Codec.Default) \n
		No command help available \n
			:param codec_use: No help available
			:param codec: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Codec')"""
		param = Conversions.bool_to_str(codec_use)
		codec_cmd_val = self._base.get_repcap_cmd_value(codec, repcap.Codec)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:CODec{codec_cmd_val}:ENABle {param}')

	def get(self, codec=repcap.Codec.Default) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:CODec<codecIdx>:ENABle \n
		Snippet: value: bool = driver.configure.data.control.ims.voice.codec.enable.get(codec = repcap.Codec.Default) \n
		No command help available \n
			:param codec: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Codec')
			:return: codec_use: No help available"""
		codec_cmd_val = self._base.get_repcap_cmd_value(codec, repcap.Codec)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS:VOICe:CODec{codec_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
