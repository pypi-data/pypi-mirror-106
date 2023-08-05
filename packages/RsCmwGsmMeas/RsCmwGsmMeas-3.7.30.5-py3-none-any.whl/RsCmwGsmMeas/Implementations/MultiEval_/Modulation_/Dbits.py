from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dbits:
	"""Dbits commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dbits", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:DBITs \n
		Snippet: value: List[int] = driver.multiEval.modulation.dbits.fetch() \n
		Returns the demodulated bits of the 'Measurement Slot'. For GMSK modulation, a symbol consists of 1 bit, for 8PSK of 3
		bits, for 16-QAM of 4 bits. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: demod_bits: decimal 142 values, one value per symbol, representing the demodulated bits of the symbol in decimal presentation Range: 0 to 15"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:MODulation:DBITs?', suppressed)
		return response
