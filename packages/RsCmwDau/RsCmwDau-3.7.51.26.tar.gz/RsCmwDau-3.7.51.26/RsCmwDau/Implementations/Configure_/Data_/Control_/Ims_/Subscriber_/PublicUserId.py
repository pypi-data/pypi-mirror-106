from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PublicUserId:
	"""PublicUserId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: UserId, default value after init: UserId.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("publicUserId", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_userId_get', 'repcap_userId_set', repcap.UserId.Ix1)

	def repcap_userId_set(self, enum_value: repcap.UserId) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserId.Default
		Default value after init: UserId.Ix1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_userId_get(self) -> repcap.UserId:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, public_user_ids: str, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default, userId=repcap.UserId.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:PUBLicuserid<Index> \n
		Snippet: driver.configure.data.control.ims.subscriber.publicUserId.set(public_user_ids = '1', ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default, userId = repcap.UserId.Default) \n
		Defines public user ID number <Index> for the subscriber profile number <s>. \n
			:param public_user_ids: Public user ID as string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:param userId: optional repeated capability selector. Default value: Ix1 (settable in the interface 'PublicUserId')"""
		param = Conversions.value_to_quoted_str(public_user_ids)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		userId_cmd_val = self._base.get_repcap_cmd_value(userId, repcap.UserId)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:PUBLicuserid{userId_cmd_val} {param}')

	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default, userId=repcap.UserId.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:PUBLicuserid<Index> \n
		Snippet: value: str = driver.configure.data.control.ims.subscriber.publicUserId.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default, userId = repcap.UserId.Default) \n
		Defines public user ID number <Index> for the subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:param userId: optional repeated capability selector. Default value: Ix1 (settable in the interface 'PublicUserId')
			:return: public_user_ids: Public user ID as string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		userId_cmd_val = self._base.get_repcap_cmd_value(userId, repcap.UserId)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:PUBLicuserid{userId_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'PublicUserId':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PublicUserId(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
