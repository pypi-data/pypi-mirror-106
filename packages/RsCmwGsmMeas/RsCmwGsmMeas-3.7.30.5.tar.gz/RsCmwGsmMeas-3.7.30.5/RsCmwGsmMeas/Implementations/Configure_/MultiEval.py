from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 122 total commands, 11 Sub-groups, 18 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def vamos(self):
		"""vamos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vamos'):
			from .MultiEval_.Vamos import Vamos
			self._vamos = Vamos(self._core, self._base)
		return self._vamos

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_filterPy'):
			from .MultiEval_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def rotation(self):
		"""rotation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rotation'):
			from .MultiEval_.Rotation import Rotation
			self._rotation = Rotation(self._core, self._base)
		return self._rotation

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .MultiEval_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_scount'):
			from .MultiEval_.Scount import Scount
			self._scount = Scount(self._core, self._base)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 13 commands."""
		if not hasattr(self, '_result'):
			from .MultiEval_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .MultiEval_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	@property
	def smodulation(self):
		"""smodulation commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_smodulation'):
			from .MultiEval_.Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._base)
		return self._smodulation

	@property
	def sswitching(self):
		"""sswitching commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_sswitching'):
			from .MultiEval_.Sswitching import Sswitching
			self._sswitching = Sswitching(self._core, self._base)
		return self._sswitching

	@property
	def ber(self):
		"""ber commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ber'):
			from .MultiEval_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.multiEval.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | SLFail NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:SCONdition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.multiEval.get_mo_exception() \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: ON | OFF ON: Results are never rejected OFF: Faulty results are rejected
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results that the R&S CMW identifies as faulty or inaccurate are rejected. \n
			:param meas_on_exception: ON | OFF ON: Results are never rejected OFF: Faulty results are rejected
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:MOEXception {param}')

	# noinspection PyTypeChecker
	def get_rp_mode(self) -> enums.RefPowerMode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RPMode \n
		Snippet: value: enums.RefPowerMode = driver.configure.multiEval.get_rp_mode() \n
		Defines how the reference power, i.e. the 0-dB line in the measurement diagram, is calculated. \n
			:return: ref_power_mode: CURRent | DCOMpensated | AVERage Current, data compensated, average
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RPMode?')
		return Conversions.str_to_scalar_enum(response, enums.RefPowerMode)

	def set_rp_mode(self, ref_power_mode: enums.RefPowerMode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RPMode \n
		Snippet: driver.configure.multiEval.set_rp_mode(ref_power_mode = enums.RefPowerMode.AVERage) \n
		Defines how the reference power, i.e. the 0-dB line in the measurement diagram, is calculated. \n
			:param ref_power_mode: CURRent | DCOMpensated | AVERage Current, data compensated, average
		"""
		param = Conversions.enum_scalar_to_str(ref_power_mode, enums.RefPowerMode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RPMode {param}')

	# noinspection PyTypeChecker
	def get_fc_range(self) -> enums.RangeMode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FCRange \n
		Snippet: value: enums.RangeMode = driver.configure.multiEval.get_fc_range() \n
		Selects the width of the frequency range that the R&S CMW analyzes to establish time-synchronization with the received
		signal. \n
			:return: mode: NORMal | WIDE NORMal: Normal frequency range WIDE: Wide frequency range
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:FCRange?')
		return Conversions.str_to_scalar_enum(response, enums.RangeMode)

	def set_fc_range(self, mode: enums.RangeMode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:FCRange \n
		Snippet: driver.configure.multiEval.set_fc_range(mode = enums.RangeMode.NORMal) \n
		Selects the width of the frequency range that the R&S CMW analyzes to establish time-synchronization with the received
		signal. \n
			:param mode: NORMal | WIDE NORMal: Normal frequency range WIDE: Wide frequency range
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RangeMode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:FCRange {param}')

	def get_hda_level(self) -> float or bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:HDALevel \n
		Snippet: value: float or bool = driver.configure.multiEval.get_hda_level() \n
		Defines a signal level relative to the 'Expected Nominal Power' (method RsCmwGsmMeas.Configure.RfSettings.envelopePower)
		where the two results obtained in a two stage measurement are joined. \n
			:return: high_dyn_ass_level: numeric | ON | OFF Range: -60 dB to -10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables two-shot measurement)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:HDALevel?')
		return Conversions.str_to_float_or_bool(response)

	def set_hda_level(self, high_dyn_ass_level: float or bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:HDALevel \n
		Snippet: driver.configure.multiEval.set_hda_level(high_dyn_ass_level = 1.0) \n
		Defines a signal level relative to the 'Expected Nominal Power' (method RsCmwGsmMeas.Configure.RfSettings.envelopePower)
		where the two results obtained in a two stage measurement are joined. \n
			:param high_dyn_ass_level: numeric | ON | OFF Range: -60 dB to -10 dB, Unit: dB Additional parameters: OFF | ON (disables | enables two-shot measurement)
		"""
		param = Conversions.decimal_or_bool_value_to_str(high_dyn_ass_level)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:HDALevel {param}')

	# noinspection PyTypeChecker
	class MslotsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Slot_Offset: int: decimal Start of the measurement interval relative to the GSM frame boundary Range: 0 to 7
			- Slot_Count: int: decimal Number of slots to be measured Range: 1 to 8
			- Meas_Slot: int: decimal Slot to be measured for one-slot measurements Range: 0 to 7"""
		__meta_args_list = [
			ArgStruct.scalar_int('Slot_Offset'),
			ArgStruct.scalar_int('Slot_Count'),
			ArgStruct.scalar_int('Meas_Slot')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Slot_Offset: int = None
			self.Slot_Count: int = None
			self.Meas_Slot: int = None

	def get_mslots(self) -> MslotsStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MSLots \n
		Snippet: value: MslotsStruct = driver.configure.multiEval.get_mslots() \n
		Defines settings for the measured slots. For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:MSLot:UL. \n
			:return: structure: for return value, see the help for MslotsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:MSLots?', self.__class__.MslotsStruct())

	def set_mslots(self, value: MslotsStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MSLots \n
		Snippet: driver.configure.multiEval.set_mslots(value = MslotsStruct()) \n
		Defines settings for the measured slots. For the combined signal path scenario, useCONFigure:GSM:SIGN<i>:MSLot:UL. \n
			:param value: see the help for MslotsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:MSLots', value)

	# noinspection PyTypeChecker
	def get_tsequence(self) -> enums.TscA:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:TSEQuence \n
		Snippet: value: enums.TscA = driver.configure.multiEval.get_tsequence() \n
		Selects the training sequence of the analyzed bursts. For the combined signal path scenario,
		use CONFigure:GSM:SIGN<i>:CELL:BCC. \n
			:return: tsc: OFF | TSC0 | TSC1 | TSC2 | TSC3 | TSC4 | TSC5 | TSC6 | TSC7 | TSCA | DUMM OFF: Analyze all bursts, irrespective of their training sequence TSC0 ... TSC7:Analyze bursts with a particular GSM training sequence TSCA: Analyze bursts with any of the GSM training sequences TSC0 to TSC7 DUMMY: Analyze GSM-specific dummy bursts
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:TSEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.TscA)

	def set_tsequence(self, tsc: enums.TscA) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:TSEQuence \n
		Snippet: driver.configure.multiEval.set_tsequence(tsc = enums.TscA.DUMM) \n
		Selects the training sequence of the analyzed bursts. For the combined signal path scenario,
		use CONFigure:GSM:SIGN<i>:CELL:BCC. \n
			:param tsc: OFF | TSC0 | TSC1 | TSC2 | TSC3 | TSC4 | TSC5 | TSC6 | TSC7 | TSCA | DUMM OFF: Analyze all bursts, irrespective of their training sequence TSC0 ... TSC7:Analyze bursts with a particular GSM training sequence TSCA: Analyze bursts with any of the GSM training sequences TSC0 to TSC7 DUMMY: Analyze GSM-specific dummy bursts
		"""
		param = Conversions.enum_scalar_to_str(tsc, enums.TscA)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:TSEQuence {param}')

	def get_nbq_search(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:NBQSearch \n
		Snippet: value: bool = driver.configure.multiEval.get_nbq_search() \n
		Enables or disables the search for 16-QAM-modulated normal bursts. \n
			:return: enable: OFF | ON ON: Enable 16-QAM NB search OFF: Disable 16-QAM NB search
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:NBQSearch?')
		return Conversions.str_to_bool(response)

	def set_nbq_search(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:NBQSearch \n
		Snippet: driver.configure.multiEval.set_nbq_search(enable = False) \n
		Enables or disables the search for 16-QAM-modulated normal bursts. \n
			:param enable: OFF | ON ON: Enable 16-QAM NB search OFF: Disable 16-QAM NB search
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:NBQSearch {param}')

	def get_ab_search(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:ABSearch \n
		Snippet: value: bool = driver.configure.multiEval.get_ab_search() \n
		Enables or disables the access burst measurement. \n
			:return: enable: OFF | ON ON: Enable access burst search OFF: Disable access burst search
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:ABSearch?')
		return Conversions.str_to_bool(response)

	def set_ab_search(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:ABSearch \n
		Snippet: driver.configure.multiEval.set_ab_search(enable = False) \n
		Enables or disables the access burst measurement. \n
			:param enable: OFF | ON ON: Enable access burst search OFF: Disable access burst search
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:ABSearch {param}')

	# noinspection PyTypeChecker
	def get_mview(self) -> List[enums.SlotA]:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MVIew \n
		Snippet: value: List[enums.SlotA] = driver.configure.multiEval.get_mview() \n
		Defines the expected modulation scheme and burst type in all timeslots and adjusts the power/time template accordingly. \n
			:return: slot: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:MVIew?')
		return Conversions.str_to_list_enum(response, enums.SlotA)

	def set_mview(self, slot: List[enums.SlotA]) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:MVIew \n
		Snippet: driver.configure.multiEval.set_mview(slot = [SlotA.ACCess, SlotA.Q16]) \n
		Defines the expected modulation scheme and burst type in all timeslots and adjusts the power/time template accordingly. \n
			:param slot: ANY | OFF | GMSK | EPSK | ACCess | Q16 ANY: Any burst type can be analyzed OFF: No signal expected GMSK: GMSK-modulated normal bursts EPSK: 8PSK-modulated normal bursts ACCess: Access bursts Q16: 16-QAM-modulated normal bursts
		"""
		param = Conversions.enum_list_to_str(slot, enums.SlotA)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:MVIew {param}')

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AcquisitionMode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:AMODe \n
		Snippet: value: enums.AcquisitionMode = driver.configure.multiEval.get_amode() \n
		Selects the method that the R&S CMW uses for frame synchronization. \n
			:return: acquisition_mode: GAP | PATTern GAP: Gap PATTern: Pattern
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AcquisitionMode)

	def set_amode(self, acquisition_mode: enums.AcquisitionMode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:AMODe \n
		Snippet: driver.configure.multiEval.set_amode(acquisition_mode = enums.AcquisitionMode.GAP) \n
		Selects the method that the R&S CMW uses for frame synchronization. \n
			:param acquisition_mode: GAP | PATTern GAP: Gap PATTern: Pattern
		"""
		param = Conversions.enum_scalar_to_str(acquisition_mode, enums.AcquisitionMode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:AMODe {param}')

	# noinspection PyTypeChecker
	class ApatternStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Slot_0: enums.SlotB: No parameter help available
			- Slot_1: enums.SlotB: No parameter help available
			- Slot_2: enums.SlotB: No parameter help available
			- Slot_3: enums.SlotB: No parameter help available
			- Slot_4: enums.SlotB: No parameter help available
			- Slot_5: enums.SlotB: No parameter help available
			- Slot_6: enums.SlotB: No parameter help available
			- Slot_7: enums.SlotB: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Slot_0', enums.SlotB),
			ArgStruct.scalar_enum('Slot_1', enums.SlotB),
			ArgStruct.scalar_enum('Slot_2', enums.SlotB),
			ArgStruct.scalar_enum('Slot_3', enums.SlotB),
			ArgStruct.scalar_enum('Slot_4', enums.SlotB),
			ArgStruct.scalar_enum('Slot_5', enums.SlotB),
			ArgStruct.scalar_enum('Slot_6', enums.SlotB),
			ArgStruct.scalar_enum('Slot_7', enums.SlotB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Slot_0: enums.SlotB = None
			self.Slot_1: enums.SlotB = None
			self.Slot_2: enums.SlotB = None
			self.Slot_3: enums.SlotB = None
			self.Slot_4: enums.SlotB = None
			self.Slot_5: enums.SlotB = None
			self.Slot_6: enums.SlotB = None
			self.Slot_7: enums.SlotB = None

	# noinspection PyTypeChecker
	def get_apattern(self) -> ApatternStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:APATtern \n
		Snippet: value: ApatternStruct = driver.configure.multiEval.get_apattern() \n
		Defines the burst pattern that the R&S CMW expects in the TDMA frames of the received GSM signal. The pattern is used for
		frame synchronization if the pattern acquisition mode is active (see method RsCmwGsmMeas.Configure.MultiEval.amode) . \n
			:return: structure: for return value, see the help for ApatternStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:APATtern?', self.__class__.ApatternStruct())

	def set_apattern(self, value: ApatternStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:APATtern \n
		Snippet: driver.configure.multiEval.set_apattern(value = ApatternStruct()) \n
		Defines the burst pattern that the R&S CMW expects in the TDMA frames of the received GSM signal. The pattern is used for
		frame synchronization if the pattern acquisition mode is active (see method RsCmwGsmMeas.Configure.MultiEval.amode) . \n
			:param value: see the help for ApatternStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:APATtern', value)

	def get_glength(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:GLENgth \n
		Snippet: value: int = driver.configure.multiEval.get_glength() \n
		Defines the gap length as an integer number of slots. The gap length is used for frame synchronization if the gap
		acquisition mode is active (see method RsCmwGsmMeas.Configure.MultiEval.amode) . \n
			:return: gap_length: integer Range: 1 slot to 3 slots, Unit: slots
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:GLENgth?')
		return Conversions.str_to_int(response)

	def set_glength(self, gap_length: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:GLENgth \n
		Snippet: driver.configure.multiEval.set_glength(gap_length = 1) \n
		Defines the gap length as an integer number of slots. The gap length is used for frame synchronization if the gap
		acquisition mode is active (see method RsCmwGsmMeas.Configure.MultiEval.amode) . \n
			:param gap_length: integer Range: 1 slot to 3 slots, Unit: slots
		"""
		param = Conversions.decimal_value_to_str(gap_length)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:GLENgth {param}')

	# noinspection PyTypeChecker
	def get_pcl_mode(self) -> enums.PclMode:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:PCLMode \n
		Snippet: value: enums.PclMode = driver.configure.multiEval.get_pcl_mode() \n
		Defines how the R&S CMW determines the PCL of the measured signal. \n
			:return: pcl_mode: AUTO | PCL | SIGNaling AUTO: Estimated PCL PCL: PCL defined via method RsCmwGsmMeas.Configure.MultiEval.pcl SIGNaling: PCL determined by coupled signaling application (combined signal path only)
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:PCLMode?')
		return Conversions.str_to_scalar_enum(response, enums.PclMode)

	def set_pcl_mode(self, pcl_mode: enums.PclMode) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:PCLMode \n
		Snippet: driver.configure.multiEval.set_pcl_mode(pcl_mode = enums.PclMode.AUTO) \n
		Defines how the R&S CMW determines the PCL of the measured signal. \n
			:param pcl_mode: AUTO | PCL | SIGNaling AUTO: Estimated PCL PCL: PCL defined via method RsCmwGsmMeas.Configure.MultiEval.pcl SIGNaling: PCL determined by coupled signaling application (combined signal path only)
		"""
		param = Conversions.enum_scalar_to_str(pcl_mode, enums.PclMode)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:PCLMode {param}')

	# noinspection PyTypeChecker
	class PclStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Slot_0: int: integer Range: 0 to 31
			- Slot_1: int: integer Range: 0 to 31
			- Slot_2: int: integer Range: 0 to 31
			- Slot_3: int: integer Range: 0 to 31
			- Slot_4: int: integer Range: 0 to 31
			- Slot_5: int: integer Range: 0 to 31
			- Slot_6: int: integer Range: 0 to 31
			- Slot_7: int: integer Range: 0 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_int('Slot_0'),
			ArgStruct.scalar_int('Slot_1'),
			ArgStruct.scalar_int('Slot_2'),
			ArgStruct.scalar_int('Slot_3'),
			ArgStruct.scalar_int('Slot_4'),
			ArgStruct.scalar_int('Slot_5'),
			ArgStruct.scalar_int('Slot_6'),
			ArgStruct.scalar_int('Slot_7')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Slot_0: int = None
			self.Slot_1: int = None
			self.Slot_2: int = None
			self.Slot_3: int = None
			self.Slot_4: int = None
			self.Slot_5: int = None
			self.Slot_6: int = None
			self.Slot_7: int = None

	def get_pcl(self) -> PclStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:PCL \n
		Snippet: value: PclStruct = driver.configure.multiEval.get_pcl() \n
		Sets the expected PCL values in all timeslots, to be used in method RsCmwGsmMeas.Configure.MultiEval.pclModePCL. The PCL
		values are interpreted according to the current GSM band setting (method RsCmwGsmMeas.Configure.band) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:PCL:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched \n
			:return: structure: for return value, see the help for PclStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:PCL?', self.__class__.PclStruct())

	def set_pcl(self, value: PclStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:PCL \n
		Snippet: driver.configure.multiEval.set_pcl(value = PclStruct()) \n
		Sets the expected PCL values in all timeslots, to be used in method RsCmwGsmMeas.Configure.MultiEval.pclModePCL. The PCL
		values are interpreted according to the current GSM band setting (method RsCmwGsmMeas.Configure.band) .
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:PCL:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched \n
			:param value: see the help for PclStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:PCL', value)

	def get_iio_frames(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:IIOFrames \n
		Snippet: value: bool = driver.configure.multiEval.get_iio_frames() \n
		Enables feature ignore initial off frames to avoid trigger timeout in access burst measurement in idle mode. \n
			:return: ignore: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:IIOFrames?')
		return Conversions.str_to_bool(response)

	def set_iio_frames(self, ignore: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:IIOFrames \n
		Snippet: driver.configure.multiEval.set_iio_frames(ignore = False) \n
		Enables feature ignore initial off frames to avoid trigger timeout in access burst measurement in idle mode. \n
			:param ignore: OFF | ON
		"""
		param = Conversions.bool_to_str(ignore)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:IIOFrames {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
