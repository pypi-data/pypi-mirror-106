from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selection:
	"""Selection commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("selection", core, parent)

	def set(self, sip_timer_sel: enums.SipTimerSel, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SIP:TIMer:CASE:SELection \n
		Snippet: driver.configure.data.control.ims.sip.timer.case.selection.set(sip_timer_sel = enums.SipTimerSel.CUSTom, ims = repcap.Ims.Default) \n
		Selects a configuration mode for SIP timer T1. \n
			:param sip_timer_sel: DEFault | RFC | CUSTom DEFault: 3GPP TS 24.229 (2000 ms) RFC: RFC 3261 (500 ms) CUSTom: method RsCmwDau.Configure.Data.Control.Ims.Sip.Timer.Value.set
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(sip_timer_sel, enums.SipTimerSel)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SIP:TIMer:CASE:SELection {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.SipTimerSel:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SIP:TIMer:CASE:SELection \n
		Snippet: value: enums.SipTimerSel = driver.configure.data.control.ims.sip.timer.case.selection.get(ims = repcap.Ims.Default) \n
		Selects a configuration mode for SIP timer T1. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: sip_timer_sel: DEFault | RFC | CUSTom DEFault: 3GPP TS 24.229 (2000 ms) RFC: RFC 3261 (500 ms) CUSTom: method RsCmwDau.Configure.Data.Control.Ims.Sip.Timer.Value.set"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SIP:TIMer:CASE:SELection?')
		return Conversions.str_to_scalar_enum(response, enums.SipTimerSel)
