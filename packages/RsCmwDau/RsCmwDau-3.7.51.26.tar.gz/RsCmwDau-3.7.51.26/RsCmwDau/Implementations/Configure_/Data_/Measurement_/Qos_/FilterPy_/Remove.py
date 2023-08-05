from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remove:
	"""Remove commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("remove", core, parent)

	def set(self, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:REMove \n
		Snippet: driver.configure.data.measurement.qos.filterPy.remove.set(fltr = repcap.Fltr.Default) \n
		Deletes the QoS profile number <Index>. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:REMove')

	def set_with_opc(self, fltr=repcap.Fltr.Default) -> None:
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:REMove \n
		Snippet: driver.configure.data.measurement.qos.filterPy.remove.set_with_opc(fltr = repcap.Fltr.Default) \n
		Deletes the QoS profile number <Index>. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:REMove')
