from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mobile:
	"""Mobile commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
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
	def deRegister(self):
		"""deRegister commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deRegister'):
			from .Mobile_.DeRegister import DeRegister
			self._deRegister = DeRegister(self._core, self._base)
		return self._deRegister

	def clone(self) -> 'Mobile':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mobile(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
