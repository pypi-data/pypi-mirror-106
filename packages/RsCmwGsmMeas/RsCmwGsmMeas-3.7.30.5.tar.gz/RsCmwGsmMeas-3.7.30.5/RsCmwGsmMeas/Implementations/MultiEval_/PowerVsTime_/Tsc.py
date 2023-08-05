from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsc:
	"""Tsc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tsc", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.TscB]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:TSC \n
		Snippet: value: List[enums.TscB] = driver.multiEval.powerVsTime.tsc.fetch() \n
		Returns the detected training sequence code (TSC) and burst type for all measured timeslots. 8 values are returned,
		irrespective of the 'No. of Slots' measured (method RsCmwGsmMeas.Configure.MultiEval.mslots) . If 'No. of Slots' < 8,
		some of the returned values are NAN. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: tsc: OFF | NB0 | NB1 | NB2 | NB3 | NB4 | NB5 | NB6 | NB7 | DUMMy | AB0 | AB1 | AB2 | AB3 | AB4 | AB5 | AB6 | AB7 Detected TSC (8 values) : OFF: Inactive slot NB0 ... NB7: Normal burst, training sequence TSC0 to TSC7 DUMMY: Dummy burst AB0 ... AB7: Access burst, TSC 0 to TSC7"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:TSC?', suppressed)
		return Conversions.str_to_list_enum(response, enums.TscB)
