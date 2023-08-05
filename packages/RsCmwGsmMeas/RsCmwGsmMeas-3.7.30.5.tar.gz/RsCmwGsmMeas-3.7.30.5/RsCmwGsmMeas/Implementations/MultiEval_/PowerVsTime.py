from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTime:
	"""PowerVsTime commands group definition. 10 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("powerVsTime", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_all'):
			from .PowerVsTime_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def tsc(self):
		"""tsc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsc'):
			from .PowerVsTime_.Tsc import Tsc
			self._tsc = Tsc(self._core, self._base)
		return self._tsc

	@property
	def btype(self):
		"""btype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_btype'):
			from .PowerVsTime_.Btype import Btype
			self._btype = Btype(self._core, self._base)
		return self._btype

	@property
	def rsTiming(self):
		"""rsTiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsTiming'):
			from .PowerVsTime_.RsTiming import RsTiming
			self._rsTiming = RsTiming(self._core, self._base)
		return self._rsTiming

	@property
	def current(self):
		"""current commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .PowerVsTime_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .PowerVsTime_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def minimum(self):
		"""minimum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .PowerVsTime_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def maximum(self):
		"""maximum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .PowerVsTime_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	def clone(self) -> 'PowerVsTime':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerVsTime(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
