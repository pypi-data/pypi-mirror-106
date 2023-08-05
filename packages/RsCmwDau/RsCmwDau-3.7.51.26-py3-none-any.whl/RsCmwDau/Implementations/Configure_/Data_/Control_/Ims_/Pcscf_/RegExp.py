from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RegExp:
	"""RegExp commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("regExp", core, parent)

	# noinspection PyTypeChecker
	class RegExpStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Reg_Exp_Min: int: Minimum acceptable expiration time Unit: s
			- Reg_Exp_Default: int: Default value, used if the DUT does not suggest an expiration time Unit: s
			- Reg_Exp_Max: int: Maximum acceptable expiration time Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reg_Exp_Min'),
			ArgStruct.scalar_int('Reg_Exp_Default'),
			ArgStruct.scalar_int('Reg_Exp_Max')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reg_Exp_Min: int = None
			self.Reg_Exp_Default: int = None
			self.Reg_Exp_Max: int = None

	def set(self, structure: RegExpStruct, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:REGexp \n
		Snippet: driver.configure.data.control.ims.pcscf.regExp.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines registration expiration times for the P-CSCF number {p}. \n
			:param structure: for set value, see the help for RegExpStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:REGexp', structure)

	def get(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> RegExpStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:REGexp \n
		Snippet: value: RegExpStruct = driver.configure.data.control.ims.pcscf.regExp.get(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines registration expiration times for the P-CSCF number {p}. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')
			:return: structure: for return value, see the help for RegExpStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:REGexp?', self.__class__.RegExpStruct())
