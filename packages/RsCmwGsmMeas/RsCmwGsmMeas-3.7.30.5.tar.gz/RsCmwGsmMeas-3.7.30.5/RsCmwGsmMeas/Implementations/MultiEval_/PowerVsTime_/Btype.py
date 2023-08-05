from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btype:
	"""Btype commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("btype", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.SlotInfo]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:BTYPe \n
		Snippet: value: List[enums.SlotInfo] = driver.multiEval.powerVsTime.btype.fetch() \n
		Returns the detected burst type for all measured timeslots. 8 values are returned, irrespective of the 'No. of Slots'
		measured (method RsCmwGsmMeas.Configure.MultiEval.mslots) . If 'No. of Slots' < 8, some of the returned values are NAN. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: burst_type: OFF | GMSK | EPSK | ACCess | Q16 Detected burst type (8 values) : GMSK: Normal burst, GMSK-modulated EPSK: Normal burst, 8PSK-modulated ACCess: Access burst Q16: Normal burst, 16-QAM-modulated OFF: Inactive slot"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:BTYPe?', suppressed)
		return Conversions.str_to_list_enum(response, enums.SlotInfo)
