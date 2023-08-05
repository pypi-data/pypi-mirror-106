from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rotation:
	"""Rotation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rotation", core, parent)

	# noinspection PyTypeChecker
	def get_iq(self) -> enums.Rotation:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:ROTation:IQ \n
		Snippet: value: enums.Rotation = driver.configure.multiEval.rotation.get_iq() \n
		Specifies whether the rotation of the 8PSK and 16-QAM symbols is subtracted off before the symbols are displayed in the
		constellation diagram. \n
			:return: rotation: P38 | P38R P38: Rotation not removed, phase-rotated symbols displayed P38R: Rotation removed
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:ROTation:IQ?')
		return Conversions.str_to_scalar_enum(response, enums.Rotation)

	def set_iq(self, rotation: enums.Rotation) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:ROTation:IQ \n
		Snippet: driver.configure.multiEval.rotation.set_iq(rotation = enums.Rotation.P38) \n
		Specifies whether the rotation of the 8PSK and 16-QAM symbols is subtracted off before the symbols are displayed in the
		constellation diagram. \n
			:param rotation: P38 | P38R P38: Rotation not removed, phase-rotated symbols displayed P38R: Rotation removed
		"""
		param = Conversions.enum_scalar_to_str(rotation, enums.Rotation)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:ROTation:IQ {param}')
