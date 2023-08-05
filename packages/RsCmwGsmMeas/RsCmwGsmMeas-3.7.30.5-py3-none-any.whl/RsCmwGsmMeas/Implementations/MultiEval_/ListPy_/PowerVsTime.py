from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTime:
	"""PowerVsTime commands group definition. 21 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("powerVsTime", core, parent)

	@property
	def abPower(self):
		"""abPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_abPower'):
			from .PowerVsTime_.AbPower import AbPower
			self._abPower = AbPower(self._core, self._base)
		return self._abPower

	@property
	def svector(self):
		"""svector commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_svector'):
			from .PowerVsTime_.Svector import Svector
			self._svector = Svector(self._core, self._base)
		return self._svector

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .PowerVsTime_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def current(self):
		"""current commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .PowerVsTime_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'PowerVsTime':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerVsTime(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
