from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 13 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def singleCmw(self):
		"""singleCmw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_singleCmw'):
			from .ListPy_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	def get_slength(self) -> int or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SLENgth \n
		Snippet: value: int or bool = driver.configure.multiEval.listPy.get_slength() \n
		Selects the step length, i.e. the time difference between two measured TDMA timeslots. A step length of 1 means that
		every slot is measured, a step length of 8 means that a single timeslot per TDMA frame is measured.
			INTRO_CMD_HELP: If the step length is set to OFF, an arbitrary number of slots in each TDMA frame can be measured. The measured slots are defined by the <FramePattern> parameter of the following commands: \n
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Modulation.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.PowerVsTime.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Smodulation.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Sswitching.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Ber.set \n
			:return: step_length: numeric | ON | OFF Step length as number of TDMA slots Range: 1 to 8 Additional parameters: ON | OFF (enable step length | use FramePattern)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SLENgth?')
		return Conversions.str_to_int_or_bool(response)

	def set_slength(self, step_length: int or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SLENgth \n
		Snippet: driver.configure.multiEval.listPy.set_slength(step_length = 1) \n
		Selects the step length, i.e. the time difference between two measured TDMA timeslots. A step length of 1 means that
		every slot is measured, a step length of 8 means that a single timeslot per TDMA frame is measured.
			INTRO_CMD_HELP: If the step length is set to OFF, an arbitrary number of slots in each TDMA frame can be measured. The measured slots are defined by the <FramePattern> parameter of the following commands: \n
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Modulation.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.PowerVsTime.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Smodulation.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Sswitching.set
			- method RsCmwGsmMeas.Configure.MultiEval.ListPy.Segment.Ber.set \n
			:param step_length: numeric | ON | OFF Step length as number of TDMA slots Range: 1 to 8 Additional parameters: ON | OFF (enable step length | use FramePattern)
		"""
		param = Conversions.decimal_or_bool_value_to_str(step_length)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:SLENgth {param}')

	# noinspection PyTypeChecker
	class LrangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: numeric First measured segment in the range of configured segments Range: 1 to 2000
			- Nr_Segments: int: numeric Relative number within the range of measured segments Range: 1 to 512"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Nr_Segments')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Nr_Segments: int = None

	def get_lrange(self) -> LrangeStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: value: LrangeStruct = driver.configure.multiEval.listPy.get_lrange() \n
		Select a range of measured segments. The segments must be configured using method RsCmwGsmMeas.Configure.MultiEval.ListPy.
		Segment.Setup.set. \n
			:return: structure: for return value, see the help for LrangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:LRANge?', self.__class__.LrangeStruct())

	def set_lrange(self, value: LrangeStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:LRANge \n
		Snippet: driver.configure.multiEval.listPy.set_lrange(value = LrangeStruct()) \n
		Select a range of measured segments. The segments must be configured using method RsCmwGsmMeas.Configure.MultiEval.ListPy.
		Segment.Setup.set. \n
			:param value: see the help for LrangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:LRANge', value)

	def get_os_index(self) -> int or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: value: int or bool = driver.configure.multiEval.listPy.get_os_index() \n
		Selects the number of the segment to be displayed in the measurement diagram. The selected index must be within the range
		of measured segments (method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange) . Setting a value also enables the offline
		mode. \n
			:return: offline_seg_index: numeric | ON | OFF Range: 1 to 200 Additional parameters: ON | OFF (enables | disables offline mode)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:OSINdex?')
		return Conversions.str_to_int_or_bool(response)

	def set_os_index(self, offline_seg_index: int or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:OSINdex \n
		Snippet: driver.configure.multiEval.listPy.set_os_index(offline_seg_index = 1) \n
		Selects the number of the segment to be displayed in the measurement diagram. The selected index must be within the range
		of measured segments (method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange) . Setting a value also enables the offline
		mode. \n
			:param offline_seg_index: numeric | ON | OFF Range: 1 to 200 Additional parameters: ON | OFF (enables | disables offline mode)
		"""
		param = Conversions.decimal_or_bool_value_to_str(offline_seg_index)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:OSINdex {param}')

	def get_ii_frames(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:IIFRames \n
		Snippet: value: bool = driver.configure.multiEval.listPy.get_ii_frames() \n
		Selects whether idle frames are ignored or cause a 'signal low' error. For details, see 'Idle frame evaluation'. \n
			:return: ignore: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:IIFRames?')
		return Conversions.str_to_bool(response)

	def set_ii_frames(self, ignore: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:IIFRames \n
		Snippet: driver.configure.multiEval.listPy.set_ii_frames(ignore = False) \n
		Selects whether idle frames are ignored or cause a 'signal low' error. For details, see 'Idle frame evaluation'. \n
			:param ignore: OFF | ON
		"""
		param = Conversions.bool_to_str(ignore)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST:IIFRames {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: value: bool = driver.configure.multiEval.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF | ON ON: Enable list mode OFF: Disable list mode
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST \n
		Snippet: driver.configure.multiEval.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF | ON ON: Enable list mode OFF: Disable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
