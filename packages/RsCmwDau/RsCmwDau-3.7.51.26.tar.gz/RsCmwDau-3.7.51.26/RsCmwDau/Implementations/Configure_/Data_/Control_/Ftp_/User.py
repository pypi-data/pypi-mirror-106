from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("user", core, parent)

	# noinspection PyTypeChecker
	class AddStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- User: str: User name as string
			- Password: str: Password as string
			- Delete_Allowed: bool: OFF | ON
			- Download_Allowed: bool: OFF | ON
			- Upload_Allowed: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_str('User'),
			ArgStruct.scalar_str('Password'),
			ArgStruct.scalar_bool('Delete_Allowed'),
			ArgStruct.scalar_bool('Download_Allowed'),
			ArgStruct.scalar_bool('Upload_Allowed')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.User: str = None
			self.Password: str = None
			self.Delete_Allowed: bool = None
			self.Download_Allowed: bool = None
			self.Upload_Allowed: bool = None

	def set_add(self, value: AddStruct) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:USER:ADD \n
		Snippet: driver.configure.data.control.ftp.user.set_add(value = AddStruct()) \n
		Creates an FTP user account. \n
			:param value: see the help for AddStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:CONTrol:FTP:USER:ADD', value)

	def delete(self, user: str, password: str = None) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:USER:DELete \n
		Snippet: driver.configure.data.control.ftp.user.delete(user = '1', password = '1') \n
		Deletes an FTP user account. \n
			:param user: FTP user name as string
			:param password: Password of the FTP user as string - supported for backward compatibility of the command, can be omitted
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('user', user, DataType.String), ArgSingle('password', password, DataType.String, True))
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:USER:DELete {param}'.rstrip())
