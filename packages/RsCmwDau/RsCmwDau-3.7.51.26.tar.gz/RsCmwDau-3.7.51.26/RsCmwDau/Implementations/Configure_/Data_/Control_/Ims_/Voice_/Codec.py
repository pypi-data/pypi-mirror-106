from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Codec:
	"""Codec commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Codec, default value after init: Codec.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("codec", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_codec_get', 'repcap_codec_set', repcap.Codec.Ix1)

	def repcap_codec_set(self, enum_value: repcap.Codec) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Codec.Default
		Default value after init: Codec.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_codec_get(self) -> repcap.Codec:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Codec_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	def clone(self) -> 'Codec':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Codec(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
