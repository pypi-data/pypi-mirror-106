from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smodulation:
	"""Smodulation commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smodulation", core, parent)

	def get_ofrequence(self) -> List[float or bool]:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:OFRequence \n
		Snippet: value: List[float or bool] = driver.configure.multiEval.smodulation.get_ofrequence() \n
		Defines the frequency offsets to be used for spectrum modulation measurements. The offsets are defined relative to the
		analyzer frequency. Up to 20 offsets can be defined and enabled. \n
			:return: frequency_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:OFRequence?')
		return Conversions.str_to_float_or_bool_list(response)

	def set_ofrequence(self, frequency_offset: List[float or bool]) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:OFRequence \n
		Snippet: driver.configure.multiEval.smodulation.set_ofrequence(frequency_offset = [1.1, True, 2.2, False, 3.3]) \n
		Defines the frequency offsets to be used for spectrum modulation measurements. The offsets are defined relative to the
		analyzer frequency. Up to 20 offsets can be defined and enabled. \n
			:param frequency_offset: numeric | OFF | ON Set and enable frequency offset. Range: 0 Hz to 3 MHz, Unit: Hz Additional parameters: OFF | ON (disables / enables offset using the previous/default value)
		"""
		param = Conversions.list_to_csv_str(frequency_offset)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:OFRequence {param}')

	# noinspection PyTypeChecker
	class EareaStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable_1: bool: OFF | ON ON: Enable area 1 OFF: Disable area 1
			- Start_1: int: integer Start of evaluation area 1 Range: 0 Sym to 146 Sym, Unit: Symbol
			- Stop_1: int: integer Stop of evaluation area 1 Range: 1 Symbol to 147 Symbol, Unit: Symbol
			- Enable_2: bool: OFF | ON ON: Enable area 2 OFF: Disable area 2
			- Start_2: int: integer Start of evaluation area 2 Range: 0 Sym to 146 Sym, Unit: Symbol
			- Stop_2: int: integer Stop of evaluation area 2 Range: 1 Symbol to 147 Symbol, Unit: Symbol"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_1'),
			ArgStruct.scalar_int('Start_1'),
			ArgStruct.scalar_int('Stop_1'),
			ArgStruct.scalar_bool('Enable_2'),
			ArgStruct.scalar_int('Start_2'),
			ArgStruct.scalar_int('Stop_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_1: bool = None
			self.Start_1: int = None
			self.Stop_1: int = None
			self.Enable_2: bool = None
			self.Start_2: int = None
			self.Stop_2: int = None

	def get_earea(self) -> EareaStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:EARea \n
		Snippet: value: EareaStruct = driver.configure.multiEval.smodulation.get_earea() \n
		Defines the time intervals (evaluation areas) to be used for spectrum modulation measurements. \n
			:return: structure: for return value, see the help for EareaStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:EARea?', self.__class__.EareaStruct())

	def set_earea(self, value: EareaStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:EARea \n
		Snippet: driver.configure.multiEval.smodulation.set_earea(value = EareaStruct()) \n
		Defines the time intervals (evaluation areas) to be used for spectrum modulation measurements. \n
			:param value: see the help for EareaStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:EARea', value)

	def get_tdf_select(self) -> int or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:TDFSelect \n
		Snippet: value: int or bool = driver.configure.multiEval.smodulation.get_tdf_select() \n
		Defines the offset frequency for the spectrum modulation time diagram. The diagram shows the measured power vs. time at
		the selected offset frequency. The numbers 1 to 20 select the negative frequency offsets from the frequency offsets list,
		numbers 21 to 40 select the positive frequency offsets. \n
			:return: nr_freq_offset: integer | ON | OFF Range: 0 to 40 Additional parameters: ON | OFF (enables | disables offset)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:TDFSelect?')
		return Conversions.str_to_int_or_bool(response)

	def set_tdf_select(self, nr_freq_offset: int or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:TDFSelect \n
		Snippet: driver.configure.multiEval.smodulation.set_tdf_select(nr_freq_offset = 1) \n
		Defines the offset frequency for the spectrum modulation time diagram. The diagram shows the measured power vs. time at
		the selected offset frequency. The numbers 1 to 20 select the negative frequency offsets from the frequency offsets list,
		numbers 21 to 40 select the positive frequency offsets. \n
			:param nr_freq_offset: integer | ON | OFF Range: 0 to 40 Additional parameters: ON | OFF (enables | disables offset)
		"""
		param = Conversions.decimal_or_bool_value_to_str(nr_freq_offset)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SMODulation:TDFSelect {param}')
