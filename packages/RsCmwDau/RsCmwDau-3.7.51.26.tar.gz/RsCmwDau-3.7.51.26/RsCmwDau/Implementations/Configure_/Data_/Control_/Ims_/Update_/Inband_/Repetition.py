from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Repetition:
	"""Repetition commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("repetition", core, parent)

	def set(self, repetition: enums.Repetition, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:REPetition \n
		Snippet: driver.configure.data.control.ims.update.inband.repetition.set(repetition = enums.Repetition.ENDLess, ims = repcap.Ims.Default) \n
		Selects whether a CMR is sent only once or continuously. \n
			:param repetition: ENDLess | ONCE
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repetition)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:REPetition {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.Repetition:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:INBand:REPetition \n
		Snippet: value: enums.Repetition = driver.configure.data.control.ims.update.inband.repetition.get(ims = repcap.Ims.Default) \n
		Selects whether a CMR is sent only once or continuously. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: repetition: ENDLess | ONCE"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:INBand:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repetition)
