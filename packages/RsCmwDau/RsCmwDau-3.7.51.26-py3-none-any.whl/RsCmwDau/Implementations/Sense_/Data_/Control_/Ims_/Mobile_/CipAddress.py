from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CipAddress:
	"""CipAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cipAddress", core, parent)

	def get(self, ims=repcap.Ims.Default, profile=repcap.Profile.Default) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:MOBile<UE>:CIPaddress \n
		Snippet: value: str = driver.sense.data.control.ims.mobile.cipAddress.get(ims = repcap.Ims.Default, profile = repcap.Profile.Default) \n
		Queries the IP addresses of a subscriber. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param profile: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mobile')
			:return: ip_address: IP addresses as string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		profile_cmd_val = self._base.get_repcap_cmd_value(profile, repcap.Profile)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:MOBile{profile_cmd_val}:CIPaddress?')
		return trim_str_response(response)
