from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qam:
	"""Qam commands group definition. 19 total commands, 10 Sub-groups, 0 group commands
	Repeated Capability: QamOrder, default value after init: QamOrder.Nr16"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qam", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_qamOrder_get', 'repcap_qamOrder_set', repcap.QamOrder.Nr16)

	def repcap_qamOrder_set(self, enum_value: repcap.QamOrder) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to QamOrder.Default
		Default value after init: QamOrder.Nr16"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_qamOrder_get(self) -> repcap.QamOrder:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .Qam_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .Qam_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_merror'):
			from .Qam_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Qam_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Qam_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .Qam_.IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._base)
		return self._iqImbalance

	@property
	def terror(self):
		"""terror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_terror'):
			from .Qam_.Terror import Terror
			self._terror = Terror(self._core, self._base)
		return self._terror

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqError'):
			from .Qam_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	@property
	def smodulation(self):
		"""smodulation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_smodulation'):
			from .Qam_.Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._base)
		return self._smodulation

	@property
	def sswitching(self):
		"""sswitching commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sswitching'):
			from .Qam_.Sswitching import Sswitching
			self._sswitching = Sswitching(self._core, self._base)
		return self._sswitching

	def clone(self) -> 'Qam':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qam(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
