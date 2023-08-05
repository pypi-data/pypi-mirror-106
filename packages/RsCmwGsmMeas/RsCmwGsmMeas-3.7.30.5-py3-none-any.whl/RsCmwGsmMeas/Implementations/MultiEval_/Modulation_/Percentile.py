from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Percentile:
	"""Percentile commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("percentile", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tolerance: int: decimal Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Evm: enums.ResultStatus2: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Magnitude_Error: enums.ResultStatus2: float Magnitude error percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error: enums.ResultStatus2: float Phase error percentile Range: 0 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_enum('Evm', enums.ResultStatus2),
			ArgStruct.scalar_enum('Magnitude_Error', enums.ResultStatus2),
			ArgStruct.scalar_enum('Phase_Error', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm: enums.ResultStatus2 = None
			self.Magnitude_Error: enums.ResultStatus2 = None
			self.Phase_Error: enums.ResultStatus2 = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.percentile.calculate() \n
		Returns the 95th percentile results of the multi-evaluation measurement. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tolerance: int: decimal Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Evm: float: float Error vector magnitude percentile Range: 0 % to 100 %, Unit: %
			- Magnitude_Error: float: float Magnitude error percentile Range: 0 % to 100 %, Unit: %
			- Phase_Error: float: float Phase error percentile Range: 0 deg to 180 deg, Unit: deg"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Magnitude_Error'),
			ArgStruct.scalar_float('Phase_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm: float = None
			self.Magnitude_Error: float = None
			self.Phase_Error: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile \n
		Snippet: value: ResultData = driver.multiEval.modulation.percentile.fetch() \n
		Returns the 95th percentile results of the multi-evaluation measurement. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile \n
		Snippet: value: ResultData = driver.multiEval.modulation.percentile.read() \n
		Returns the 95th percentile results of the multi-evaluation measurement. The values described below are returned by FETCh
		and READ commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:MODulation:PERCentile?', self.__class__.ResultData())
