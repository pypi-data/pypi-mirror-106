from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StartMode:
	"""StartMode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("startMode", core, parent)

	def set(self, start_mode: enums.StartMode, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:STARtmode \n
		Snippet: driver.configure.data.control.ims.update.evs.startMode.set(start_mode = enums.StartMode.EAMRwbio, ims = repcap.Ims.Default) \n
		Selects the start mode for the EVS codec, for a call update. \n
			:param start_mode: EPRimary | EAMRwbio EVS primary or EVS AMR-WB IO
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(start_mode, enums.StartMode)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:STARtmode {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.StartMode:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:STARtmode \n
		Snippet: value: enums.StartMode = driver.configure.data.control.ims.update.evs.startMode.get(ims = repcap.Ims.Default) \n
		Selects the start mode for the EVS codec, for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: start_mode: EPRimary | EAMRwbio EVS primary or EVS AMR-WB IO"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:STARtmode?')
		return Conversions.str_to_scalar_enum(response, enums.StartMode)
