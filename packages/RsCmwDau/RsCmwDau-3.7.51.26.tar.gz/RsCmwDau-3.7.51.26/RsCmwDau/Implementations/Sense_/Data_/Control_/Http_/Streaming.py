from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Streaming:
	"""Streaming commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("streaming", core, parent)

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tid: int: No parameter help available
			- Filename: str: No parameter help available
			- Container: str: No parameter help available
			- Duration: float: No parameter help available
			- Video_Codec: str: No parameter help available
			- Video_Data_Rate: float: No parameter help available
			- Video_Profile: str: No parameter help available
			- Video_Level: str: No parameter help available
			- Frame_Numerator: int: No parameter help available
			- Frame_Denominator: int: No parameter help available
			- Height: int: No parameter help available
			- Width: int: No parameter help available
			- Channel_Count: int: No parameter help available
			- Audio_Codec: str: No parameter help available
			- Audio_Data_Rate: float: No parameter help available
			- Audio_Sampling_Rate: int: No parameter help available
			- Data_Type: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Tid'),
			ArgStruct.scalar_str('Filename'),
			ArgStruct.scalar_str('Container'),
			ArgStruct.scalar_float('Duration'),
			ArgStruct.scalar_str('Video_Codec'),
			ArgStruct.scalar_float('Video_Data_Rate'),
			ArgStruct.scalar_str('Video_Profile'),
			ArgStruct.scalar_str('Video_Level'),
			ArgStruct.scalar_int('Frame_Numerator'),
			ArgStruct.scalar_int('Frame_Denominator'),
			ArgStruct.scalar_int('Height'),
			ArgStruct.scalar_int('Width'),
			ArgStruct.scalar_int('Channel_Count'),
			ArgStruct.scalar_str('Audio_Codec'),
			ArgStruct.scalar_float('Audio_Data_Rate'),
			ArgStruct.scalar_int('Audio_Sampling_Rate'),
			ArgStruct.scalar_str('Data_Type')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tid: int = None
			self.Filename: str = None
			self.Container: str = None
			self.Duration: float = None
			self.Video_Codec: str = None
			self.Video_Data_Rate: float = None
			self.Video_Profile: str = None
			self.Video_Level: str = None
			self.Frame_Numerator: int = None
			self.Frame_Denominator: int = None
			self.Height: int = None
			self.Width: int = None
			self.Channel_Count: int = None
			self.Audio_Codec: str = None
			self.Audio_Data_Rate: float = None
			self.Audio_Sampling_Rate: int = None
			self.Data_Type: str = None

	def get_result(self) -> ResultStruct:
		"""SCPI: SENSe:DATA:CONTrol:HTTP:STReaming:RESult \n
		Snippet: value: ResultStruct = driver.sense.data.control.http.streaming.get_result() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:HTTP:STReaming:RESult?', self.__class__.ResultStruct())
