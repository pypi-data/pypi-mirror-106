from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, codec_rate: bool, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default, codec=repcap.Codec.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AMR:CODec<CodecIdx>:ENABle \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.amr.codec.enable.set(codec_rate = False, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default, codec = repcap.Codec.Default) \n
		Enables or disables a codec rate for the currently active AMR type, see method RsCmwDau.Configure.Data.Control.Ims.
		VirtualSubscriber.AdCodec.TypePy.set. \n
			:param codec_rate: OFF | ON OFF: codec rate not supported ON: codec rate supported
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:param codec: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Codec')"""
		param = Conversions.bool_to_str(codec_rate)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		codec_cmd_val = self._base.get_repcap_cmd_value(codec, repcap.Codec)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AMR:CODec{codec_cmd_val}:ENABle {param}')

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default, codec=repcap.Codec.Default) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AMR:CODec<CodecIdx>:ENABle \n
		Snippet: value: bool = driver.configure.data.control.ims.virtualSubscriber.amr.codec.enable.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default, codec = repcap.Codec.Default) \n
		Enables or disables a codec rate for the currently active AMR type, see method RsCmwDau.Configure.Data.Control.Ims.
		VirtualSubscriber.AdCodec.TypePy.set. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:param codec: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Codec')
			:return: codec_rate: OFF | ON OFF: codec rate not supported ON: codec rate supported"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		codec_cmd_val = self._base.get_repcap_cmd_value(codec, repcap.Codec)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AMR:CODec{codec_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
