from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RisingEdge:
	"""RisingEdge commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: RisingEdge, default value after init: RisingEdge.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("risingEdge", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_risingEdge_get', 'repcap_risingEdge_set', repcap.RisingEdge.Nr1)

	def repcap_risingEdge_set(self, enum_value: repcap.RisingEdge) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RisingEdge.Default
		Default value after init: RisingEdge.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_risingEdge_get(self) -> repcap.RisingEdge:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def static(self):
		"""static commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_static'):
			from .RisingEdge_.Static import Static
			self._static = Static(self._core, self._base)
		return self._static

	@property
	def dynamic(self):
		"""dynamic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dynamic'):
			from .RisingEdge_.Dynamic import Dynamic
			self._dynamic = Dynamic(self._core, self._base)
		return self._dynamic

	def clone(self) -> 'RisingEdge':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RisingEdge(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
