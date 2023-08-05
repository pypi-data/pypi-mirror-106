from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulink:
	"""Ulink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Slot, default value after init: Slot.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ulink", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_slot_get', 'repcap_slot_set', repcap.Slot.Nr1)

	def repcap_slot_set(self, enum_value: repcap.Slot) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Slot.Default
		Default value after init: Slot.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_slot_get(self) -> repcap.Slot:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, uplink_selection: bool, slot=repcap.Slot.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:TRACe:ULINk<Index> \n
		Snippet: driver.configure.data.measurement.throughput.ran.trace.ulink.set(uplink_selection = False, slot = repcap.Slot.Default) \n
		Enables or disables the uplink trace for RAN slot number <Index>. \n
			:param uplink_selection: OFF | ON
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ulink')"""
		param = Conversions.bool_to_str(uplink_selection)
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TRACe:ULINk{slot_cmd_val} {param}')

	def get(self, slot=repcap.Slot.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:TRACe:ULINk<Index> \n
		Snippet: value: bool = driver.configure.data.measurement.throughput.ran.trace.ulink.get(slot = repcap.Slot.Default) \n
		Enables or disables the uplink trace for RAN slot number <Index>. \n
			:param slot: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ulink')
			:return: uplink_selection: OFF | ON"""
		slot_cmd_val = self._base.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TRACe:ULINk{slot_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ulink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ulink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
