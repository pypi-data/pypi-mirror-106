from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sswitching:
	"""Sswitching commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sswitching", core, parent)

	# noinspection PyTypeChecker
	class SswitchingStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Statistic: int: integer The statistical length is defined in slots. It is limited by the number of evaluated slots (defined via step length or frame pattern) . Range: 1 to 100
			- Enable: bool: OFF | ON ON: Enable measurement of spectrum due to switching (including the 'spectrum switching time' results in offline mode) OFF: Disable measurement
			- Frame_Pattern: str: Optional setting parameter. binary 8-digit binary value, defines the evaluated timeslots in each TDMA frame. Used only if no step length is configured (see [CMDLINK: CONFigure:GSM:MEASi:MEValuation:LIST:SLENgth CMDLINK]) . Range: #B00000000 to #B11111111 (no slots ... all slots measured)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Statistic'),
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_raw_str('Frame_Pattern')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Statistic: int = None
			self.Enable: bool = None
			self.Frame_Pattern: str = None

	def set(self, structure: SswitchingStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SSWitching \n
		Snippet: driver.configure.multiEval.listPy.segment.sswitching.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for the maximum calculation (peak hold mode) and enables the spectrum due to switching
		measurement in segment no. <no>; see 'List Mode'. \n
			:param structure: for set value, see the help for SswitchingStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SSWitching', structure)

	def get(self, segment=repcap.Segment.Default) -> SswitchingStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:SSWitching \n
		Snippet: value: SswitchingStruct = driver.configure.multiEval.listPy.segment.sswitching.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the maximum calculation (peak hold mode) and enables the spectrum due to switching
		measurement in segment no. <no>; see 'List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SswitchingStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:SSWitching?', self.__class__.SswitchingStruct())
