from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MvThroughput:
	"""MvThroughput commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mvThroughput", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:MVTHroughput \n
		Snippet: value: float = driver.multiEval.mvThroughput.fetch() \n
		Returns the modulation view throughput, i.e. the percentage of measurement intervals where the detected burst pattern was
		found to correspond to the 'Modulation View' settings. See also 'Mod. View Throughput' \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: mv_throughput: float Modulation view throughput Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:MVTHroughput?', suppressed)
		return Conversions.str_to_float(response)
