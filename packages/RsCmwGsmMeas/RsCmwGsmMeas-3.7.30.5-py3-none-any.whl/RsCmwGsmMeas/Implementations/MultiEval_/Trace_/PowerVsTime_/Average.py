from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:PVTime:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.powerVsTime.average.fetch() \n
		Returns the values of the power vs. time traces. 16 results are available for each symbol period of the measured slots
		(method RsCmwGsmMeas.Configure.MultiEval.mslots) . The trace covers 18.25 symbol periods before the beginning of the
		first slot in the measured slot range, 10 symbol periods after the end of the last measured slot. The length of the trace
		is given as: The first sample of the 'Measurement Slot' is at position m in the trace, where: The results of the current,
		average minimum and maximum traces can be retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float Range: -100 dB to 100 dB, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:PVTime:AVERage?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:TRACe:PVTime:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.powerVsTime.average.read() \n
		Returns the values of the power vs. time traces. 16 results are available for each symbol period of the measured slots
		(method RsCmwGsmMeas.Configure.MultiEval.mslots) . The trace covers 18.25 symbol periods before the beginning of the
		first slot in the measured slot range, 10 symbol periods after the end of the last measured slot. The length of the trace
		is given as: The first sample of the 'Measurement Slot' is at position m in the trace, where: The results of the current,
		average minimum and maximum traces can be retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float Range: -100 dB to 100 dB, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:TRACe:PVTime:AVERage?', suppressed)
		return response
