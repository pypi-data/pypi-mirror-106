from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sswitching:
	"""Sswitching commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sswitching", core, parent)

	@property
	def plevel(self):
		"""plevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plevel'):
			from .Sswitching_.Plevel import Plevel
			self._plevel = Plevel(self._core, self._base)
		return self._plevel

	@property
	def mpoint(self):
		"""mpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpoint'):
			from .Sswitching_.Mpoint import Mpoint
			self._mpoint = Mpoint(self._core, self._base)
		return self._mpoint

	def clone(self) -> 'Sswitching':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sswitching(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
