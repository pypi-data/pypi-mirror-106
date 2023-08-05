from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msd:
	"""Msd commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msd", core, parent)

	@property
	def extended(self):
		"""extended commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_extended'):
			from .Msd_.Extended import Extended
			self._extended = Extended(self._core, self._base)
		return self._extended

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Count: int: No parameter help available
			- Msd: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Count'),
			ArgStruct('Msd', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: int = None
			self.Msd: List[int] = None

	def get(self, call_id: str, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:ECALl:MSD \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.ecall.msd.get(call_id = '1', ims = repcap.Ims.Default) \n
		No command help available \n
			:param call_id: No help available
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_quoted_str(call_id)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:ECALl:MSD? {param}', self.__class__.GetStruct())

	def clone(self) -> 'Msd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Msd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
