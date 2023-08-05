from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apn:
	"""Apn commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: AccPointName, default value after init: AccPointName.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apn", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_accPointName_get', 'repcap_accPointName_set', repcap.AccPointName.Nr1)

	def repcap_accPointName_set(self, enum_value: repcap.AccPointName) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AccPointName.Default
		Default value after init: AccPointName.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_accPointName_get(self) -> repcap.AccPointName:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def release(self):
		"""release commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_release'):
			from .Apn_.Release import Release
			self._release = Release(self._core, self._base)
		return self._release

	def clone(self) -> 'Apn':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Apn(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
