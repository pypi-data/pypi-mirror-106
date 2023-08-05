from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limits:
	"""Limits commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limits", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:SMODulation:FREQuency:LIMits \n
		Snippet: value: List[float] = driver.multiEval.smodulation.frequency.limits.fetch() \n
		Queries the limits for spectrum modulation frequency. See also method RsCmwGsmMeas.Configure.MultiEval.Smodulation.
		ofrequence \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: limit: float 41 values display limits at the following frequency offsets: values 1 to 20 = minus offset 19 to minus offset 0 value 21 = carrier frequency, no offset values 21 to 41 = plus offset 0 to plus offset 19 Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:SMODulation:FREQuency:LIMits?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:SMODulation:FREQuency:LIMits \n
		Snippet: value: List[float] = driver.multiEval.smodulation.frequency.limits.read() \n
		Queries the limits for spectrum modulation frequency. See also method RsCmwGsmMeas.Configure.MultiEval.Smodulation.
		ofrequence \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: limit: float 41 values display limits at the following frequency offsets: values 1 to 20 = minus offset 19 to minus offset 0 value 21 = carrier frequency, no offset values 21 to 41 = plus offset 0 to plus offset 19 Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:SMODulation:FREQuency:LIMits?', suppressed)
		return response
