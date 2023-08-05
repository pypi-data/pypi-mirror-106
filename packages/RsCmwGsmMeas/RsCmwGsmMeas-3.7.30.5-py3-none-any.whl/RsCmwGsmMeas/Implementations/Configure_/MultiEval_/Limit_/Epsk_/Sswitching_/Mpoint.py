from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpoint:
	"""Mpoint commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: MeasPoint, default value after init: MeasPoint.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mpoint", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_measPoint_get', 'repcap_measPoint_set', repcap.MeasPoint.Nr1)

	def repcap_measPoint_set(self, enum_value: repcap.MeasPoint) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MeasPoint.Default
		Default value after init: MeasPoint.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_measPoint_get(self) -> repcap.MeasPoint:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class MpointStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Limit: List[float]: No parameter help available
			- Enable: bool: OFF | ON ON: Enable limits for the given no OFF: Disable limits for the given no"""
		__meta_args_list = [
			ArgStruct('Limit', DataType.FloatList, None, False, False, 10),
			ArgStruct.scalar_bool('Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Limit: List[float] = None
			self.Enable: bool = None

	def set(self, structure: MpointStruct, measPoint=repcap.MeasPoint.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:SSWitching:MPOint<nr> \n
		Snippet: driver.configure.multiEval.limit.epsk.sswitching.mpoint.set(value = [PROPERTY_STRUCT_NAME](), measPoint = repcap.MeasPoint.Default) \n
		Define and activate a limit line for the modulation schemes 8PSK and 16-QAM for a certain frequency offset. The specified
		limits apply at the reference power values defined by method RsCmwGsmMeas.Configure.MultiEval.Limit.Epsk.Sswitching.
		plevel and method RsCmwGsmMeas.Configure.MultiEval.Limit.Qam.Sswitching.Plevel.set. Between the reference power values
		the limits are determined by linear interpolation. \n
			:param structure: for set value, see the help for MpointStruct structure arguments.
			:param measPoint: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpoint')"""
		measPoint_cmd_val = self._base.get_repcap_cmd_value(measPoint, repcap.MeasPoint)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:SSWitching:MPOint{measPoint_cmd_val}', structure)

	def get(self, measPoint=repcap.MeasPoint.Default) -> MpointStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:SSWitching:MPOint<nr> \n
		Snippet: value: MpointStruct = driver.configure.multiEval.limit.epsk.sswitching.mpoint.get(measPoint = repcap.MeasPoint.Default) \n
		Define and activate a limit line for the modulation schemes 8PSK and 16-QAM for a certain frequency offset. The specified
		limits apply at the reference power values defined by method RsCmwGsmMeas.Configure.MultiEval.Limit.Epsk.Sswitching.
		plevel and method RsCmwGsmMeas.Configure.MultiEval.Limit.Qam.Sswitching.Plevel.set. Between the reference power values
		the limits are determined by linear interpolation. \n
			:param measPoint: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mpoint')
			:return: structure: for return value, see the help for MpointStruct structure arguments."""
		measPoint_cmd_val = self._base.get_repcap_cmd_value(measPoint, repcap.MeasPoint)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:SSWitching:MPOint{measPoint_cmd_val}?', self.__class__.MpointStruct())

	def clone(self) -> 'Mpoint':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mpoint(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
