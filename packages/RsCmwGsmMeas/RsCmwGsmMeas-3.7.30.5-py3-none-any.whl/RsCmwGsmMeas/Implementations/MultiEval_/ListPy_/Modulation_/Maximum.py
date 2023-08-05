from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm_Rms: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: List[float]: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: List[float]: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %) , Unit: %
			- Phase_Error_Rms: List[float]: No parameter help available
			- Phase_Error_Peak: List[float]: No parameter help available
			- Iq_Offset: List[float]: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: List[float]: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: List[float]: float Average carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: List[float]: float Transmit time error Range: -100 Symbol to 100 Symbol, Unit: Symbol
			- Burst_Power: List[float]: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: List[float]: float AM-PM delay (determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned) Range: -0.9225E-6 s to 0.9225E-6 s (a quarter of a symbol period) , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Imbalance', DataType.FloatList, None, False, True, 1),
			ArgStruct('Frequency_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Timing_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Burst_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Am_Pm_Delay', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Evm_Rms: List[float] = None
			self.Evm_Peak: List[float] = None
			self.Mag_Error_Rms: List[float] = None
			self.Mag_Error_Peak: List[float] = None
			self.Phase_Error_Rms: List[float] = None
			self.Phase_Error_Peak: List[float] = None
			self.Iq_Offset: List[float] = None
			self.Iq_Imbalance: List[float] = None
			self.Frequency_Error: List[float] = None
			self.Timing_Error: List[float] = None
			self.Burst_Power: List[float] = None
			self.Am_Pm_Delay: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.modulation.maximum.fetch() \n
		Returns the modulation results in list mode. The values listed below in curly brackets {} are returned for each measured
		segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of configured
		segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values described
		below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance' result) are also returned
		by CALCulate commands. The remaining values returned by CALCulate commands are limit check results, one value for each
		result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MAXimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm_Rms: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: List[float]: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: List[float]: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: List[float]: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %) , Unit: %
			- Phase_Error_Rms: List[float]: No parameter help available
			- Phase_Error_Peak: List[float]: No parameter help available
			- Iq_Offset: List[float]: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: List[float]: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: List[float]: float Average carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: List[float]: float Transmit time error Range: -100 Symbol to 100 Symbol, Unit: Symbol
			- Burst_Power: List[float]: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: List[float]: float AM-PM delay (determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned) Range: -0.9225E-6 s to 0.9225E-6 s (a quarter of a symbol period) , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Evm_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Evm_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Mag_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Rms', DataType.FloatList, None, False, True, 1),
			ArgStruct('Phase_Error_Peak', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Imbalance', DataType.FloatList, None, False, True, 1),
			ArgStruct('Frequency_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Timing_Error', DataType.FloatList, None, False, True, 1),
			ArgStruct('Burst_Power', DataType.FloatList, None, False, True, 1),
			ArgStruct('Am_Pm_Delay', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Evm_Rms: List[float] = None
			self.Evm_Peak: List[float] = None
			self.Mag_Error_Rms: List[float] = None
			self.Mag_Error_Peak: List[float] = None
			self.Phase_Error_Rms: List[float] = None
			self.Phase_Error_Peak: List[float] = None
			self.Iq_Offset: List[float] = None
			self.Iq_Imbalance: List[float] = None
			self.Frequency_Error: List[float] = None
			self.Timing_Error: List[float] = None
			self.Burst_Power: List[float] = None
			self.Am_Pm_Delay: List[float] = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.modulation.maximum.calculate() \n
		Returns the modulation results in list mode. The values listed below in curly brackets {} are returned for each measured
		segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of configured
		segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. The values described
		below are returned by FETCh commands. The first six values ('Reliability' to 'Out of Tolerance' result) are also returned
		by CALCulate commands. The remaining values returned by CALCulate commands are limit check results, one value for each
		result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MAXimum?', self.__class__.CalculateStruct())
