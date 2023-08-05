from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("event", core, parent)

	def set(self, update_call_event: enums.UpdateCallEvent, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:EVENt \n
		Snippet: driver.configure.data.control.ims.update.call.event.set(update_call_event = enums.UpdateCallEvent.HOLD, ims = repcap.Ims.Default) \n
		Puts a call on hold or resumes a call that has been put on hold. To select the call, use method RsCmwDau.Configure.Data.
		Control.Ims.Update.Call.Id.set. \n
			:param update_call_event: HOLD | RESume
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(update_call_event, enums.UpdateCallEvent)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:EVENt {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.UpdateCallEvent:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:CALL:EVENt \n
		Snippet: value: enums.UpdateCallEvent = driver.configure.data.control.ims.update.call.event.get(ims = repcap.Ims.Default) \n
		Puts a call on hold or resumes a call that has been put on hold. To select the call, use method RsCmwDau.Configure.Data.
		Control.Ims.Update.Call.Id.set. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: update_call_event: HOLD | RESume"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:CALL:EVENt?')
		return Conversions.str_to_scalar_enum(response, enums.UpdateCallEvent)
