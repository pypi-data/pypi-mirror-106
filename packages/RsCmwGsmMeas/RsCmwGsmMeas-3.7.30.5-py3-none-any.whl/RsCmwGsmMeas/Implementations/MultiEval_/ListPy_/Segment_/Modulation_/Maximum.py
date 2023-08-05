from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


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
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: int: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: enums.SlotInfo: No parameter help available
			- Slot_Statistic: bool: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: int: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: float: float Carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: float: float Transmit time error Range: -100 Symbol to 100 Symbol, Unit: Symbol
			- Burst_Power: float: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: float: float AM-PM delay, determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned Range: -0.9225E-6 s to 0.9225E-6 s (a quarter of a symbol period) , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_enum('Slot_Info', enums.SlotInfo),
			ArgStruct.scalar_bool('Slot_Statistic'),
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
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Slot_Info: enums.SlotInfo = None
			self.Slot_Statistic: bool = None
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

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.maximum.fetch(segment = repcap.Segment.Default) \n
		Returns the modulation results for segment <no> in list mode. The values described below are returned by FETCh commands.
		The first six values ('Reliability' to 'Out of Tolerance' result) are also returned by CALCulate commands. The remaining
		values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:MAXimum?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: int: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: enums.SlotInfo: No parameter help available
			- Slot_Statistic: bool: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: int: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS value Range: 0 % to 100 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error peak value Range: -100 % to 100 % (AVERage: 0% to 100 %, SDEViation: 0 % to 50 %) , Unit: %
			- Phase_Error_Rms: float: No parameter help available
			- Phase_Error_Peak: float: No parameter help available
			- Iq_Offset: float: float I/Q origin offset Range: -100 dB to 0 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: -100 dB to 0 dB, Unit: dB
			- Frequency_Error: float: float Carrier frequency error Range: -56000 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: float: float Transmit time error Range: -100 Symbol to 100 Symbol, Unit: Symbol
			- Burst_Power: float: float Burst power Range: -100 dBm to 55 dBm, Unit: dBm
			- Am_Pm_Delay: float: float AM-PM delay, determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned Range: -0.9225E-6 s to 0.9225E-6 s (a quarter of a symbol period) , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_enum('Slot_Info', enums.SlotInfo),
			ArgStruct.scalar_bool('Slot_Statistic'),
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
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Slot_Info: enums.SlotInfo = None
			self.Slot_Statistic: bool = None
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

	def calculate(self, segment=repcap.Segment.Default) -> CalculateStruct:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.listPy.segment.modulation.maximum.calculate(segment = repcap.Segment.Default) \n
		Returns the modulation results for segment <no> in list mode. The values described below are returned by FETCh commands.
		The first six values ('Reliability' to 'Out of Tolerance' result) are also returned by CALCulate commands. The remaining
		values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:MAXimum?', self.__class__.CalculateStruct())
