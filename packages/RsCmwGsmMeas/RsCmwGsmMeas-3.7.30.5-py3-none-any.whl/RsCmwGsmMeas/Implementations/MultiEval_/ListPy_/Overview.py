from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Overview:
	"""Overview commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("overview", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Segm_Reliability: List[int]: No parameter help available
			- Out_Of_Tol: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Avg_Burst_Power: List[float]: No parameter help available
			- Evm_Rms_Avg: List[float]: No parameter help available
			- Evm_Peak_Max: List[float]: No parameter help available
			- Evm_95_Perc: List[float]: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error_Rms_Avg: List[float]: No parameter help available
			- Phase_Error_Peak_Max: List[float]: No parameter help available
			- Iq_Offset_Avg: List[float]: No parameter help available
			- Frequency_Error_Avg: List[float]: No parameter help available
			- Spec_Mod_Offs_N_5: List[float]: No parameter help available
			- Spec_Mod_Offs_N_4: List[float]: No parameter help available
			- Spec_Mod_Carrier: List[float]: No parameter help available
			- Spec_Mod_Offs_P_4: List[float]: No parameter help available
			- Spec_Mod_Offs_P_5: List[float]: No parameter help available
			- Spec_Switch_Offs_N_2: List[float]: No parameter help available
			- Spec_Switch_Offs_N_1: List[float]: No parameter help available
			- Spec_Switch_Carrier: List[float]: No parameter help available
			- Spec_Switch_Offs_P_1: List[float]: No parameter help available
			- Spec_Switch_Offs_P_2: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Segm_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Out_Of_Tol', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Avg_Burst_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Rms_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak_Max', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_95_Perc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Rms_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Peak_Max', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Frequency_Error_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_N_5', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_N_4', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Carrier', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_P_4', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_P_5', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Switch_Offs_N_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Switch_Offs_N_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Switch_Carrier', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Switch_Offs_P_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Switch_Offs_P_2', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Segm_Reliability: List[int] = None
			self.Out_Of_Tol: List[int] = None
			self.Avg_Burst_Power: List[float] = None
			self.Evm_Rms_Avg: List[float] = None
			self.Evm_Peak_Max: List[float] = None
			self.Evm_95_Perc: List[float] = None
			self.Phase_Error_Rms_Avg: List[float] = None
			self.Phase_Error_Peak_Max: List[float] = None
			self.Iq_Offset_Avg: List[float] = None
			self.Frequency_Error_Avg: List[float] = None
			self.Spec_Mod_Offs_N_5: List[float] = None
			self.Spec_Mod_Offs_N_4: List[float] = None
			self.Spec_Mod_Carrier: List[float] = None
			self.Spec_Mod_Offs_P_4: List[float] = None
			self.Spec_Mod_Offs_P_5: List[float] = None
			self.Spec_Switch_Offs_N_2: List[float] = None
			self.Spec_Switch_Offs_N_1: List[float] = None
			self.Spec_Switch_Carrier: List[float] = None
			self.Spec_Switch_Offs_P_1: List[float] = None
			self.Spec_Switch_Offs_P_2: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:OVERview \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.overview.fetch() \n
		Returns all single results in list mode. The values listed below in curly brackets {} are returned for each measured
		segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of configured
		segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values described
		below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:OVERview?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Segm_Reliability: List[int]: No parameter help available
			- Out_Of_Tol: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Avg_Burst_Power: List[float]: No parameter help available
			- Evm_Rms_Avg: List[float]: No parameter help available
			- Evm_Peak_Max: List[float]: No parameter help available
			- Evm_95_Perc: List[float]: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error_Rms_Avg: List[float]: No parameter help available
			- Phase_Error_Peak_Max: List[float]: No parameter help available
			- Iq_Offset_Avg: List[float]: No parameter help available
			- Frequency_Error_Avg: List[float]: No parameter help available
			- Spec_Mod_Offs_N_5: List[enums.ResultStatus2]: No parameter help available
			- Spec_Mod_Offs_N_4: List[enums.ResultStatus2]: No parameter help available
			- Spec_Mod_Carrier: List[float]: No parameter help available
			- Spec_Mod_Offs_P_4: List[enums.ResultStatus2]: No parameter help available
			- Spec_Mod_Offs_P_5: List[enums.ResultStatus2]: No parameter help available
			- Spec_Switch_Offs_N_2: List[enums.ResultStatus2]: No parameter help available
			- Spec_Switch_Offs_N_1: List[enums.ResultStatus2]: No parameter help available
			- Spec_Switch_Carrier: List[enums.ResultStatus2]: No parameter help available
			- Spec_Switch_Offs_P_1: List[enums.ResultStatus2]: No parameter help available
			- Spec_Switch_Offs_P_2: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Segm_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Out_Of_Tol', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Avg_Burst_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Rms_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak_Max', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_95_Perc', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Rms_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Peak_Max', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Frequency_Error_Avg', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_N_5', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Mod_Offs_N_4', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Mod_Carrier', DataType.FloatList, None, False, True, 1),
			ArgStruct('Spec_Mod_Offs_P_4', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Mod_Offs_P_5', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Switch_Offs_N_2', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Switch_Offs_N_1', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Switch_Carrier', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Switch_Offs_P_1', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('Spec_Switch_Offs_P_2', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Segm_Reliability: List[int] = None
			self.Out_Of_Tol: List[int] = None
			self.Avg_Burst_Power: List[float] = None
			self.Evm_Rms_Avg: List[float] = None
			self.Evm_Peak_Max: List[float] = None
			self.Evm_95_Perc: List[float] = None
			self.Phase_Error_Rms_Avg: List[float] = None
			self.Phase_Error_Peak_Max: List[float] = None
			self.Iq_Offset_Avg: List[float] = None
			self.Frequency_Error_Avg: List[float] = None
			self.Spec_Mod_Offs_N_5: List[enums.ResultStatus2] = None
			self.Spec_Mod_Offs_N_4: List[enums.ResultStatus2] = None
			self.Spec_Mod_Carrier: List[float] = None
			self.Spec_Mod_Offs_P_4: List[enums.ResultStatus2] = None
			self.Spec_Mod_Offs_P_5: List[enums.ResultStatus2] = None
			self.Spec_Switch_Offs_N_2: List[enums.ResultStatus2] = None
			self.Spec_Switch_Offs_N_1: List[enums.ResultStatus2] = None
			self.Spec_Switch_Carrier: List[enums.ResultStatus2] = None
			self.Spec_Switch_Offs_P_1: List[enums.ResultStatus2] = None
			self.Spec_Switch_Offs_P_2: List[enums.ResultStatus2] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:OVERview \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.overview.calculate() \n
		Returns all single results in list mode. The values listed below in curly brackets {} are returned for each measured
		segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of configured
		segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values described
		below are returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:OVERview?', self.__class__.CalculateStruct())
