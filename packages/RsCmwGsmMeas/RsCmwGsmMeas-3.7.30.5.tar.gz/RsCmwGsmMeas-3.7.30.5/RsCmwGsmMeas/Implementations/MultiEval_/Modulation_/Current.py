from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tolerance: int: decimal Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Evm_Rms: enums.ResultStatus2: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: enums.ResultStatus2: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: enums.ResultStatus2: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: enums.ResultStatus2: float Magnitude error peak value Range: -100 % to 100 %, Unit: %
			- Phase_Error_Rms: enums.ResultStatus2: float Phase error RMS value Range: 0 deg to 180 deg, Unit: deg
			- Phase_Error_Peak: enums.ResultStatus2: float Phase error peak value Range: -180 deg to 180 deg, Unit: deg
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: float: float Carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: float: float Transmit time error Range: -100 Sym to 100 Sym, Unit: Symbol
			- Burst_Power: float: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: float: float AM-PM delay (determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned) Range: -0.9225E-6 s to 0.9225E-6 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_enum('Evm_Rms', enums.ResultStatus2),
			ArgStruct.scalar_enum('Evm_Peak', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mag_Error_Rms', enums.ResultStatus2),
			ArgStruct.scalar_enum('Mag_Error_Peak', enums.ResultStatus2),
			ArgStruct.scalar_enum('Phase_Error_Rms', enums.ResultStatus2),
			ArgStruct.scalar_enum('Phase_Error_Peak', enums.ResultStatus2),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Am_Pm_Delay')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms: enums.ResultStatus2 = None
			self.Evm_Peak: enums.ResultStatus2 = None
			self.Mag_Error_Rms: enums.ResultStatus2 = None
			self.Mag_Error_Peak: enums.ResultStatus2 = None
			self.Phase_Error_Rms: enums.ResultStatus2 = None
			self.Phase_Error_Peak: enums.ResultStatus2 = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Burst_Power: float = None
			self.Am_Pm_Delay: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.current.calculate() \n
		Returns the current and minimum/maximum single slot modulation results of the multi-evaluation measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tolerance: int: decimal Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:MODulation CMDLINK]) exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 %, Unit: %
			- Phase_Error_Rms: float: float Phase error RMS value Range: 0 deg to 180 deg, Unit: deg
			- Phase_Error_Peak: float: float Phase error peak value Range: -180 deg to 180 deg, Unit: deg
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: float: float Carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: float: float Transmit time error Range: -100 Sym to 100 Sym, Unit: Symbol
			- Burst_Power: float: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: float: float AM-PM delay (determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned) Range: -0.9225E-6 s to 0.9225E-6 s, Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Evm_Rms'),
			ArgStruct.scalar_float('Evm_Peak'),
			ArgStruct.scalar_float('Mag_Error_Rms'),
			ArgStruct.scalar_float('Mag_Error_Peak'),
			ArgStruct.scalar_float('Phase_Error_Rms'),
			ArgStruct.scalar_float('Phase_Error_Peak'),
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Burst_Power'),
			ArgStruct.scalar_float('Am_Pm_Delay')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms: float = None
			self.Evm_Peak: float = None
			self.Mag_Error_Rms: float = None
			self.Mag_Error_Peak: float = None
			self.Phase_Error_Rms: float = None
			self.Phase_Error_Peak: float = None
			self.Iq_Offset: float = None
			self.Iq_Imbalance: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Burst_Power: float = None
			self.Am_Pm_Delay: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: ResultData = driver.multiEval.modulation.current.fetch() \n
		Returns the current and minimum/maximum single slot modulation results of the multi-evaluation measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent \n
		Snippet: value: ResultData = driver.multiEval.modulation.current.read() \n
		Returns the current and minimum/maximum single slot modulation results of the multi-evaluation measurement. The values
		described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:MODulation:CURRent?', self.__class__.ResultData())
