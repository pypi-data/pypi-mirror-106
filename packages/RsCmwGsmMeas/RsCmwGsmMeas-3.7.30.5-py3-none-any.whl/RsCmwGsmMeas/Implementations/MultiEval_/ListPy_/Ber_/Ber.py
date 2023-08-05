from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER:BER \n
		Snippet: value: List[float] = driver.multiEval.listPy.ber.ber.fetch() \n
		Returns the bit error rate for each measured list mode segment. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: ber: float Comma-separated list of values, one per measured segment Range: 0 % to 100 %, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER:BER?', suppressed)
		return response
