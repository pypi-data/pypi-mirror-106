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
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.average.fetch() \n
		Returns the values of the magnitude error traces. The results of the current, average and minimum/maximum traces can be
		retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n magnitude error results, depending on the type of modulation 8PSK/16-QAM modulation: 142 values (one value per symbol period, symbol 3 to symbol 144) GMSK modulation: 588 values (four values per symbol period, symbol 0.5 to symbol 147.5) Access burst: 348 values (four values per symbol period, symbol 0.5 to symbol 87.5) Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage \n
		Snippet: value: List[float] = driver.multiEval.trace.merror.average.read() \n
		Returns the values of the magnitude error traces. The results of the current, average and minimum/maximum traces can be
		retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n magnitude error results, depending on the type of modulation 8PSK/16-QAM modulation: 142 values (one value per symbol period, symbol 3 to symbol 144) GMSK modulation: 588 values (four values per symbol period, symbol 0.5 to symbol 147.5) Access burst: 348 values (four values per symbol period, symbol 0.5 to symbol 87.5) Range: -100 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:TRACe:MERRor:AVERage?', suppressed)
		return response
