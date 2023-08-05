from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Static:
	"""Static commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("static", core, parent)

	# noinspection PyTypeChecker
	class StaticStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Time_Start: float: numeric Start time of the area Range: -50 µs to 600 µs, Unit: s
			- Time_End: float: numeric End time of the area Range: -50 µs to 600 µs, Unit: s
			- Rel_Lev_Start: float: numeric Start level of the relative limit for the area Range: -100 dB to 10 dB, Unit: dB
			- Rel_Lev_End: float: numeric End level of the relative limit for the area Range: -100 dB to 10 dB, Unit: dB
			- Abs_Lev_Start: float or bool: numeric | ON | OFF Start level of the absolute limit for the area Range: -100 dBm to 10 dBm, Unit: dBm Additional parameters: OFF | ON (disables start and end level | enables start and end level using the previous/default values)
			- Abs_Lev_End: float or bool: numeric | ON | OFF End level of the absolute limit for the area Range: -100 dBm to 10 dBm, Unit: dBm Additional parameters: OFF | ON (disables start and end level | enables start and end level using the previous/default values)
			- Enable: bool: OFF | ON ON: Enable area no OFF: Disable area no"""
		__meta_args_list = [
			ArgStruct.scalar_float('Time_Start'),
			ArgStruct.scalar_float('Time_End'),
			ArgStruct.scalar_float('Rel_Lev_Start'),
			ArgStruct.scalar_float('Rel_Lev_End'),
			ArgStruct.scalar_float_ext('Abs_Lev_Start'),
			ArgStruct.scalar_float_ext('Abs_Lev_End'),
			ArgStruct.scalar_bool('Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Time_Start: float = None
			self.Time_End: float = None
			self.Rel_Lev_Start: float = None
			self.Rel_Lev_End: float = None
			self.Abs_Lev_Start: float or bool = None
			self.Abs_Lev_End: float or bool = None
			self.Enable: bool = None

	def set(self, structure: StaticStruct, usefulPart=repcap.UsefulPart.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:PVTime:LOWer:UPARt<nr>:STATic \n
		Snippet: driver.configure.multiEval.limit.epsk.powerVsTime.lower.upart.static.set(value = [PROPERTY_STRUCT_NAME](), usefulPart = repcap.UsefulPart.Default) \n
		These commands define and activate lower limit lines for the measured power vs. time. The lines apply to the 'useful
		part' of a burst for modulation schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) . Each line can consist of several areas for
		which relative and absolute limits can be defined (if both are defined the lower limit overrules the higher one) . \n
			:param structure: for set value, see the help for StaticStruct structure arguments.
			:param usefulPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Upart')"""
		usefulPart_cmd_val = self._base.get_repcap_cmd_value(usefulPart, repcap.UsefulPart)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:PVTime:LOWer:UPARt{usefulPart_cmd_val}:STATic', structure)

	def get(self, usefulPart=repcap.UsefulPart.Default) -> StaticStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:PVTime:LOWer:UPARt<nr>:STATic \n
		Snippet: value: StaticStruct = driver.configure.multiEval.limit.epsk.powerVsTime.lower.upart.static.get(usefulPart = repcap.UsefulPart.Default) \n
		These commands define and activate lower limit lines for the measured power vs. time. The lines apply to the 'useful
		part' of a burst for modulation schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) . Each line can consist of several areas for
		which relative and absolute limits can be defined (if both are defined the lower limit overrules the higher one) . \n
			:param usefulPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Upart')
			:return: structure: for return value, see the help for StaticStruct structure arguments."""
		usefulPart_cmd_val = self._base.get_repcap_cmd_value(usefulPart, repcap.UsefulPart)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:EPSK:PVTime:LOWer:UPARt{usefulPart_cmd_val}:STATic?', self.__class__.StaticStruct())
