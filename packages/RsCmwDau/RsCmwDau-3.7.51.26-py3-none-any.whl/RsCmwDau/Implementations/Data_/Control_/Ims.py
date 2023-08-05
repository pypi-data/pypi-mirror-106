from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ims:
	"""Ims commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Ims, default value after init: Ims.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ims", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_ims_get', 'repcap_ims_set', repcap.Ims.Ix1)

	def repcap_ims_set(self, enum_value: repcap.Ims) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Ims.Default
		Default value after init: Ims.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_ims_get(self) -> repcap.Ims:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def virtualSubscriber(self):
		"""virtualSubscriber commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_virtualSubscriber'):
			from .Ims_.VirtualSubscriber import VirtualSubscriber
			self._virtualSubscriber = VirtualSubscriber(self._core, self._base)
		return self._virtualSubscriber

	def clone(self) -> 'Ims':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ims(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
