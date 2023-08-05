from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offered:
	"""Offered commands group definition. 7 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("offered", core, parent)

	@property
	def srIndication(self):
		"""srIndication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srIndication'):
			from .Offered_.SrIndication import SrIndication
			self._srIndication = SrIndication(self._core, self._base)
		return self._srIndication

	@property
	def ecurve(self):
		"""ecurve commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecurve'):
			from .Offered_.Ecurve import Ecurve
			self._ecurve = Ecurve(self._core, self._base)
		return self._ecurve

	@property
	def cipSuite(self):
		"""cipSuite commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cipSuite'):
			from .Offered_.CipSuite import CipSuite
			self._cipSuite = CipSuite(self._core, self._base)
		return self._cipSuite

	@property
	def shAlgorithm(self):
		"""shAlgorithm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shAlgorithm'):
			from .Offered_.ShAlgorithm import ShAlgorithm
			self._shAlgorithm = ShAlgorithm(self._core, self._base)
		return self._shAlgorithm

	@property
	def version(self):
		"""version commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_version'):
			from .Offered_.Version import Version
			self._version = Version(self._core, self._base)
		return self._version

	@property
	def compression(self):
		"""compression commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_compression'):
			from .Offered_.Compression import Compression
			self._compression = Compression(self._core, self._base)
		return self._compression

	@property
	def ecpFormat(self):
		"""ecpFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecpFormat'):
			from .Offered_.EcpFormat import EcpFormat
			self._ecpFormat = EcpFormat(self._core, self._base)
		return self._ecpFormat

	def clone(self) -> 'Offered':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offered(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
