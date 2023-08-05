from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FailureCode:
	"""FailureCode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("failureCode", core, parent)

	def set(self, failure_code: int, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:FAILurecode \n
		Snippet: driver.configure.data.control.ims.pcscf.failureCode.set(failure_code = 1, ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines a failure code for the P-CSCF number {p}, behavior = FAIL. \n
			:param failure_code: BADRequest | FORBidden | NOTFound | INTerror | UNAVailable | BUSYeveryw BADRequest: '400 Bad Request' FORBidden: '403 Forbidden' NOTFound: '404 Not Found' INTerror: '500 Server Internal Error' UNAVailable: '503 Service Unavailable' BUSYeveryw: '600 Busy Everywhere'
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		param = Conversions.decimal_value_to_str(failure_code)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:FAILurecode {param}')

	def get(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:FAILurecode \n
		Snippet: value: int = driver.configure.data.control.ims.pcscf.failureCode.get(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines a failure code for the P-CSCF number {p}, behavior = FAIL. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')
			:return: failure_code: BADRequest | FORBidden | NOTFound | INTerror | UNAVailable | BUSYeveryw BADRequest: '400 Bad Request' FORBidden: '403 Forbidden' NOTFound: '404 Not Found' INTerror: '500 Server Internal Error' UNAVailable: '503 Service Unavailable' BUSYeveryw: '600 Busy Everywhere'"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:FAILurecode?')
		return Conversions.str_to_int(response)
