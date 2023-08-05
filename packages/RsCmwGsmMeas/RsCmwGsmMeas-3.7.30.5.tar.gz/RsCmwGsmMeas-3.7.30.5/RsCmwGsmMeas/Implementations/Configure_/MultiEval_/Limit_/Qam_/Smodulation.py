from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smodulation:
	"""Smodulation commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smodulation", core, parent)

	@property
	def rpower(self):
		"""rpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpower'):
			from .Smodulation_.Rpower import Rpower
			self._rpower = Rpower(self._core, self._base)
		return self._rpower

	@property
	def mpoint(self):
		"""mpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpoint'):
			from .Smodulation_.Mpoint import Mpoint
			self._mpoint = Mpoint(self._core, self._base)
		return self._mpoint

	def clone(self) -> 'Smodulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Smodulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
