from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .MultiEval_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def get_source(self) -> str:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:SOURce \n
		Snippet: value: str = driver.trigger.multiEval.get_source() \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:return: source: string 'Power': Power trigger (received RF power) 'Acquisition': Frame trigger according to defined burst pattern 'Free Run': Free run (untriggered)
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:SOURce \n
		Snippet: driver.trigger.multiEval.set_source(source = '1') \n
		Selects the source of the trigger events. Some values are always available. They are listed below. Depending on the
		installed options, additional values are available. You can query a list of all supported values via TRIGger:...
		:CATalog:SOURce?. \n
			:param source: string 'Power': Power trigger (received RF power) 'Acquisition': Frame trigger according to defined burst pattern 'Free Run': Free run (untriggered)
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:SOURce {param}')

	def get_threshold(self) -> float or bool:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: value: float or bool = driver.trigger.multiEval.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: threshold: numeric | ON | OFF Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation) Additional parameters: OFF | ON (disables | enables the threshold)
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:THReshold?')
		return Conversions.str_to_float_or_bool(response)

	def set_threshold(self, threshold: float or bool) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: driver.trigger.multiEval.set_threshold(threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param threshold: numeric | ON | OFF Range: -50 dB to 0 dB, Unit: dB (full scale, i.e. relative to reference level minus external attenuation) Additional parameters: OFF | ON (disables | enables the threshold)
		"""
		param = Conversions.decimal_or_bool_value_to_str(threshold)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.multiEval.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:SLOPe \n
		Snippet: driver.trigger.multiEval.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe | FEDGe REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float or bool = driver.trigger.multiEval.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:return: trigger_timeout: numeric | ON | OFF Range: 0.01 s to 167.77215E+3 s, Unit: s Additional parameters: OFF | ON (disables timeout | enables timeout using the previous/default values)
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.trigger.multiEval.set_timeout(trigger_timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on 'Free Run' measurements. \n
			:param trigger_timeout: numeric | ON | OFF Range: 0.01 s to 167.77215E+3 s, Unit: s Additional parameters: OFF | ON (disables timeout | enables timeout using the previous/default values)
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_mgap(self) -> int:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:MGAP \n
		Snippet: value: int = driver.trigger.multiEval.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: min_trigger_gap: integer Range: 1 slot to 7 slots, Unit: slot
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:MGAP?')
		return Conversions.str_to_int(response)

	def set_mgap(self, min_trigger_gap: int) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:MGAP \n
		Snippet: driver.trigger.multiEval.set_mgap(min_trigger_gap = 1) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param min_trigger_gap: integer Range: 1 slot to 7 slots, Unit: slot
		"""
		param = Conversions.decimal_value_to_str(min_trigger_gap)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:MGAP {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
