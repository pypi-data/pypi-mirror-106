from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsTiming:
	"""RsTiming commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rsTiming", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:RSTiming \n
		Snippet: value: List[float] = driver.multiEval.powerVsTime.rsTiming.fetch() \n
		Returns the slot timing for all measured timeslots, relative to the timing of the 'Measurement Slot'. The relative slot
		timing of the 'Measurement Slot' is always zero. The relative slot timing of the other timeslots is the deviation of the
		measured relative timing from the nominal timing. The nominal timing is based on a timeslot length of 156.
		25 symbol durations. The command returns 8 values, irrespective of the 'No. of Slots' measured (method RsCmwGsmMeas.
		Configure.MultiEval.mslots) . If 'No. of Slots' < 8, some of the returned values are NAN. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: rel_slot_timing: float Range: -1500 Sym to 1500 Sym, Unit: bits"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:RSTiming?', suppressed)
		return response
