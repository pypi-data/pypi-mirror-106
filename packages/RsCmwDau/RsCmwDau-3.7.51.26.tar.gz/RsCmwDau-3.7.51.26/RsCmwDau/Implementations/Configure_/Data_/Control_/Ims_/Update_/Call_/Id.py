from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("id", core, parent)

	def set(self, idn: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:ID \n
		Snippet: driver.configure.data.control.ims.update.call.id.set(idn = '1', ims = repcap.Ims.Default) \n
		Selects the call to be updated. To query a list of IDs, see method RsCmwDau.Configure.Data.Control.Ims.Release.Call.Id.
		set. All other UPDate commands affect the call selected via this command. \n
			:param idn: Call ID as string, selecting the call to be updated
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(idn)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:ID {param}')

	def get(self, ims=repcap.Ims.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:ID \n
		Snippet: value: str = driver.configure.data.control.ims.update.call.id.get(ims = repcap.Ims.Default) \n
		Selects the call to be updated. To query a list of IDs, see method RsCmwDau.Configure.Data.Control.Ims.Release.Call.Id.
		set. All other UPDate commands affect the call selected via this command. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: idn: Call ID as string, selecting the call to be updated"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:ID?')
		return trim_str_response(response)
