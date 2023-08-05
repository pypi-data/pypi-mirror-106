from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:TRACe:SSWitching:TIME[:CURRent] \n
		Snippet: value: List[float] = driver.multiEval.trace.sswitching.time.current.read() \n
		Returns the spectrum due to switching trace values measured at a selected offset frequency (method RsCmwGsmMeas.Configure.
		MultiEval.Sswitching.tdfSelect) . \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n power results, 4 for each symbol period of all measured slots Range: -100 dBm to 55 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:TRACe:SSWitching:TIME:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:SSWitching:TIME[:CURRent] \n
		Snippet: value: List[float] = driver.multiEval.trace.sswitching.time.current.fetch() \n
		Returns the spectrum due to switching trace values measured at a selected offset frequency (method RsCmwGsmMeas.Configure.
		MultiEval.Sswitching.tdfSelect) . \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: results: float n power results, 4 for each symbol period of all measured slots Range: -100 dBm to 55 dBm, Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:TRACe:SSWitching:TIME:CURRent?', suppressed)
		return response
