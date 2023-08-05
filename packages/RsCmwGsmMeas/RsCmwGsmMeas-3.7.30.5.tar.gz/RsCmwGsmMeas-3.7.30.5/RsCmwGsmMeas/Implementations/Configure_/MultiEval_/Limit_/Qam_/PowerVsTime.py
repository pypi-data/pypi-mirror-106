from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTime:
	"""PowerVsTime commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("powerVsTime", core, parent)

	@property
	def upper(self):
		"""upper commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .PowerVsTime_.Upper import Upper
			self._upper = Upper(self._core, self._base)
		return self._upper

	@property
	def lower(self):
		"""lower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .PowerVsTime_.Lower import Lower
			self._lower = Lower(self._core, self._base)
		return self._lower

	def clone(self) -> 'PowerVsTime':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerVsTime(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
