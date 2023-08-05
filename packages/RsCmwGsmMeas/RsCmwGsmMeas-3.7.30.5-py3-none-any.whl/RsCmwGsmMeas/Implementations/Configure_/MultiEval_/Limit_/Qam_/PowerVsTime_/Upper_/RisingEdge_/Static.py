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
			- Time_Start: float: numeric Start and end time of the area Range: -50 µs to 600 µs, Unit: s
			- Time_End: float: numeric Start and end time of the area Range: -50 µs to 600 µs, Unit: s
			- Rel_Lev_Start: float: numeric Start and end level of the relative limit for the area Range: -100 dB to 10 dB, Unit: dB
			- Rel_Lev_End: float: numeric Start and end level of the relative limit for the area Range: -100 dB to 10 dB, Unit: dB
			- Abs_Lev_Start: float or bool: numeric | OFF | ON Start and end level of the absolute limit for the area Range: -100 dBm to 10 dBm, Unit: dBm Additional parameters: OFF | ON (disables start/end level | enables start/end level using the previous/default values)
			- Abs_Lev_End: float or bool: numeric | OFF | ON Start and end level of the absolute limit for the area Range: -100 dBm to 10 dBm, Unit: dBm Additional parameters: OFF | ON (disables start/end level | enables start/end level using the previous/default values)
			- Enable: bool: ON | OFF ON: Enable area no OFF: Disable area no"""
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

	def set(self, structure: StaticStruct, qamOrder=repcap.QamOrder.Default, risingEdge=repcap.RisingEdge.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PVTime:UPPer:REDGe<nr>:STATic \n
		Snippet: driver.configure.multiEval.limit.qam.powerVsTime.upper.risingEdge.static.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default, risingEdge = repcap.RisingEdge.Default) \n
		These commands define and activate upper limit lines for the measured power vs. time. The lines apply to the modulation
		schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) . Each line consists of three sections: rising edge (REDGe) , useful part
		(UPARt) and falling edge (FEDGe) . Each section consists of several areas for which relative and absolute limits can be
		defined (if both are defined the higher limit overrules the lower one) . \n
			:param structure: for set value, see the help for StaticStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:param risingEdge: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RisingEdge')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		risingEdge_cmd_val = self._base.get_repcap_cmd_value(risingEdge, repcap.RisingEdge)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:PVTime:UPPer:REDGe{risingEdge_cmd_val}:STATic', structure)

	def get(self, qamOrder=repcap.QamOrder.Default, risingEdge=repcap.RisingEdge.Default) -> StaticStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:PVTime:UPPer:REDGe<nr>:STATic \n
		Snippet: value: StaticStruct = driver.configure.multiEval.limit.qam.powerVsTime.upper.risingEdge.static.get(qamOrder = repcap.QamOrder.Default, risingEdge = repcap.RisingEdge.Default) \n
		These commands define and activate upper limit lines for the measured power vs. time. The lines apply to the modulation
		schemes GMSK, 8PSK (EPSK) or 16-QAM (QAM16) . Each line consists of three sections: rising edge (REDGe) , useful part
		(UPARt) and falling edge (FEDGe) . Each section consists of several areas for which relative and absolute limits can be
		defined (if both are defined the higher limit overrules the lower one) . \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:param risingEdge: optional repeated capability selector. Default value: Nr1 (settable in the interface 'RisingEdge')
			:return: structure: for return value, see the help for StaticStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		risingEdge_cmd_val = self._base.get_repcap_cmd_value(risingEdge, repcap.RisingEdge)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:PVTime:UPPer:REDGe{risingEdge_cmd_val}:STATic?', self.__class__.StaticStruct())
