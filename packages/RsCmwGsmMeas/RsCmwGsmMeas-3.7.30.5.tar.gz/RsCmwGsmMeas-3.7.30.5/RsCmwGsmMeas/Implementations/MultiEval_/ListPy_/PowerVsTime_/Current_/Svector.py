from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Svector:
	"""Svector commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("svector", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: List[int]: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: List[int]: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Usefull_Part_Min: List[float]: No parameter help available
			- Usefull_Part_Max: List[float]: No parameter help available
			- Subvector_1: List[float]: No parameter help available
			- Subvector_2: List[float]: No parameter help available
			- Subvector_3: List[float]: No parameter help available
			- Subvector_4: List[float]: No parameter help available
			- Subvector_5: List[float]: No parameter help available
			- Subvector_6: List[float]: No parameter help available
			- Subvector_7: List[float]: No parameter help available
			- Subvector_8: List[float]: No parameter help available
			- Subvector_9: List[float]: No parameter help available
			- Subvector_10: List[float]: No parameter help available
			- Subvector_11: List[float]: No parameter help available
			- Subvector_12: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statist_Expired', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Out_Of_Tolerance', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Usefull_Part_Min', DataType.FloatList, None, False, True, 1),
			ArgStruct('Usefull_Part_Max', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_1', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_2', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_3', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_4', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_5', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_6', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_7', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_8', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_9', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_10', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_11', DataType.FloatList, None, False, True, 1),
			ArgStruct('Subvector_12', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statist_Expired: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Out_Of_Tolerance: List[int] = None
			self.Usefull_Part_Min: List[float] = None
			self.Usefull_Part_Max: List[float] = None
			self.Subvector_1: List[float] = None
			self.Subvector_2: List[float] = None
			self.Subvector_3: List[float] = None
			self.Subvector_4: List[float] = None
			self.Subvector_5: List[float] = None
			self.Subvector_6: List[float] = None
			self.Subvector_7: List[float] = None
			self.Subvector_8: List[float] = None
			self.Subvector_9: List[float] = None
			self.Subvector_10: List[float] = None
			self.Subvector_11: List[float] = None
			self.Subvector_12: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:CURRent:SVECtor \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.powerVsTime.current.svector.fetch() \n
		Returns special burst power values in list mode. The values listed below in curly brackets {} are returned for each
		measured segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of
		configured segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:PVTime:CURRent:SVECtor?', self.__class__.FetchStruct())
