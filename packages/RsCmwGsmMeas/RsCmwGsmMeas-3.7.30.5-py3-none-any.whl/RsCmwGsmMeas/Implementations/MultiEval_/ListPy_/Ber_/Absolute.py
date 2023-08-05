from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("absolute", core, parent)

	def fetch(self) -> List[int or bool]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER:ABSolute \n
		Snippet: value: List[int or bool] = driver.multiEval.listPy.ber.absolute.fetch() \n
		Returns the total number of detected bit errors for each measured list mode segment. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: ber_absolute: Comma-separated list of values, one per measured segment Range: 0 to no. of measured bits"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER:ABSolute?', suppressed)
		return Conversions.str_to_int_or_bool_list(response)
