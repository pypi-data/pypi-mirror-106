from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sswitching:
	"""Sswitching commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sswitching", core, parent)

	def get_ofrequence(self) -> List[float or bool]:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:OFRequence \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.sswitching.get_ofrequence() \n
		Defines the frequency offsets to be used for spectrum switching measurements. The offsets are defined relative to the
		analyzer frequency. Up to 20 offsets can be defined and enabled. \n
			:return: frequency_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:OFRequence?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_ofrequence(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:OFRequence \n
		Snippet: driver.configure.multiEval.sswitching.set_ofrequence(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the frequency offsets to be used for spectrum switching measurements. The offsets are defined relative to the
		analyzer frequency. Up to 20 offsets can be defined and enabled. \n
			:param frequency_offset: numeric | OFF | ON Set and enable frequency offset. Range: 0 Hz to 3 MHz, Unit: Hz Additional parameters: OFF | ON (disables / enables offset using the previous/default value)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:OFRequence {param}')

	def get_tdf_select(self) -> int or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:TDFSelect \n
		Snippet: value: int or bool = driver.configure.multiEval.sswitching.get_tdf_select() \n
		Defines the offset frequency for the spectrum modulation time diagram. The diagram shows the measured power vs. time at
		the selected offset frequency. The numbers 1 to 20 select the negative frequency offsets from the frequency offsets list,
		numbers 21 to 40 select the positive frequency offsets. \n
			:return: nr_freq_offset: integer | ON | OFF Range: 0 to 40 Additional parameters: OFF | ON (disables | enables the offset)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:TDFSelect?')
		return Conversions.str_to_int_or_bool(response)

	def set_tdf_select(self, nr_freq_offset: int or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:TDFSelect \n
		Snippet: driver.configure.multiEval.sswitching.set_tdf_select(nr_freq_offset = 1) \n
		Defines the offset frequency for the spectrum modulation time diagram. The diagram shows the measured power vs. time at
		the selected offset frequency. The numbers 1 to 20 select the negative frequency offsets from the frequency offsets list,
		numbers 21 to 40 select the positive frequency offsets. \n
			:param nr_freq_offset: integer | ON | OFF Range: 0 to 40 Additional parameters: OFF | ON (disables | enables the offset)
		"""
		param = Conversions.decimal_or_bool_value_to_str(nr_freq_offset)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:TDFSelect {param}')

	# noinspection PyTypeChecker
	def get_ph_mode(self) -> enums.PeakHoldMode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:PHMode \n
		Snippet: value: enums.PeakHoldMode = driver.configure.multiEval.sswitching.get_ph_mode() \n
		Specifies how the peak hold mode is used for the spectrum switching results in frequency domain (bar graphs) and in time
		domain. \n
			:return: peak_hold_mode: PHOL | SCO PHOL: Frequency and time: peak hold SCO: Frequency: stat. count, time: current
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:PHMode?')
		return Conversions.str_to_scalar_enum(response, enums.PeakHoldMode)

	def set_ph_mode(self, peak_hold_mode: enums.PeakHoldMode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:PHMode \n
		Snippet: driver.configure.multiEval.sswitching.set_ph_mode(peak_hold_mode = enums.PeakHoldMode.PHOL) \n
		Specifies how the peak hold mode is used for the spectrum switching results in frequency domain (bar graphs) and in time
		domain. \n
			:param peak_hold_mode: PHOL | SCO PHOL: Frequency and time: peak hold SCO: Frequency: stat. count, time: current
		"""
		param = Conversions.enum_scalar_to_str(peak_hold_mode, enums.PeakHoldMode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SSWitching:PHMode {param}')
