from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Mod_Statistics: int: integer The statistical length is defined in slots. It is limited by the number of evaluated slots (defined via step length or frame pattern) . Range: 1 to 1000
			- Evm_Enable: bool: OFF | ON ON: Enable measurement of EVM OFF: Disable measurement of EVM
			- Mag_Error_Enable: bool: OFF | ON Enable or disable measurement of magnitude error
			- Phase_Err_Enable: bool: OFF | ON Enable or disable measurement of phase error
			- Am_Pm_Enable: bool: OFF | ON Enable or disable measurement of AM PM delay
			- Frame_Pattern: str: Optional setting parameter. binary 8-digit binary value, defines the evaluated timeslots in each TDMA frame. Used only if no step length is configured (see [CMDLINK: CONFigure:GSM:MEASi:MEValuation:LIST:SLENgth CMDLINK]) . Range: #B00000000 to #B11111111 (no slots ... all slots measured)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Evm_Enable'),
			ArgStruct.scalar_bool('Mag_Error_Enable'),
			ArgStruct.scalar_bool('Phase_Err_Enable'),
			ArgStruct.scalar_bool('Am_Pm_Enable'),
			ArgStruct.scalar_raw_str('Frame_Pattern')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Evm_Enable: bool = None
			self.Mag_Error_Enable: bool = None
			self.Phase_Err_Enable: bool = None
			self.Am_Pm_Enable: bool = None
			self.Frame_Pattern: str = None

	def set(self, structure: ModulationStruct, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: driver.configure.multiEval.listPy.segment.modulation.set(value = [PROPERTY_STRUCT_NAME](), segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MIN, and MAX calculation and enables the calculation of the different
		modulation results in segment no. <no>; see 'List Mode'. \n
			:param structure: for set value, see the help for ModulationStruct structure arguments.
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation', structure)

	def get(self, segment=repcap.Segment.Default) -> ModulationStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation \n
		Snippet: value: ModulationStruct = driver.configure.multiEval.listPy.segment.modulation.get(segment = repcap.Segment.Default) \n
		Defines the statistical length for the AVERage, MIN, and MAX calculation and enables the calculation of the different
		modulation results in segment no. <no>; see 'List Mode'. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation?', self.__class__.ModulationStruct())
