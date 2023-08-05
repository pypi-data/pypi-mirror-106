from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("status", core, parent)

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, profile=repcap.Profile.Default) -> enums.MobileStatus:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:MOBile<UE>:STATus \n
		Snippet: value: enums.MobileStatus = driver.sense.data.control.ims.mobile.status.get(ims = repcap.Ims.Default, profile = repcap.Profile.Default) \n
		Queries the state of a subscriber. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param profile: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mobile')
			:return: status: UNRegistered | REGistered | EMERgency | EXPired DUT unregistered, registered, emergency registered, registration expired"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		profile_cmd_val = self._base.get_repcap_cmd_value(profile, repcap.Profile)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:MOBile{profile_cmd_val}:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.MobileStatus)
