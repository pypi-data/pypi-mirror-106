from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("user", core, parent)

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- User: List[str]: FTP user name as string
			- Delete_Allowed: List[bool]: OFF | ON OFF: delete forbidden ON: delete allowed
			- Download_Allowed: List[bool]: OFF | ON OFF: download forbidden ON: download allowed
			- Upload_Allowed: List[bool]: OFF | ON OFF: upload forbidden ON: upload allowed"""
		__meta_args_list = [
			ArgStruct('User', DataType.StringList, None, False, True, 1),
			ArgStruct('Delete_Allowed', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Download_Allowed', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Upload_Allowed', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.User: List[str] = None
			self.Delete_Allowed: List[bool] = None
			self.Download_Allowed: List[bool] = None
			self.Upload_Allowed: List[bool] = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: SENSe:DATA:CONTrol:FTP:USER:CATalog \n
		Snippet: value: CatalogStruct = driver.sense.data.control.ftp.user.get_catalog() \n
		Queries the existing FTP user accounts and their permissions. The four values listed below are returned for each FTP
		user: {<User>, <DeleteAllowed>, <DownloadAllowed>, <UploadAllowed>}user 1, {...}user 2, ..., {...}user n. \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:FTP:USER:CATalog?', self.__class__.CatalogStruct())
