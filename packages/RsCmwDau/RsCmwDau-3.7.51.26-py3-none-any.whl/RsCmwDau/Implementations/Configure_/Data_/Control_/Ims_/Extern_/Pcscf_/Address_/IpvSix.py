from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvSix:
	"""IpvSix commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipvSix", core, parent)

	def set(self, ip_v_6_address: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:EXTern:PCSCf:ADDRess:IPVSix \n
		Snippet: driver.configure.data.control.ims.extern.pcscf.address.ipvSix.set(ip_v_6_address = '1', ims = repcap.Ims.Default) \n
		Specifies the IPv6 address of an external P-CSCF. \n
			:param ip_v_6_address: IPv6 address string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(ip_v_6_address)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:EXTern:PCSCf:ADDRess:IPVSix {param}')

	def get(self, ims=repcap.Ims.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:EXTern:PCSCf:ADDRess:IPVSix \n
		Snippet: value: str = driver.configure.data.control.ims.extern.pcscf.address.ipvSix.get(ims = repcap.Ims.Default) \n
		Specifies the IPv6 address of an external P-CSCF. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: ip_v_6_address: IPv6 address string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:EXTern:PCSCf:ADDRess:IPVSix?')
		return trim_str_response(response)
