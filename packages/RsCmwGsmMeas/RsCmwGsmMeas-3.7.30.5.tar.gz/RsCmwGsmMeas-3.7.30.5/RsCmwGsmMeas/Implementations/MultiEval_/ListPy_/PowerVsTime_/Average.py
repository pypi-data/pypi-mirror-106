from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Average_Burst_Pow: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Average_Burst_Pow', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Average_Burst_Pow: List[float] = None

	def fetch(self, segment_start: int = None, segment_count: int = None) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:AVERage \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.powerVsTime.average.fetch(segment_start = 1, segment_count = 1) \n
		Returns the power vs. time results in list mode. By default results are returned for all measured segments.
		Use the optional parameters to query only a subset. The values listed below in curly brackets {} are returned for each
		measured segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of
		configured segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values
		described below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance' result) are
		also returned by CALCulate commands. The remaining values returned by CALCulate commands are limit check results, one
		value for each result listed below. \n
			:param segment_start: integer First segment to be returned
			:param segment_count: integer Number of segments to be returned
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('segment_start', segment_start, DataType.Integer, True), ArgSingle('segment_count', segment_count, DataType.Integer, True))
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:AVERage? {param}'.rstrip(), self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Average_Burst_Pow: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Average_Burst_Pow', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Average_Burst_Pow: List[float] = None

	def calculate(self, segment_start: int = None, segment_count: int = None) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:AVERage \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.powerVsTime.average.calculate(segment_start = 1, segment_count = 1) \n
		Returns the power vs. time results in list mode. By default results are returned for all measured segments.
		Use the optional parameters to query only a subset. The values listed below in curly brackets {} are returned for each
		measured segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of
		configured segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values
		described below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance' result) are
		also returned by CALCulate commands. The remaining values returned by CALCulate commands are limit check results, one
		value for each result listed below. \n
			:param segment_start: integer First segment to be returned
			:param segment_count: integer Number of segments to be returned
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('segment_start', segment_start, DataType.Integer, True), ArgSingle('segment_count', segment_count, DataType.Integer, True))
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:AVERage? {param}'.rstrip(), self.__class__.CalculateStruct())
