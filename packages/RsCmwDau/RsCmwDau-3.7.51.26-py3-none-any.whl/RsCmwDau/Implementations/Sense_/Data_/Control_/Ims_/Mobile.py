from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mobile:
	"""Mobile commands group definition. 6 total commands, 3 Sub-groups, 2 group commands
	Repeated Capability: Profile, default value after init: Profile.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mobile", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_profile_get', 'repcap_profile_set', repcap.Profile.Nr1)

	def repcap_profile_set(self, enum_value: repcap.Profile) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Profile.Default
		Default value after init: Profile.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_profile_get(self) -> repcap.Profile:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def cipAddress(self):
		"""cipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cipAddress'):
			from .Mobile_.CipAddress import CipAddress
			self._cipAddress = CipAddress(self._core, self._base)
		return self._cipAddress

	@property
	def status(self):
		"""status commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_status'):
			from .Mobile_.Status import Status
			self._status = Status(self._core, self._base)
		return self._status

	@property
	def uid(self):
		"""uid commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_uid'):
			from .Mobile_.Uid import Uid
			self._uid = Uid(self._core, self._base)
		return self._uid

	def get_hdomain(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS:MOBile:HDOMain \n
		Snippet: value: str = driver.sense.data.control.ims.mobile.get_hdomain() \n
		No command help available \n
			:return: home_domain: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:MOBile:HDOMain?')
		return trim_str_response(response)

	def get_ip_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS:MOBile:IPADdress \n
		Snippet: value: str = driver.sense.data.control.ims.mobile.get_ip_address() \n
		No command help available \n
			:return: ip_address: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:MOBile:IPADdress?')
		return trim_str_response(response)

	def clone(self) -> 'Mobile':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mobile(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
