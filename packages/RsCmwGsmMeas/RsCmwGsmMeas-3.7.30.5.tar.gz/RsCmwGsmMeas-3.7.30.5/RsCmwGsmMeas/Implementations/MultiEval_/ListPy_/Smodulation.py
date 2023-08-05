from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smodulation:
	"""Smodulation commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smodulation", core, parent)

	@property
	def cpower(self):
		"""cpower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cpower'):
			from .Smodulation_.Cpower import Cpower
			self._cpower = Cpower(self._core, self._base)
		return self._cpower

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_poffset'):
			from .Smodulation_.Poffset import Poffset
			self._poffset = Poffset(self._core, self._base)
		return self._poffset

	def clone(self) -> 'Smodulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Smodulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
