from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Svector:
	"""Svector commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("svector", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Usefull_Part_Min: float: No parameter help available
			- Usefull_Part_Max: float: No parameter help available
			- Subvector: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Usefull_Part_Min'),
			ArgStruct.scalar_float('Usefull_Part_Max'),
			ArgStruct('Subvector', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Usefull_Part_Min: float = None
			self.Usefull_Part_Max: float = None
			self.Subvector: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:CURRent:SVECtor \n
		Snippet: value: FetchStruct = driver.multiEval.powerVsTime.current.svector.fetch() \n
		Returns special burst power values for the 'Measure Slot'. The number to the left of each result parameter is provided
		for easy identification of the parameter position within the result array. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:PVTime:CURRent:SVECtor?', self.__class__.FetchStruct())
