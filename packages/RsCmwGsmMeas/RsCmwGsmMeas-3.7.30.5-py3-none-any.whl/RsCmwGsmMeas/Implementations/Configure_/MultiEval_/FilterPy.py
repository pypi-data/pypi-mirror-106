from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	# noinspection PyTypeChecker
	def get_power_vs_time(self) -> enums.FilterPvTime:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:PVTime \n
		Snippet: value: enums.FilterPvTime = driver.configure.multiEval.filterPy.get_power_vs_time() \n
		Selects the bandwidth of the IF filter. \n
			:return: filter_py: G05M | G10M G05M: 500 kHz Gauss filter G10M: 1 MHz Gauss filter
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:PVTime?')
		return Conversions.str_to_scalar_enum(response, enums.FilterPvTime)

	def set_power_vs_time(self, filter_py: enums.FilterPvTime) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:PVTime \n
		Snippet: driver.configure.multiEval.filterPy.set_power_vs_time(filter_py = enums.FilterPvTime.G05M) \n
		Selects the bandwidth of the IF filter. \n
			:param filter_py: G05M | G10M G05M: 500 kHz Gauss filter G10M: 1 MHz Gauss filter
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterPvTime)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:PVTime {param}')

	# noinspection PyTypeChecker
	def get_iq(self) -> enums.FilterIq:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:IQ \n
		Snippet: value: enums.FilterIq = driver.configure.multiEval.filterPy.get_iq() \n
		Specifies whether the I/Q data is filtered to eliminate the inter-symbol interference (ISI) at all constellation points. \n
			:return: filter_py: ISIRemoved | UNFiltered | F90Khz ISIRemoved: ISI removed UNFiltered: Unfiltered data F90Khz: 90 kHz filter
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:IQ?')
		return Conversions.str_to_scalar_enum(response, enums.FilterIq)

	def set_iq(self, filter_py: enums.FilterIq) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:IQ \n
		Snippet: driver.configure.multiEval.filterPy.set_iq(filter_py = enums.FilterIq.F90Khz) \n
		Specifies whether the I/Q data is filtered to eliminate the inter-symbol interference (ISI) at all constellation points. \n
			:param filter_py: ISIRemoved | UNFiltered | F90Khz ISIRemoved: ISI removed UNFiltered: Unfiltered data F90Khz: 90 kHz filter
		"""
		param = Conversions.enum_scalar_to_str(filter_py, enums.FilterIq)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:FILTer:IQ {param}')
