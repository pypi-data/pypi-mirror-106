from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VirtualSubscriber:
	"""VirtualSubscriber commands group definition. 4 total commands, 4 Sub-groups, 0 group commands
	Repeated Capability: VirtualSubscriber, default value after init: VirtualSubscriber.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("virtualSubscriber", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_virtualSubscriber_get', 'repcap_virtualSubscriber_set', repcap.VirtualSubscriber.Nr1)

	def repcap_virtualSubscriber_set(self, enum_value: repcap.VirtualSubscriber) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to VirtualSubscriber.Default
		Default value after init: VirtualSubscriber.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_virtualSubscriber_get(self) -> repcap.VirtualSubscriber:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def mtFileTfr(self):
		"""mtFileTfr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtFileTfr'):
			from .VirtualSubscriber_.MtFileTfr import MtFileTfr
			self._mtFileTfr = MtFileTfr(self._core, self._base)
		return self._mtFileTfr

	@property
	def mtSms(self):
		"""mtSms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtSms'):
			from .VirtualSubscriber_.MtSms import MtSms
			self._mtSms = MtSms(self._core, self._base)
		return self._mtSms

	@property
	def mtCall(self):
		"""mtCall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtCall'):
			from .VirtualSubscriber_.MtCall import MtCall
			self._mtCall = MtCall(self._core, self._base)
		return self._mtCall

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .VirtualSubscriber_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	def clone(self) -> 'VirtualSubscriber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VirtualSubscriber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
