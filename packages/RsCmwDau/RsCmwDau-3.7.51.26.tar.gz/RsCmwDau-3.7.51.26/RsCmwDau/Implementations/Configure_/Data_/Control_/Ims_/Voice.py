from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Voice:
	"""Voice commands group definition. 11 total commands, 3 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("voice", core, parent)

	@property
	def codec(self):
		"""codec commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_codec'):
			from .Voice_.Codec import Codec
			self._codec = Codec(self._core, self._base)
		return self._codec

	@property
	def mendPoint(self):
		"""mendPoint commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mendPoint'):
			from .Voice_.MendPoint import MendPoint
			self._mendPoint = MendPoint(self._core, self._base)
		return self._mendPoint

	@property
	def call(self):
		"""call commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_call'):
			from .Voice_.Call import Call
			self._call = Call(self._core, self._base)
		return self._call

	# noinspection PyTypeChecker
	def get_audio_routing(self) -> enums.AudioRouting:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:AUDiorouting \n
		Snippet: value: enums.AudioRouting = driver.configure.data.control.ims.voice.get_audio_routing() \n
		No command help available \n
			:return: audio_routing: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:AUDiorouting?')
		return Conversions.str_to_scalar_enum(response, enums.AudioRouting)

	def set_audio_routing(self, audio_routing: enums.AudioRouting) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:AUDiorouting \n
		Snippet: driver.configure.data.control.ims.voice.set_audio_routing(audio_routing = enums.AudioRouting.AUDioboard) \n
		No command help available \n
			:param audio_routing: No help available
		"""
		param = Conversions.enum_scalar_to_str(audio_routing, enums.AudioRouting)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:AUDiorouting {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.AvTypeA:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:TYPE \n
		Snippet: value: enums.AvTypeA = driver.configure.data.control.ims.voice.get_type_py() \n
		No command help available \n
			:return: call_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AvTypeA)

	def set_type_py(self, call_type: enums.AvTypeA) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:TYPE \n
		Snippet: driver.configure.data.control.ims.voice.set_type_py(call_type = enums.AvTypeA.AUDio) \n
		No command help available \n
			:param call_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(call_type, enums.AvTypeA)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:TYPE {param}')

	# noinspection PyTypeChecker
	def get_amr_type(self) -> enums.AmrType:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:AMRType \n
		Snippet: value: enums.AmrType = driver.configure.data.control.ims.voice.get_amr_type() \n
		No command help available \n
			:return: amr_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:AMRType?')
		return Conversions.str_to_scalar_enum(response, enums.AmrType)

	def set_amr_type(self, amr_type: enums.AmrType) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:AMRType \n
		Snippet: driver.configure.data.control.ims.voice.set_amr_type(amr_type = enums.AmrType.NARRowband) \n
		No command help available \n
			:param amr_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(amr_type, enums.AmrType)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:AMRType {param}')

	# noinspection PyTypeChecker
	def get_vcodec(self) -> enums.VideoCodec:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:VCODec \n
		Snippet: value: enums.VideoCodec = driver.configure.data.control.ims.voice.get_vcodec() \n
		No command help available \n
			:return: video_codec: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:VCODec?')
		return Conversions.str_to_scalar_enum(response, enums.VideoCodec)

	def set_vcodec(self, video_codec: enums.VideoCodec) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:VCODec \n
		Snippet: driver.configure.data.control.ims.voice.set_vcodec(video_codec = enums.VideoCodec.H263) \n
		No command help available \n
			:param video_codec: No help available
		"""
		param = Conversions.enum_scalar_to_str(video_codec, enums.VideoCodec)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:VCODec {param}')

	def get_loopback(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:LOOPback \n
		Snippet: value: bool = driver.configure.data.control.ims.voice.get_loopback() \n
		No command help available \n
			:return: use_loopback: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:LOOPback?')
		return Conversions.str_to_bool(response)

	def set_loopback(self, use_loopback: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:LOOPback \n
		Snippet: driver.configure.data.control.ims.voice.set_loopback(use_loopback = False) \n
		No command help available \n
			:param use_loopback: No help available
		"""
		param = Conversions.bool_to_str(use_loopback)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:LOOPback {param}')

	# noinspection PyTypeChecker
	def get_precondition(self) -> enums.VoicePrecondition:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:PRECondition \n
		Snippet: value: enums.VoicePrecondition = driver.configure.data.control.ims.voice.get_precondition() \n
		No command help available \n
			:return: voice_precon: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:VOICe:PRECondition?')
		return Conversions.str_to_scalar_enum(response, enums.VoicePrecondition)

	def set_precondition(self, voice_precon: enums.VoicePrecondition) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:VOICe:PRECondition \n
		Snippet: driver.configure.data.control.ims.voice.set_precondition(voice_precon = enums.VoicePrecondition.SIMPle) \n
		No command help available \n
			:param voice_precon: No help available
		"""
		param = Conversions.enum_scalar_to_str(voice_precon, enums.VoicePrecondition)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:VOICe:PRECondition {param}')

	def clone(self) -> 'Voice':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Voice(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
