from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alignment:
	"""Alignment commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("alignment", core, parent)

	def set(self, amr_alignment: enums.AlignMode, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:AMR:ALIGnment \n
		Snippet: driver.configure.data.control.ims.update.amr.alignment.set(amr_alignment = enums.AlignMode.BANDwidtheff, ims = repcap.Ims.Default) \n
		Selects the new AMR voice codec alignment mode for a call update. \n
			:param amr_alignment: OCTetaligned | BANDwidtheff OCTetaligned: octet-aligned BANDwidtheff: bandwidth-efficient
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(amr_alignment, enums.AlignMode)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:AMR:ALIGnment {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.AlignMode:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:AMR:ALIGnment \n
		Snippet: value: enums.AlignMode = driver.configure.data.control.ims.update.amr.alignment.get(ims = repcap.Ims.Default) \n
		Selects the new AMR voice codec alignment mode for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: amr_alignment: OCTetaligned | BANDwidtheff OCTetaligned: octet-aligned BANDwidtheff: bandwidth-efficient"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:AMR:ALIGnment?')
		return Conversions.str_to_scalar_enum(response, enums.AlignMode)
