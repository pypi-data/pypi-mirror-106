from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frequency", core, parent)

	@property
	def limits(self):
		"""limits commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_limits'):
			from .Frequency_.Limits import Limits
			self._limits = Limits(self._core, self._base)
		return self._limits

	# noinspection PyTypeChecker
	def calculate(self) -> List[enums.ResultStatus2]:
		"""SCPI: CALCulate:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency \n
		Snippet: value: List[enums.ResultStatus2] = driver.multiEval.sswitching.frequency.calculate() \n
		Returns the maximum burst power measured at a series of frequencies. The frequencies are determined by the offset values
		defined via the command method RsCmwGsmMeas.Configure.MultiEval.Sswitching.ofrequence. All defined offset values are
		considered (irrespective of their activation status) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency?', suppressed)
		return Conversions.str_to_list_enum(response, enums.ResultStatus2)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency \n
		Snippet: value: List[float] = driver.multiEval.sswitching.frequency.fetch() \n
		Returns the maximum burst power measured at a series of frequencies. The frequencies are determined by the offset values
		defined via the command method RsCmwGsmMeas.Configure.MultiEval.Sswitching.ofrequence. All defined offset values are
		considered (irrespective of their activation status) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency \n
		Snippet: value: List[float] = driver.multiEval.sswitching.frequency.read() \n
		Returns the maximum burst power measured at a series of frequencies. The frequencies are determined by the offset values
		defined via the command method RsCmwGsmMeas.Configure.MultiEval.Sswitching.ofrequence. All defined offset values are
		considered (irrespective of their activation status) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
		Use RsCmwGsmMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: power: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:GSM:MEASurement<Instance>:MEValuation:SSWitching:FREQuency?', suppressed)
		return response

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
