from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("value", core, parent)

	def set(self, sip_timer_value: int, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SIP:TIMer:VALue \n
		Snippet: driver.configure.data.control.ims.sip.timer.value.set(sip_timer_value = 1, ims = repcap.Ims.Default) \n
		Sets SIP timer T1 for custom mode, see method RsCmwDau.Configure.Data.Control.Ims.Sip.Timer.Case.Selection.set. \n
			:param sip_timer_value: Range: 10 ms to 600E+3 ms, Unit: ms
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.decimal_value_to_str(sip_timer_value)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SIP:TIMer:VALue {param}')

	def get(self, ims=repcap.Ims.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SIP:TIMer:VALue \n
		Snippet: value: int = driver.configure.data.control.ims.sip.timer.value.get(ims = repcap.Ims.Default) \n
		Sets SIP timer T1 for custom mode, see method RsCmwDau.Configure.Data.Control.Ims.Sip.Timer.Case.Selection.set. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: sip_timer_value: Range: 10 ms to 600E+3 ms, Unit: ms"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SIP:TIMer:VALue?')
		return Conversions.str_to_int(response)
