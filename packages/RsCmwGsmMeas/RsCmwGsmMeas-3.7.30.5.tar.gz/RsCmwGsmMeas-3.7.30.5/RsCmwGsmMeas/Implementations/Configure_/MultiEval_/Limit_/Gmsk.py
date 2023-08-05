from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gmsk:
	"""Gmsk commands group definition. 19 total commands, 3 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gmsk", core, parent)

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .Gmsk_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	@property
	def smodulation(self):
		"""smodulation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_smodulation'):
			from .Gmsk_.Smodulation import Smodulation
			self._smodulation = Smodulation(self._core, self._base)
		return self._smodulation

	@property
	def sswitching(self):
		"""sswitching commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sswitching'):
			from .Gmsk_.Sswitching import Sswitching
			self._sswitching = Sswitching(self._core, self._base)
		return self._sswitching

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Values: List[float]: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Values', DataType.FloatList, None, False, False, 3),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 7)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Values: List[float] = None
			self.Selection: List[bool] = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.multiEval.limit.gmsk.get_ev_magnitude() \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the error vector magnitude (EVM) . \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:EVMagnitude \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the error vector magnitude (EVM) . \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Values: List[float]: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Values', DataType.FloatList, None, False, False, 3),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 7)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Values: List[float] = None
			self.Selection: List[bool] = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.multiEval.limit.gmsk.get_merror() \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the magnitude error. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:MERRor \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_merror(value = MerrorStruct()) \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the magnitude error. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Values: List[float]: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Values', DataType.FloatList, None, False, False, 3),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 7)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Values: List[float] = None
			self.Selection: List[bool] = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.multiEval.limit.gmsk.get_perror() \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the phase error. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:PERRor \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_perror(value = PerrorStruct()) \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the phase error. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:PERRor', value)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value: float: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Value'),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: float = None
			self.Selection: List[bool] = None

	def get_iq_offset(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.multiEval.limit.gmsk.get_iq_offset() \n
		Defines and activates upper limits for the I/Q origin offset values. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQOFfset?', self.__class__.IqOffsetStruct())

	def set_iq_offset(self, value: IqOffsetStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQOFfset \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_iq_offset(value = IqOffsetStruct()) \n
		Defines and activates upper limits for the I/Q origin offset values. \n
			:param value: see the help for IqOffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQOFfset', value)

	# noinspection PyTypeChecker
	class IqImbalanceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value: float: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Value'),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: float = None
			self.Selection: List[bool] = None

	def get_iq_imbalance(self) -> IqImbalanceStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQIMbalance \n
		Snippet: value: IqImbalanceStruct = driver.configure.multiEval.limit.gmsk.get_iq_imbalance() \n
		Defines and activates upper limits for the I/Q imbalance values. \n
			:return: structure: for return value, see the help for IqImbalanceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQIMbalance?', self.__class__.IqImbalanceStruct())

	def set_iq_imbalance(self, value: IqImbalanceStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQIMbalance \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_iq_imbalance(value = IqImbalanceStruct()) \n
		Defines and activates upper limits for the I/Q imbalance values. \n
			:param value: see the help for IqImbalanceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:IQIMbalance', value)

	# noinspection PyTypeChecker
	class TerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value: float: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Value'),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: float = None
			self.Selection: List[bool] = None

	def get_terror(self) -> TerrorStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:TERRor \n
		Snippet: value: TerrorStruct = driver.configure.multiEval.limit.gmsk.get_terror() \n
		Defines and activates upper limits for the timing error. \n
			:return: structure: for return value, see the help for TerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:TERRor?', self.__class__.TerrorStruct())

	def set_terror(self, value: TerrorStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:TERRor \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_terror(value = TerrorStruct()) \n
		Defines and activates upper limits for the timing error. \n
			:param value: see the help for TerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:TERRor', value)

	# noinspection PyTypeChecker
	class FreqErrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Value: float: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Value'),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: float = None
			self.Selection: List[bool] = None

	def get_freq_error(self) -> FreqErrorStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:FERRor \n
		Snippet: value: FreqErrorStruct = driver.configure.multiEval.limit.gmsk.get_freq_error() \n
		Defines and activates upper limits for the frequency error. \n
			:return: structure: for return value, see the help for FreqErrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:FERRor?', self.__class__.FreqErrorStruct())

	def set_freq_error(self, value: FreqErrorStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:FERRor \n
		Snippet: driver.configure.multiEval.limit.gmsk.set_freq_error(value = FreqErrorStruct()) \n
		Defines and activates upper limits for the frequency error. \n
			:param value: see the help for FreqErrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:FERRor', value)

	def clone(self) -> 'Gmsk':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gmsk(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
