from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vamos:
	"""Vamos commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("vamos", core, parent)

	def get_tsc_set(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:VAMos:TSCSet \n
		Snippet: value: int = driver.configure.multiEval.vamos.get_tsc_set() \n
		Specifies the expected VAMOS training sequence code (TSC) set of the measured GSM uplink signal. With a specific TSC set
		selection, the R&S CMW analyzes bursts with this TSC set only. \n
			:return: tsc_set: integer Range: 1 to 2
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:VAMos:TSCSet?')
		return Conversions.str_to_int(response)

	def set_tsc_set(self, tsc_set: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:VAMos:TSCSet \n
		Snippet: driver.configure.multiEval.vamos.set_tsc_set(tsc_set = 1) \n
		Specifies the expected VAMOS training sequence code (TSC) set of the measured GSM uplink signal. With a specific TSC set
		selection, the R&S CMW analyzes bursts with this TSC set only. \n
			:param tsc_set: integer Range: 1 to 2
		"""
		param = Conversions.decimal_value_to_str(tsc_set)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:VAMos:TSCSet {param}')
