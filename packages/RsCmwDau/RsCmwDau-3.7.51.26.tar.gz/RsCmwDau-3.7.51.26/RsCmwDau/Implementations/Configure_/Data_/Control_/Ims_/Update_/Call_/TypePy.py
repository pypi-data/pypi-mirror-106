from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("typePy", core, parent)

	def set(self, call_type: enums.AvTypeA, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:TYPE \n
		Snippet: driver.configure.data.control.ims.update.call.typePy.set(call_type = enums.AvTypeA.AUDio, ims = repcap.Ims.Default) \n
		Selects the new call type for a call update. \n
			:param call_type: AUDio | VIDeo
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(call_type, enums.AvTypeA)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.AvTypeA:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:TYPE \n
		Snippet: value: enums.AvTypeA = driver.configure.data.control.ims.update.call.typePy.get(ims = repcap.Ims.Default) \n
		Selects the new call type for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: call_type: AUDio | VIDeo"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AvTypeA)
