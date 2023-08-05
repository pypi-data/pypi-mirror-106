from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Bursts_Out_Tol: float or bool: float Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:PVTime CMDLINK]) exceeding the specified limits, see 'Limits (Power vs. Time) ' Range: 0 % to 100 %, Unit: %
			- Avg_Burst_Pow_Avg: List[float]: No parameter help available
			- Avg_Burst_Pow_Cur: List[float]: No parameter help available
			- Max_Burst_Pow_Cur: List[float]: No parameter help available
			- Min_Burst_Pow_Cur: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Bursts_Out_Tol'),
			ArgStruct('Avg_Burst_Pow_Avg', DataType.FloatList, None, False, False, 8),
			ArgStruct('Avg_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8),
			ArgStruct('Max_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8),
			ArgStruct('Min_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Tol: float or bool = None
			self.Avg_Burst_Pow_Avg: List[float] = None
			self.Avg_Burst_Pow_Cur: List[float] = None
			self.Max_Burst_Pow_Cur: List[float] = None
			self.Min_Burst_Pow_Cur: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:PVTime[:ALL] \n
		Snippet: value: CalculateStruct = driver.multiEval.powerVsTime.all.calculate() \n
		Returns burst power values for slot 0 to slot 7. In addition to the current value statistical values are returned
		(average, minimum and maximum) . The relative number of bursts out of tolerance is also returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:PVTime:ALL?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Bursts_Out_Tol: float or bool: float Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:PVTime CMDLINK]) exceeding the specified limits, see 'Limits (Power vs. Time) ' Range: 0 % to 100 %, Unit: %
			- Avg_Burst_Pow_Avg: List[float or bool]: No parameter help available
			- Avg_Burst_Pow_Cur: List[float or bool]: No parameter help available
			- Max_Burst_Pow_Cur: List[float or bool]: No parameter help available
			- Min_Burst_Pow_Cur: List[float or bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Bursts_Out_Tol'),
			ArgStruct('Avg_Burst_Pow_Avg', DataType.FloatList, None, False, False, 8),
			ArgStruct('Avg_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8),
			ArgStruct('Max_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8),
			ArgStruct('Min_Burst_Pow_Cur', DataType.FloatList, None, False, False, 8)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Tol: float or bool = None
			self.Avg_Burst_Pow_Avg: List[float or bool] = None
			self.Avg_Burst_Pow_Cur: List[float or bool] = None
			self.Max_Burst_Pow_Cur: List[float or bool] = None
			self.Min_Burst_Pow_Cur: List[float or bool] = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime[:ALL] \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.all.fetch() \n
		Returns burst power values for slot 0 to slot 7. In addition to the current value statistical values are returned
		(average, minimum and maximum) . The relative number of bursts out of tolerance is also returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:ALL?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:PVTime[:ALL] \n
		Snippet: value: ResultData = driver.multiEval.powerVsTime.all.read() \n
		Returns burst power values for slot 0 to slot 7. In addition to the current value statistical values are returned
		(average, minimum and maximum) . The relative number of bursts out of tolerance is also returned. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:PVTime:ALL?', self.__class__.ResultData())
