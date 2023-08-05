from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prange:
	"""Prange commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prange", core, parent)

	# noinspection PyTypeChecker
	class PrangeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Start_Port: int: No parameter help available
			- End_Port: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Port'),
			ArgStruct.scalar_int('End_Port')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Port: int = None
			self.End_Port: int = None

	def set(self, structure: PrangeStruct, impairments=repcap.Impairments.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:PRANge \n
		Snippet: driver.configure.data.measurement.nimpairments.prange.set(value = [PROPERTY_STRUCT_NAME](), impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param structure: for set value, see the help for PrangeStruct structure arguments.
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')"""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		self._core.io.write_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:PRANge', structure)

	def get(self, impairments=repcap.Impairments.Default) -> PrangeStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:PRANge \n
		Snippet: value: PrangeStruct = driver.configure.data.measurement.nimpairments.prange.get(impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')
			:return: structure: for return value, see the help for PrangeStruct structure arguments."""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		return self._core.io.query_struct(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:PRANge?', self.__class__.PrangeStruct())
