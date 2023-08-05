from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	# noinspection PyTypeChecker
	def get_loop(self) -> enums.LoopType:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:LOOP \n
		Snippet: value: enums.LoopType = driver.configure.multiEval.ber.get_loop() \n
		Selects the loop for BER tests. \n
			:return: loop: C | SRB C: Loop C (for GMSK signals, with channel coding) SRB: SRB loop (for 8PSK-modulated signals, MCS7 to MCS9)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:LOOP?')
		return Conversions.str_to_scalar_enum(response, enums.LoopType)

	def set_loop(self, loop: enums.LoopType) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:LOOP \n
		Snippet: driver.configure.multiEval.ber.set_loop(loop = enums.LoopType.C) \n
		Selects the loop for BER tests. \n
			:param loop: C | SRB C: Loop C (for GMSK signals, with channel coding) SRB: SRB loop (for 8PSK-modulated signals, MCS7 to MCS9)
		"""
		param = Conversions.enum_scalar_to_str(loop, enums.LoopType)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:LOOP {param}')

	def get_tstart(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TSTart \n
		Snippet: value: float = driver.configure.multiEval.ber.get_tstart() \n
		Selects the threshold start value for BER tests. This value is the maximum bit error rate in the first burst of the BER
		measurement. \n
			:return: threshold_start: numeric Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TSTart?')
		return Conversions.str_to_float(response)

	def set_tstart(self, threshold_start: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TSTart \n
		Snippet: driver.configure.multiEval.ber.set_tstart(threshold_start = 1.0) \n
		Selects the threshold start value for BER tests. This value is the maximum bit error rate in the first burst of the BER
		measurement. \n
			:param threshold_start: numeric Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(threshold_start)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TSTart {param}')

	def get_trun(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TRUN \n
		Snippet: value: float = driver.configure.multiEval.ber.get_trun() \n
		Selects the threshold run value for BER tests. This value is the maximum bit error rate in any burst considered for the
		BER measurement. \n
			:return: threshold_run: numeric Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TRUN?')
		return Conversions.str_to_float(response)

	def set_trun(self, threshold_run: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TRUN \n
		Snippet: driver.configure.multiEval.ber.set_trun(threshold_run = 1.0) \n
		Selects the threshold run value for BER tests. This value is the maximum bit error rate in any burst considered for the
		BER measurement. \n
			:param threshold_run: numeric Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(threshold_run)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:BER:TRUN {param}')
