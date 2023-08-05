from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Svector:
	"""Svector commands group definition. 12 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("svector", core, parent)

	@property
	def uminimum(self):
		"""uminimum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_uminimum'):
			from .Svector_.Uminimum import Uminimum
			self._uminimum = Uminimum(self._core, self._base)
		return self._uminimum

	@property
	def umaximum(self):
		"""umaximum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_umaximum'):
			from .Svector_.Umaximum import Umaximum
			self._umaximum = Umaximum(self._core, self._base)
		return self._umaximum

	@property
	def subvector(self):
		"""subvector commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_subvector'):
			from .Svector_.Subvector import Subvector
			self._subvector = Subvector(self._core, self._base)
		return self._subvector

	def clone(self) -> 'Svector':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Svector(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
