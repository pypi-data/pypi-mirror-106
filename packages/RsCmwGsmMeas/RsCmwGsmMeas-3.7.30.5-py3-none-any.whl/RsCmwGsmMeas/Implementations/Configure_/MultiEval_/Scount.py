from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scount", core, parent)

	def get_power_vs_time(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: value: int = driver.configure.multiEval.scount.get_power_vs_time() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the power vs. time measurement Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:PVTime?')
		return Conversions.str_to_int(response)

	def set_power_vs_time(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:PVTime \n
		Snippet: driver.configure.multiEval.scount.set_power_vs_time(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the power vs. time measurement Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:PVTime {param}')

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.multiEval.scount.get_modulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the modulation measurement Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:MODulation \n
		Snippet: driver.configure.multiEval.scount.set_modulation(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the modulation measurement Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:MODulation {param}')

	def get_smodulation(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SMODulation \n
		Snippet: value: int = driver.configure.multiEval.scount.get_smodulation() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the spectrum modulation measurement Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SMODulation?')
		return Conversions.str_to_int(response)

	def set_smodulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SMODulation \n
		Snippet: driver.configure.multiEval.scount.set_smodulation(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the spectrum modulation measurement Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SMODulation {param}')

	def get_sswitching(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SSWitching \n
		Snippet: value: int = driver.configure.multiEval.scount.get_sswitching() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals for the spectrum switching measurement Range: 1 to 100
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SSWitching?')
		return Conversions.str_to_int(response)

	def set_sswitching(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SSWitching \n
		Snippet: driver.configure.multiEval.scount.set_sswitching(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals for the spectrum switching measurement Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:SSWitching {param}')

	def get_ber(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:BER \n
		Snippet: value: int = driver.configure.multiEval.scount.get_ber() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:return: statistic_count: numeric Number of measurement intervals (bursts) for the 'BER' measurement Range: 1 to 1000
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:BER?')
		return Conversions.str_to_int(response)

	def set_ber(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:BER \n
		Snippet: driver.configure.multiEval.scount.set_ber(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. \n
			:param statistic_count: numeric Number of measurement intervals (bursts) for the 'BER' measurement Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCOunt:BER {param}')
