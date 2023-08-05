from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Trace, default value after init: Trace.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_trace_get', 'repcap_trace_set', repcap.Trace.Ix1)

	def repcap_trace_set(self, enum_value: repcap.Trace) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Trace.Default
		Default value after init: Trace.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_trace_get(self) -> repcap.Trace:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def tflowId(self):
		"""tflowId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tflowId'):
			from .Trace_.TflowId import TflowId
			self._tflowId = TflowId(self._core, self._base)
		return self._tflowId

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
