from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get_decode(self) -> enums.Decode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MODulation:DECode \n
		Snippet: value: enums.Decode = driver.configure.multiEval.modulation.get_decode() \n
		Defines whether the guard or tail bits are decoded. \n
			:return: decode: STANdard | GTBits STANdard: Guard and tail bits are assumed to be in line with GSM and therefore not decoded. GTBits: Guard and tail bits are also decoded.
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:MODulation:DECode?')
		return Conversions.str_to_scalar_enum(response, enums.Decode)

	def set_decode(self, decode: enums.Decode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MODulation:DECode \n
		Snippet: driver.configure.multiEval.modulation.set_decode(decode = enums.Decode.GTBits) \n
		Defines whether the guard or tail bits are decoded. \n
			:param decode: STANdard | GTBits STANdard: Guard and tail bits are assumed to be in line with GSM and therefore not decoded. GTBits: Guard and tail bits are also decoded.
		"""
		param = Conversions.enum_scalar_to_str(decode, enums.Decode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:MODulation:DECode {param}')
