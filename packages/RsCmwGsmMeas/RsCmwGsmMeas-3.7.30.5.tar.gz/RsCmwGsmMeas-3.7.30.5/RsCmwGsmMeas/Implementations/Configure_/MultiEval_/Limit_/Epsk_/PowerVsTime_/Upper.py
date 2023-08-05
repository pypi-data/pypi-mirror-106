from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("upper", core, parent)

	@property
	def risingEdge(self):
		"""risingEdge commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_risingEdge'):
			from .Upper_.RisingEdge import RisingEdge
			self._risingEdge = RisingEdge(self._core, self._base)
		return self._risingEdge

	@property
	def upart(self):
		"""upart commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_upart'):
			from .Upper_.Upart import Upart
			self._upart = Upart(self._core, self._base)
		return self._upart

	@property
	def fallingEdge(self):
		"""fallingEdge commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallingEdge'):
			from .Upper_.FallingEdge import FallingEdge
			self._fallingEdge = FallingEdge(self._core, self._base)
		return self._fallingEdge

	def clone(self) -> 'Upper':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Upper(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
