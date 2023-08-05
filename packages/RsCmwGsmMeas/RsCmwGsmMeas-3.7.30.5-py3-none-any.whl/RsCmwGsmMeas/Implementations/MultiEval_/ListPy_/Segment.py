from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 22 total commands, 5 Sub-groups, 0 group commands
	Repeated Capability: Segment, default value after init: Segment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("segment", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_segment_get', 'repcap_segment_set', repcap.Segment.Nr1)

	def repcap_segment_set(self, enum_value: repcap.Segment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Segment.Default
		Default value after init: Segment.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_segment_get(self) -> repcap.Segment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .Segment_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	@property
	def modulation(self):
		"""modulation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Segment_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def smodulation(self):
		"""smodulation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_smodulation'):
			from .Segment_.Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._base)
		return self._smodulation

	@property
	def sswitching(self):
		"""sswitching commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sswitching'):
			from .Segment_.Sswitching import Sswitching
			self._sswitching = Sswitching(self._core, self._base)
		return self._sswitching

	@property
	def ber(self):
		"""ber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ber'):
			from .Segment_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
