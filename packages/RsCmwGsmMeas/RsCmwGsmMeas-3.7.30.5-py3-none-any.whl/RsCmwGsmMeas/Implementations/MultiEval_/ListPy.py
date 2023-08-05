from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 157 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def sreliability(self):
		"""sreliability commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sreliability'):
			from .ListPy_.Sreliability import Sreliability
			self._sreliability = Sreliability(self._core, self._base)
		return self._sreliability

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .ListPy_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	@property
	def modulation(self):
		"""modulation commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .ListPy_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def smodulation(self):
		"""smodulation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_smodulation'):
			from .ListPy_.Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._base)
		return self._smodulation

	@property
	def sswitching(self):
		"""sswitching commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sswitching'):
			from .ListPy_.Sswitching import Sswitching
			self._sswitching = Sswitching(self._core, self._base)
		return self._sswitching

	@property
	def ber(self):
		"""ber commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ber'):
			from .ListPy_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def overview(self):
		"""overview commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_overview'):
			from .ListPy_.Overview import Overview
			self._overview = Overview(self._core, self._base)
		return self._overview

	@property
	def segment(self):
		"""segment commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
