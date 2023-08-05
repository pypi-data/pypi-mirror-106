from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prange:
	"""Prange commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prange", core, parent)

	# noinspection PyTypeChecker
	class PrangeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Start_Port: int: Range: 0 to 65535
			- End_Port: int: Range: 0 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Port'),
			ArgStruct.scalar_int('End_Port')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Port: int = None
			self.End_Port: int = None

	def set(self, structure: PrangeStruct, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:PRANge \n
		Snippet: driver.configure.data.measurement.qos.filterPy.prange.set(value = [PROPERTY_STRUCT_NAME](), fltr = repcap.Fltr.Default) \n
		Specifies a destination port range as filter criterion for IP packets. To disable destination port filtering, set both
		values to zero. \n
			:param structure: for set value, see the help for PrangeStruct structure arguments.
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:PRANge', structure)

	def get(self, fltr=repcap.Fltr.Default) -> PrangeStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:PRANge \n
		Snippet: value: PrangeStruct = driver.configure.data.measurement.qos.filterPy.prange.get(fltr = repcap.Fltr.Default) \n
		Specifies a destination port range as filter criterion for IP packets. To disable destination port filtering, set both
		values to zero. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: structure: for return value, see the help for PrangeStruct structure arguments."""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		return self._core.io.query_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:PRANge?', self.__class__.PrangeStruct())
