from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinSe:
	"""MinSe commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minSe", core, parent)

	def set(self, min_se: int, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:SESSion:MINSe \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.session.minSe.set(min_se = 1, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the 'Min-SE' header field for the session expiration timer feature. \n
			:param min_se: Range: 0 to 64535
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.decimal_value_to_str(min_se)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:SESSion:MINSe {param}')

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:SESSion:MINSe \n
		Snippet: value: int = driver.configure.data.control.ims.virtualSubscriber.session.minSe.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Configures the 'Min-SE' header field for the session expiration timer feature. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: min_se: Range: 0 to 64535"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:SESSion:MINSe?')
		return Conversions.str_to_int(response)
