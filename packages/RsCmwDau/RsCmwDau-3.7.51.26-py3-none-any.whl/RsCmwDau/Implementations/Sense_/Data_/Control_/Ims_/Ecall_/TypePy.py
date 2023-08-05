from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Type_Py: enums.EcallType: No parameter help available
			- Testcall: enums.Testcall: No parameter help available
			- Urn: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Type_Py', enums.EcallType),
			ArgStruct.scalar_enum('Testcall', enums.Testcall),
			ArgStruct.scalar_str('Urn')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Type_Py: enums.EcallType = None
			self.Testcall: enums.Testcall = None
			self.Urn: str = None

	def get(self, call_id: str, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:ECALl:TYPE \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.ecall.typePy.get(call_id = '1', ims = repcap.Ims.Default) \n
		No command help available \n
			:param call_id: No help available
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(call_id)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:ECALl:TYPE? {param}', self.__class__.GetStruct())
