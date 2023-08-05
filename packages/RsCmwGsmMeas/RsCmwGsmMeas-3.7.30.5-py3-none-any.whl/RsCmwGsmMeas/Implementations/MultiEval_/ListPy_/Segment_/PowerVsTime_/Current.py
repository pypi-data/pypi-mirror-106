from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	@property
	def svector(self):
		"""svector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_svector'):
			from .Current_.Svector import Svector
			self._svector = Svector(self._core, self._base)
		return self._svector

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: int: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: enums.SlotInfo: No parameter help available
			- Slot_Statistic: bool: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: int: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Average_Burst_Pow: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_enum('Slot_Info', enums.SlotInfo),
			ArgStruct.scalar_bool('Slot_Statistic'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Average_Burst_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Slot_Info: enums.SlotInfo = None
			self.Slot_Statistic: bool = None
			self.Out_Of_Tolerance: int = None
			self.Average_Burst_Pow: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:PVTime:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.powerVsTime.current.fetch(segment = repcap.Segment.Default) \n
		Returns power vs. time results for segment <no> in list mode. The values described below are returned by FETCh commands.
		The first six values ('Reliability' to 'Out of Tolerance' result) are also returned by CALCulate commands. The remaining
		values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PVTime:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: int: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: enums.SlotInfo: No parameter help available
			- Slot_Statistic: bool: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: int: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Average_Burst_Pow: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_enum('Slot_Info', enums.SlotInfo),
			ArgStruct.scalar_bool('Slot_Statistic'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Average_Burst_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Slot_Info: enums.SlotInfo = None
			self.Slot_Statistic: bool = None
			self.Out_Of_Tolerance: int = None
			self.Average_Burst_Pow: float = None

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:PVTime:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.powerVsTime.current.calculate(segment = repcap.Segment.Default) \n
		Returns power vs. time results for segment <no> in list mode. The values described below are returned by FETCh commands.
		The first six values ('Reliability' to 'Out of Tolerance' result) are also returned by CALCulate commands. The remaining
		values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PVTime:CURRent?', self.__class__.CalculateStruct())

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
