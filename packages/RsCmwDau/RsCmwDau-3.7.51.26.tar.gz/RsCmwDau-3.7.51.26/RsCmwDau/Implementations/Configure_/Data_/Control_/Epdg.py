from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Epdg:
	"""Epdg commands group definition. 35 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("epdg", core, parent)

	@property
	def pcscf(self):
		"""pcscf commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcscf'):
			from .Epdg_.Pcscf import Pcscf
			self._pcscf = Pcscf(self._core, self._base)
		return self._pcscf

	@property
	def address(self):
		"""address commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_address'):
			from .Epdg_.Address import Address
			self._address = Address(self._core, self._base)
		return self._address

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_id'):
			from .Epdg_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	@property
	def ike(self):
		"""ike commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_ike'):
			from .Epdg_.Ike import Ike
			self._ike = Ike(self._core, self._base)
		return self._ike

	@property
	def esp(self):
		"""esp commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_esp'):
			from .Epdg_.Esp import Esp
			self._esp = Esp(self._core, self._base)
		return self._esp

	@property
	def dpd(self):
		"""dpd commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_dpd'):
			from .Epdg_.Dpd import Dpd
			self._dpd = Dpd(self._core, self._base)
		return self._dpd

	@property
	def authentic(self):
		"""authentic commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_authentic'):
			from .Epdg_.Authentic import Authentic
			self._authentic = Authentic(self._core, self._base)
		return self._authentic

	@property
	def certificate(self):
		"""certificate commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_certificate'):
			from .Epdg_.Certificate import Certificate
			self._certificate = Certificate(self._core, self._base)
		return self._certificate

	@property
	def connections(self):
		"""connections commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connections'):
			from .Epdg_.Connections import Connections
			self._connections = Connections(self._core, self._base)
		return self._connections

	@property
	def clean(self):
		"""clean commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clean'):
			from .Epdg_.Clean import Clean
			self._clean = Clean(self._core, self._base)
		return self._clean

	def clone(self) -> 'Epdg':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Epdg(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
