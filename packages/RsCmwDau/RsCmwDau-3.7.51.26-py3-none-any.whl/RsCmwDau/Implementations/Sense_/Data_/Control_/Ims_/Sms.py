from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	@property
	def send(self):
		"""send commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_send'):
			from .Sms_.Send import Send
			self._send = Send(self._core, self._base)
		return self._send

	# noinspection PyTypeChecker
	class ReceivedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sms_Type: enums.SmsTypeB: No parameter help available
			- Sms_Text: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sms_Type', enums.SmsTypeB),
			ArgStruct.scalar_str('Sms_Text')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sms_Type: enums.SmsTypeB = None
			self.Sms_Text: str = None

	# noinspection PyTypeChecker
	def get_received(self) -> ReceivedStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS:SMS:RECeived \n
		Snippet: value: ReceivedStruct = driver.sense.data.control.ims.sms.get_received() \n
		No command help available \n
			:return: structure: for return value, see the help for ReceivedStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:IMS:SMS:RECeived?', self.__class__.ReceivedStruct())

	def clone(self) -> 'Sms':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sms(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
