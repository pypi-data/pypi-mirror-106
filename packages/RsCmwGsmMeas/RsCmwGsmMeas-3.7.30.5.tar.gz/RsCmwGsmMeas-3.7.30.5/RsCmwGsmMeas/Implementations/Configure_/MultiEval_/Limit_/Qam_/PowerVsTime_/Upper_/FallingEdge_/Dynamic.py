from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dynamic:
	"""Dynamic commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: RangePcl, default value after init: RangePcl.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dynamic", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_rangePcl_get', 'repcap_rangePcl_set', repcap.RangePcl.Nr1)

	def repcap_rangePcl_set(self, enum_value: repcap.RangePcl) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RangePcl.Default
		Default value after init: RangePcl.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_rangePcl_get(self) -> repcap.RangePcl:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class DynamicStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF | ON Disable or enable dynamic correction
			- Pcl_Start: float: numeric First PCL in PCL range Range: 0 to 31
			- Pcl_End: float: numeric Last PCL in PCL range (can be equal to PCLStart) Range: 0 to 31
			- Correction: float: numeric Correction value for power template Range: -100 dB to 100 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Pcl_Start'),
			ArgStruct.scalar_float('Pcl_End'),
			ArgStruct.scalar_float('Correction')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Pcl_Start: float = None
			self.Pcl_End: float = None
			self.Correction: float = None

	def set(self, structure: DynamicStruct, qamOrder=repcap.QamOrder.Default, fallingEdge=repcap.FallingEdge.Default, rangePcl=repcap.RangePcl.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PVTime:UPPer:FEDGe<nr>:DYNamic<Range> \n
		Snippet: driver.configure.multiEval.limit.qam.powerVsTime.upper.fallingEdge.dynamic.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default, fallingEdge = repcap.FallingEdge.Default, rangePcl = repcap.RangePcl.Default) \n
		These commands define and activate dynamic (PCL-dependent) corrections to the upper limit lines for the measured power vs.
		time. The corrections apply to the modulation schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) and to the three limit line
		sections: rising edge (REDGe) , useful part (UPARt) and falling edge (FEDGe) . Each limit line section consists of
		several areas (<no>) . Each dynamic correction is defined for up to five different PCL ranges (<Range>) ). \n
			:param structure: for set value, see the help for DynamicStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:param fallingEdge: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FallingEdge')
			:param rangePcl: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dynamic')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		fallingEdge_cmd_val = self._base.get_repcap_cmd_value(fallingEdge, repcap.FallingEdge)
		rangePcl_cmd_val = self._base.get_repcap_cmd_value(rangePcl, repcap.RangePcl)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:PVTime:UPPer:FEDGe{fallingEdge_cmd_val}:DYNamic{rangePcl_cmd_val}', structure)

	def get(self, qamOrder=repcap.QamOrder.Default, fallingEdge=repcap.FallingEdge.Default, rangePcl=repcap.RangePcl.Default) -> DynamicStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PVTime:UPPer:FEDGe<nr>:DYNamic<Range> \n
		Snippet: value: DynamicStruct = driver.configure.multiEval.limit.qam.powerVsTime.upper.fallingEdge.dynamic.get(qamOrder = repcap.QamOrder.Default, fallingEdge = repcap.FallingEdge.Default, rangePcl = repcap.RangePcl.Default) \n
		These commands define and activate dynamic (PCL-dependent) corrections to the upper limit lines for the measured power vs.
		time. The corrections apply to the modulation schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) and to the three limit line
		sections: rising edge (REDGe) , useful part (UPARt) and falling edge (FEDGe) . Each limit line section consists of
		several areas (<no>) . Each dynamic correction is defined for up to five different PCL ranges (<Range>) ). \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:param fallingEdge: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FallingEdge')
			:param rangePcl: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dynamic')
			:return: structure: for return value, see the help for DynamicStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		fallingEdge_cmd_val = self._base.get_repcap_cmd_value(fallingEdge, repcap.FallingEdge)
		rangePcl_cmd_val = self._base.get_repcap_cmd_value(rangePcl, repcap.RangePcl)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:PVTime:UPPer:FEDGe{fallingEdge_cmd_val}:DYNamic{rangePcl_cmd_val}?', self.__class__.DynamicStruct())

	def clone(self) -> 'Dynamic':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dynamic(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
