from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AudioBoard:
	"""AudioBoard commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("audioBoard", core, parent)

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .AudioBoard_.Config import Config
			self._config = Config(self._core, self._base)
		return self._config

	# noinspection PyTypeChecker
	class AudioBoardStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Instance: enums.AudioInstance: No parameter help available
			- Dtx_Enable: bool: No parameter help available
			- Force_Mode_Nb: enums.ForceModeNb: No parameter help available
			- Force_Mode_Wb: enums.ForceModeWb: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Instance', enums.AudioInstance),
			ArgStruct.scalar_bool('Dtx_Enable'),
			ArgStruct.scalar_enum('Force_Mode_Nb', enums.ForceModeNb),
			ArgStruct.scalar_enum('Force_Mode_Wb', enums.ForceModeWb)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Instance: enums.AudioInstance = None
			self.Dtx_Enable: bool = None
			self.Force_Mode_Nb: enums.ForceModeNb = None
			self.Force_Mode_Wb: enums.ForceModeWb = None

	def set(self, structure: AudioBoardStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AUDioboard \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.audioBoard.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param structure: for set value, see the help for AudioBoardStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AUDioboard', structure)

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> AudioBoardStruct:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:AUDioboard \n
		Snippet: value: AudioBoardStruct = driver.configure.data.control.ims.virtualSubscriber.audioBoard.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: structure: for return value, see the help for AudioBoardStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		return self._core.io.query_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:AUDioboard?', self.__class__.AudioBoardStruct())

	def clone(self) -> 'AudioBoard':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AudioBoard(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
