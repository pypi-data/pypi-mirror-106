from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ber: float or bool: float % bit error rate Range: 0 % to 100 %, Unit: %
			- Ber_Absolute: List[float or bool]: float Total number of detected bit errors The BER measurement evaluates 114 data bits per GMSK-modulated normal burst, 306 data bits per 8PSK-modulated burst. Range: 0 to no. of measured bits
			- Ber_Count: List[float or bool]: float Total number of evaluated bits Range: 0 to no. of measured bits"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Ber'),
			ArgStruct('Ber_Absolute', DataType.FloatList, None, False, False, 8),
			ArgStruct('Ber_Count', DataType.FloatList, None, False, False, 8)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ber: float or bool = None
			self.Ber_Absolute: List[float or bool] = None
			self.Ber_Count: List[float or bool] = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:GSM:MEASurement<Instance>:MEValuation:BER \n
		Snippet: value: ReadStruct = driver.multiEval.ber.read() \n
		Returns the measured bit error rate. The BER measurement must be enabled using method RsCmwGsmMeas.Configure.MultiEval.
		Result.ber. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:GSM:MEASurement<Instance>:MEValuation:BER?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Ber: float or bool: float % bit error rate Range: 0 % to 100 %, Unit: %
			- Ber_Absolute: int or bool: float Total number of detected bit errors The BER measurement evaluates 114 data bits per GMSK-modulated normal burst, 306 data bits per 8PSK-modulated burst. Range: 0 to no. of measured bits
			- Ber_Count: int or bool: float Total number of evaluated bits Range: 0 to no. of measured bits"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Ber'),
			ArgStruct.scalar_int_ext('Ber_Absolute'),
			ArgStruct.scalar_int_ext('Ber_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ber: float or bool = None
			self.Ber_Absolute: int or bool = None
			self.Ber_Count: int or bool = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:BER \n
		Snippet: value: FetchStruct = driver.multiEval.ber.fetch() \n
		Returns the measured bit error rate. The BER measurement must be enabled using method RsCmwGsmMeas.Configure.MultiEval.
		Result.ber. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:BER?', self.__class__.FetchStruct())
