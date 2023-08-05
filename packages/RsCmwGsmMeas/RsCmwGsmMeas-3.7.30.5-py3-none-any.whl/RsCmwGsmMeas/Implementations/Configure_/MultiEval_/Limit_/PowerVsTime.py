from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerVsTime:
	"""PowerVsTime commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("powerVsTime", core, parent)

	@property
	def abPower(self):
		"""abPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abPower'):
			from .PowerVsTime_.AbPower import AbPower
			self._abPower = AbPower(self._core, self._base)
		return self._abPower

	def get_gp_level(self) -> float or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:GPLevel \n
		Snippet: value: float or bool = driver.configure.multiEval.limit.powerVsTime.get_gp_level() \n
		Defines the raising of the upper limit line in the guard period between two consecutive bursts. \n
			:return: guard_period_lev: numeric | ON | OFF Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:GPLevel?')
		return Conversions.str_to_float_or_bool(response)

	def set_gp_level(self, guard_period_lev: float or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:GPLevel \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.set_gp_level(guard_period_lev = 1.0) \n
		Defines the raising of the upper limit line in the guard period between two consecutive bursts. \n
			:param guard_period_lev: numeric | ON | OFF Range: 0 dB to 10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the limit)
		"""
		param = Conversions.decimal_or_bool_value_to_str(guard_period_lev)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:GPLevel {param}')

	def clone(self) -> 'PowerVsTime':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerVsTime(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
