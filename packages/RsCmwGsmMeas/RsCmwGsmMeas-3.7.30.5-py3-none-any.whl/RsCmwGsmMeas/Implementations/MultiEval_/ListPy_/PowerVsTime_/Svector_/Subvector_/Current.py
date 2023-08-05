from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, subVector=repcap.SubVector.Default) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:SVECtor:SUBVector<nr>:CURRent \n
		Snippet: value: List[float] = driver.multiEval.listPy.powerVsTime.svector.subvector.current.fetch(subVector = repcap.SubVector.Default) \n
		Return burst power at a specific burst position for all measured list mode segments. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:param subVector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subvector')
			:return: subvector: float Comma-separated list of values, one per measured segment Range: -100 dB to 100 dB, Unit: dB"""
		subVector_cmd_val = self._base.get_repcap_cmd_value(subVector, repcap.SubVector)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:SVECtor:SUBVector{subVector_cmd_val}:CURRent?', suppressed)
		return response
