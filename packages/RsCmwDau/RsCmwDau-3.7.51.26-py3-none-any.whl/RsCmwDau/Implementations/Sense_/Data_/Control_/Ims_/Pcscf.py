from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcscf:
	"""Pcscf commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcscf", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Pcscf_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	# noinspection PyTypeChecker
	def get_status(self) -> enums.PcScfStatus:
		"""SCPI: SENSe:DATA:CONTrol:IMS:PCSCf:STATus \n
		Snippet: value: enums.PcScfStatus = driver.sense.data.control.ims.pcscf.get_status() \n
		No command help available \n
			:return: status: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:PCSCf:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.PcScfStatus)

	def clone(self) -> 'Pcscf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pcscf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
