from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 99 total commands, 14 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Modulation_.Evm import Evm
			self._evm = Evm(self._core, self._base)
		return self._evm

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Modulation_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Modulation_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def iqOffset(self):
		"""iqOffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Modulation_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .Modulation_.IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._base)
		return self._iqImbalance

	@property
	def freqError(self):
		"""freqError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .Modulation_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	@property
	def terror(self):
		"""terror commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_terror'):
			from .Modulation_.Terror import Terror
			self._terror = Terror(self._core, self._base)
		return self._terror

	@property
	def bpower(self):
		"""bpower commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpower'):
			from .Modulation_.Bpower import Bpower
			self._bpower = Bpower(self._core, self._base)
		return self._bpower

	@property
	def apDelay(self):
		"""apDelay commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_apDelay'):
			from .Modulation_.ApDelay import ApDelay
			self._apDelay = ApDelay(self._core, self._base)
		return self._apDelay

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Modulation_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Modulation_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Modulation_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standardDev'):
			from .Modulation_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def percentile(self):
		"""percentile commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_percentile'):
			from .Modulation_.Percentile import Percentile
			self._percentile = Percentile(self._core, self._base)
		return self._percentile

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
