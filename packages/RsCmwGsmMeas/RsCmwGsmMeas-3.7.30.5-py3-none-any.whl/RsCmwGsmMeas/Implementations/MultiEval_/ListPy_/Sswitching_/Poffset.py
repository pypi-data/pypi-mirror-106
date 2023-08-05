from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands
	Repeated Capability: FreqOffset, default value after init: FreqOffset.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("poffset", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_freqOffset_get', 'repcap_freqOffset_set', repcap.FreqOffset.Nr1)

	def repcap_freqOffset_set(self, enum_value: repcap.FreqOffset) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FreqOffset.Default
		Default value after init: FreqOffset.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_freqOffset_get(self) -> repcap.FreqOffset:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def fetch(self, freqOffset=repcap.FreqOffset.Default) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SSWitching:POFFset<nr> \n
		Snippet: value: List[float] = driver.multiEval.listPy.sswitching.poffset.fetch(freqOffset = repcap.FreqOffset.Default) \n
		Return the burst power at the carrier frequency minus/plus a selected frequency offset, for all measured list mode
		segments of the spectrum due to switching measurement. The values described below are returned by FETCh commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:param freqOffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Poffset')
			:return: power: float Comma-separated list of values, one per measured segment Range: -100 dBm to 55 dBm, Unit: dBm"""
		freqOffset_cmd_val = self._base.get_repcap_cmd_value(freqOffset, repcap.FreqOffset)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SSWitching:POFFset{freqOffset_cmd_val}?', suppressed)
		return response

	# noinspection PyTypeChecker
	def calculate(self, freqOffset=repcap.FreqOffset.Default) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SSWitching:POFFset<nr> \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.listPy.sswitching.poffset.calculate(freqOffset = repcap.FreqOffset.Default) \n
		Return the burst power at the carrier frequency minus/plus a selected frequency offset, for all measured list mode
		segments of the spectrum due to switching measurement. The values described below are returned by FETCh commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:param freqOffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Poffset')
			:return: power: float Comma-separated list of values, one per measured segment Range: -100 dBm to 55 dBm, Unit: dBm"""
		freqOffset_cmd_val = self._base.get_repcap_cmd_value(freqOffset, repcap.FreqOffset)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:LIST:SSWitching:POFFset{freqOffset_cmd_val}?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)

	def clone(self) -> 'Poffset':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Poffset(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
