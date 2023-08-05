from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcscf:
	"""Pcscf commands group definition. 9 total commands, 8 Sub-groups, 1 group commands
	Repeated Capability: PcscFnc, default value after init: PcscFnc.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcscf", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_pcscFnc_get', 'repcap_pcscFnc_set', repcap.PcscFnc.Nr1)

	def repcap_pcscFnc_set(self, enum_value: repcap.PcscFnc) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PcscFnc.Default
		Default value after init: PcscFnc.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_pcscFnc_get(self) -> repcap.PcscFnc:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def ipAddress(self):
		"""ipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipAddress'):
			from .Pcscf_.IpAddress import IpAddress
			self._ipAddress = IpAddress(self._core, self._base)
		return self._ipAddress

	@property
	def behaviour(self):
		"""behaviour commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_behaviour'):
			from .Pcscf_.Behaviour import Behaviour
			self._behaviour = Behaviour(self._core, self._base)
		return self._behaviour

	@property
	def failureCode(self):
		"""failureCode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_failureCode'):
			from .Pcscf_.FailureCode import FailureCode
			self._failureCode = FailureCode(self._core, self._base)
		return self._failureCode

	@property
	def retryAfter(self):
		"""retryAfter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_retryAfter'):
			from .Pcscf_.RetryAfter import RetryAfter
			self._retryAfter = RetryAfter(self._core, self._base)
		return self._retryAfter

	@property
	def regExp(self):
		"""regExp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_regExp'):
			from .Pcscf_.RegExp import RegExp
			self._regExp = RegExp(self._core, self._base)
		return self._regExp

	@property
	def subExp(self):
		"""subExp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subExp'):
			from .Pcscf_.SubExp import SubExp
			self._subExp = SubExp(self._core, self._base)
		return self._subExp

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Pcscf_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .Pcscf_.Create import Create
			self._create = Create(self._core, self._base)
		return self._create

	def delete(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:DELete \n
		Snippet: driver.configure.data.control.ims.pcscf.delete(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Deletes the P-CSCF profile number {p}. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:DELete')

	def delete_with_opc(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:DELete \n
		Snippet: driver.configure.data.control.ims.pcscf.delete_with_opc(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Deletes the P-CSCF profile number {p}. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:DELete')

	def clone(self) -> 'Pcscf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcscf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
