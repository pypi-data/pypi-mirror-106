from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tolerance: int: decimal Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:SMODulation CMDLINK]) exceeding the specified modulation limits. Range: 0 % to 100 %, Unit: %
			- Evm_Rms: float: float Error vector magnitude RMS and peak value Range: 0 % to 50 %, Unit: %
			- Evm_Peak: float: float Error vector magnitude RMS and peak value Range: 0 % to 50 %, Unit: %
			- Mag_Error_Rms: float: float Magnitude error RMS and peak value Range: 0 % to 50 %, Unit: %
			- Mag_Error_Peak: float: float Magnitude error RMS and peak value Range: 0 % to 50 %, Unit: %
			- Phase_Error_Rms: float: float Phase error RMS and peak value Range: 0 deg to 90 deg, Unit: deg
			- Phase_Error_Peak: float: float Phase error RMS and peak value Range: 0 deg to 90 deg, Unit: deg
			- Iq_Offset: float: float I/Q origin offset Range: 0 dB to 50 dB, Unit: dB
			- Iq_Imbalance: float: float I/Q imbalance Range: 0 dB to 50 dB, Unit: dB
			- Frequency_Error: float: float Carrier frequency error Range: 0 Hz to 56000 Hz, Unit: Hz
			- Timing_Error: float: float Transmit time error Range: 0 Sym to 100 Sym, Unit: Symbol
			- Burst_Power: float: float Burst power Range: 0 dB to 71 dB, Unit: dB
			- Am_Pm_Delay: float: float AMPM delay (determined for 8PSK and 16-QAM modulation only - for GMSK zeros are returned) Range: 0 s to 0.9225E-6 s, Unit: s"""
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
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.modulation.standardDev.fetch() \n
		Returns the standard deviation of the single slot modulation results of the multi-evaluation measurement. The number to
		the left of each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:SDEViation?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:MODulation:SDEViation \n
		Snippet: value: ResultData = driver.multiEval.modulation.standardDev.read() \n
		Returns the standard deviation of the single slot modulation results of the multi-evaluation measurement. The number to
		the left of each result parameter is provided for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:MODulation:SDEViation?', self.__class__.ResultData())
