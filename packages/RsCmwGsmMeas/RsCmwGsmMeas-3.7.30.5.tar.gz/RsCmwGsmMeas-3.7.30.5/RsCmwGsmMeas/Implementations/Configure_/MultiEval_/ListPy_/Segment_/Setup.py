from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: integer Number of steps or frames in the segment, depending on the configured step length ([CMDLINK: CONFigure:GSM:MEASi:MEValuation:LIST:SLENgth CMDLINK]) . If the step length is set to OFF, the segment length is defined in frames. So the number of slots in the segment equals 8 * SegmentLength. If a step length is defined (1 to 8) , the segment length is defined in steps. So the number of slots in the segment equals StepLength * SegmentLength. Range: 1 to 3000
			- Level: float: numeric Expected nominal power in the segment. The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet. Unit: dBm
			- Frequency: float: numeric Range: 100 MHz to 6 GHz, Unit: Hz
			- Pcl: int: Optional setting parameter. integer Expected power control level for the segment Range: 0 to 31
			- Retrigger_Flag: enums.RetriggerFlag: Optional setting parameter. OFF | ON | IFPower Specifies whether a trigger event is required for the segment or not. The setting is ignored for the first segment of a measurement and for trigger mode ONCE (see [CMDLINK: TRIGger:GSM:MEASi:MEValuation:LIST:MODE CMDLINK]) . OFF: measure the segment without retrigger ON: wait for trigger event before measuring the segment IFPower: wait for 'IF Power' trigger event before measuring the segment
			- Evaluat_Offset: int: Optional setting parameter. integer Number of steps at the beginning of the segment which are not measured Range: 0 to 1000"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_int('Pcl'),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Frequency: float = None
			self.Pcl: int = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None

	def set(self, structure: SetupStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: driver.configure.multiEval.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the length, the analyzer settings, the expected PCL, retrigger setting and evaluation offset of a selected
		segment. In general, this command must be sent for all measured segments (method RsCmwGsmMeas.Configure.MultiEval.ListPy.
		lrange) . The PCL values are used if the global 'PCL Mode: PCL' is set (method RsCmwGsmMeas.Configure.MultiEval.
		pclModePCL) . They can affect the limit check results; see 'PCL Mode'. The current GSM band setting (method RsCmwGsmMeas.
		Configure.band) specifies the exact meaning of the PCL; see Table 'GSM power control levels'. \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup', structure)

	def get(self, segment=repcap.Segment.Default) -> SetupStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SETup \n
		Snippet: value: SetupStruct = driver.configure.multiEval.listPy.segment.setup.get(segment = repcap.Segment.Default) \n
		Defines the length, the analyzer settings, the expected PCL, retrigger setting and evaluation offset of a selected
		segment. In general, this command must be sent for all measured segments (method RsCmwGsmMeas.Configure.MultiEval.ListPy.
		lrange) . The PCL values are used if the global 'PCL Mode: PCL' is set (method RsCmwGsmMeas.Configure.MultiEval.
		pclModePCL) . They can affect the limit check results; see 'PCL Mode'. The current GSM band setting (method RsCmwGsmMeas.
		Configure.band) specifies the exact meaning of the PCL; see Table 'GSM power control levels'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SETup?', self.__class__.SetupStruct())
