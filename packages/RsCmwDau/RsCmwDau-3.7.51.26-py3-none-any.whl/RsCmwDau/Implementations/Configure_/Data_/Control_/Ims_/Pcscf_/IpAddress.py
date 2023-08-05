from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)

	def set(self, ip_address: str, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:IPADdress \n
		Snippet: driver.configure.data.control.ims.pcscf.ipAddress.set(ip_address = '1', ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the IP address of the P-CSCF number {p}. \n
			:param ip_address: IPv4 or IPv6 address string Example: '172.22.1.201' or 'fd01:cafe::1/64'
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		param = Conversions.value_to_quoted_str(ip_address)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:IPADdress {param}')

	def get(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:IPADdress \n
		Snippet: value: str = driver.configure.data.control.ims.pcscf.ipAddress.get(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the IP address of the P-CSCF number {p}. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')
			:return: ip_address: IPv4 or IPv6 address string Example: '172.22.1.201' or 'fd01:cafe::1/64'"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:IPADdress?')
		return trim_str_response(response)
