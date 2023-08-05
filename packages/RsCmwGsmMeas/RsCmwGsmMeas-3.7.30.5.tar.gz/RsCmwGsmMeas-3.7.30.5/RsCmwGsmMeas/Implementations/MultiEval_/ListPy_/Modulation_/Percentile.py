from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Percentile:
	"""Percentile commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("percentile", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: GMSK | EPSK | ACCess | Q16 | OFF Detected burst type of the last measured burst GMSK: Normal burst, GMSK-modulated EPSK: Normal burst, 8PSK-modulated ACCess: Access burst Q16: Normal burst, 16-QAM-modulated OFF: Inactive slot
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm: List[float]: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Magnitude_Error: List[float]: float Magnitude error percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error: List[float]: float Phase error percentile Range: 0 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm', DataType.FloatList, None, False, True, 1),
			ArgStruct('Magnitude_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Evm: List[float] = None
			self.Magnitude_Error: List[float] = None
			self.Phase_Error: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:PERCentile \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.modulation.percentile.fetch() \n
		Returns the 95th percentile of the modulation results in list mode. The values listed below in curly brackets {} are
		returned for each measured segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the
		range of configured segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange.
		The values described below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance'
		result) are also returned by CALCulate commands. The remaining values returned by CALCulate commands are limit check
		results, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:PERCentile?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: GMSK | EPSK | ACCess | Q16 | OFF Detected burst type of the last measured burst GMSK: Normal burst, GMSK-modulated EPSK: Normal burst, 8PSK-modulated ACCess: Access burst Q16: Normal burst, 16-QAM-modulated OFF: Inactive slot
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm: List[enums.ResultStatus2]: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Magnitude_Error: List[enums.ResultStatus2]: float Magnitude error percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error: List[enums.ResultStatus2]: float Phase error percentile Range: 0 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Magnitude_Error', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Phase_Error', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Evm: List[enums.ResultStatus2] = None
			self.Magnitude_Error: List[enums.ResultStatus2] = None
			self.Phase_Error: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:PERCentile \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.modulation.percentile.calculate() \n
		Returns the 95th percentile of the modulation results in list mode. The values listed below in curly brackets {} are
		returned for each measured segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the
		range of configured segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange.
		The values described below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance'
		result) are also returned by CALCulate commands. The remaining values returned by CALCulate commands are limit check
		results, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:PERCentile?', self.__class__.CalculateStruct())
