from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Susage:
	"""Susage commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("susage", core, parent)

	def set(self, server_usage: enums.SourceInt, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUSage \n
		Snippet: driver.configure.data.control.ims.susage.set(server_usage = enums.SourceInt.EXTernal, ims = repcap.Ims.Default) \n
		Selects whether the internal IMS server of the DAU or an external IMS network is used for IMS services. \n
			:param server_usage: INTernal | EXTernal
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(server_usage, enums.SourceInt)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUSage {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.SourceInt:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUSage \n
		Snippet: value: enums.SourceInt = driver.configure.data.control.ims.susage.get(ims = repcap.Ims.Default) \n
		Selects whether the internal IMS server of the DAU or an external IMS network is used for IMS services. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: server_usage: INTernal | EXTernal"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUSage?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)
