from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Percentile:
	"""Percentile commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("percentile", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MERRor:PERCentile \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.merror.percentile.fetch() \n
		Return magnitude error 95th percentile values for all measured list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: magnitude_error: float Comma-separated list of values, one per measured segment Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MERRor:PERCentile?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MERRor:PERCentile \n
		Snippet: value: List[float] = driver.multiEval.listPy.modulation.merror.percentile.calculate() \n
		Return magnitude error 95th percentile values for all measured list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: magnitude_error: float Comma-separated list of values, one per measured segment Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:MODulation:MERRor:PERCentile?', suppressed)
		return response
