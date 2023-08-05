from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RetryAfter:
	"""RetryAfter commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("retryAfter", core, parent)

	def set(self, retry_after: int, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:RETRyafter \n
		Snippet: driver.configure.data.control.ims.pcscf.retryAfter.set(retry_after = 1, ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the contents of the 'Retry After' header field for the P-CSCF number {p}, behavior = FAIL. \n
			:param retry_after: Unit: s
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		param = Conversions.decimal_value_to_str(retry_after)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:RETRyafter {param}')

	def get(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:RETRyafter \n
		Snippet: value: int = driver.configure.data.control.ims.pcscf.retryAfter.get(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the contents of the 'Retry After' header field for the P-CSCF number {p}, behavior = FAIL. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')
			:return: retry_after: Unit: s"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:RETRyafter?')
		return Conversions.str_to_int(response)
