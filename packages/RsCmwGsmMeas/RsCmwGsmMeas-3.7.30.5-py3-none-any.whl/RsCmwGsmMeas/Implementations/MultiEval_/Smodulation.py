from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smodulation:
	"""Smodulation commands group definition. 7 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smodulation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_frequency'):
			from .Smodulation_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Out_Of_Tol_Count: float: float Percentage of measurement intervals / bursts of the statistic count ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:SMODulation CMDLINK]) exceeding the specified limits (see 'Limits (Spectrum Modulation) ') . Range: 0 % to 100 %, Unit: %
			- Carrier_Power: float: float Measured carrier output power (reference power) Range: -100 dBm to 55 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol_Count'),
			ArgStruct.scalar_float('Carrier_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol_Count: float = None
			self.Carrier_Power: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:SMODulation \n
		Snippet: value: ResultData = driver.multiEval.smodulation.fetch() \n
		Returns general spectrum modulation results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:SMODulation?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:SMODulation \n
		Snippet: value: ResultData = driver.multiEval.smodulation.read() \n
		Returns general spectrum modulation results. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:SMODulation?', self.__class__.ResultData())

	def clone(self) -> 'Smodulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Smodulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
