from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.trace.evMagnitude.maximum.fetch() \n
		Returns the values of the EVM traces. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n EVM results, depending on the burst and modulation type 8PSK/16-QAM modulation: 142 values (one value per symbol period, symbol 3 to symbol 144) GMSK modulation: 588 values (four values per symbol period, symbol 0.5 to symbol 147.5) Access burst: 348 values (four values per symbol period, symbol 0.5 to symbol 87.5) Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:MAXimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:MAXimum \n
		Snippet: value: List[float] = driver.multiEval.trace.evMagnitude.maximum.read() \n
		Returns the values of the EVM traces. The results of the current, average and maximum traces can be retrieved. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n EVM results, depending on the burst and modulation type 8PSK/16-QAM modulation: 142 values (one value per symbol period, symbol 3 to symbol 144) GMSK modulation: 588 values (four values per symbol period, symbol 0.5 to symbol 147.5) Access burst: 348 values (four values per symbol period, symbol 0.5 to symbol 87.5) Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:TRACe:EVMagnitude:MAXimum?', suppressed)
		return response
