from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlink:
	"""Dlink commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Dlink, default value after init: Dlink.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dlink", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_dlink_get', 'repcap_dlink_set', repcap.Dlink.Ix1)

	def repcap_dlink_set(self, enum_value: repcap.Dlink) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Dlink.Default
		Default value after init: Dlink.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_dlink_get(self) -> repcap.Dlink:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, dlink_selection: bool, dlink=repcap.Dlink.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:TRACe:DLINk<Index> \n
		Snippet: driver.configure.data.measurement.throughput.ran.trace.dlink.set(dlink_selection = False, dlink = repcap.Dlink.Default) \n
		Enables or disables the downlink trace for RAN slot number <Index>. \n
			:param dlink_selection: OFF | ON
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')"""
		param = Conversions.bool_to_str(dlink_selection)
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TRACe:DLINk{dlink_cmd_val} {param}')

	def get(self, dlink=repcap.Dlink.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:THRoughput:RAN:TRACe:DLINk<Index> \n
		Snippet: value: bool = driver.configure.data.measurement.throughput.ran.trace.dlink.get(dlink = repcap.Dlink.Default) \n
		Enables or disables the downlink trace for RAN slot number <Index>. \n
			:param dlink: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Dlink')
			:return: dlink_selection: OFF | ON"""
		dlink_cmd_val = self._base.get_repcap_cmd_value(dlink, repcap.Dlink)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:THRoughput:RAN:TRACe:DLINk{dlink_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Dlink':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dlink(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
