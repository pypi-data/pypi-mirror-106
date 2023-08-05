from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 16 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evm", core, parent)

	@property
	def rms(self):
		"""rms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Evm_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Evm_.Peak import Peak
			self._peak = Peak(self._core, self._base)
		return self._peak

	@property
	def percentile(self):
		"""percentile commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_percentile'):
			from .Evm_.Percentile import Percentile
			self._percentile = Percentile(self._core, self._base)
		return self._percentile

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
