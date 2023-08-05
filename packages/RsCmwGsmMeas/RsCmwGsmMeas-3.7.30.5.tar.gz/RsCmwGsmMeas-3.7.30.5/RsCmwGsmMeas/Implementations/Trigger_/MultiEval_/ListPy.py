from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ListMode:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:LIST:MODE \n
		Snippet: value: enums.ListMode = driver.trigger.multiEval.listPy.get_mode() \n
		Specifies whether a trigger event initiates a measurement of the entire measurement interval (comprising the number of
		segments defined via method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange) or a measurement of single segment. \n
			:return: mode: ONCE | SEGMent ONCE: A trigger event is only required to start the measurement. The entire range of segments to be measured is captured without additional trigger event. The retrigger flags of the segments are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		response = self._core.io.query_str('TRIGger:GSM:MEASurement<Instance>:MEValuation:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ListMode)

	def set_mode(self, mode: enums.ListMode) -> None:
		"""SCPI: TRIGger:GSM:MEASurement<Instance>:MEValuation:LIST:MODE \n
		Snippet: driver.trigger.multiEval.listPy.set_mode(mode = enums.ListMode.ONCE) \n
		Specifies whether a trigger event initiates a measurement of the entire measurement interval (comprising the number of
		segments defined via method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange) or a measurement of single segment. \n
			:param mode: ONCE | SEGMent ONCE: A trigger event is only required to start the measurement. The entire range of segments to be measured is captured without additional trigger event. The retrigger flags of the segments are ignored. SEGMent: The retrigger flag of each segment is evaluated. It defines whether the measurement waits for a trigger event before capturing the segment, or not.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ListMode)
		self._core.io.write(f'TRIGger:GSM:MEASurement<Instance>:MEValuation:LIST:MODE {param}')
