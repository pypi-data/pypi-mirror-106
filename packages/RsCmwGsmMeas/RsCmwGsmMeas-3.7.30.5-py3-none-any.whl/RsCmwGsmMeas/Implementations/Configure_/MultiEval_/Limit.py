from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 59 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .Limit_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	@property
	def gmsk(self):
		"""gmsk commands group. 3 Sub-classes, 7 commands."""
		if not hasattr(self, '_gmsk'):
			from .Limit_.Gmsk import Gmsk
			self._gmsk = Gmsk(self._core, self._base)
		return self._gmsk

	@property
	def epsk(self):
		"""epsk commands group. 3 Sub-classes, 7 commands."""
		if not hasattr(self, '_epsk'):
			from .Limit_.Epsk import Epsk
			self._epsk = Epsk(self._core, self._base)
		return self._epsk

	@property
	def qam(self):
		"""qam commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Limit_.Qam import Qam
			self._qam = Qam(self._core, self._base)
		return self._qam

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
