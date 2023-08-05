from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


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
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statist_Expired: int: decimal Number of measured steps Range: 0 to Statistical Length (integer value)
			- Slot_Info: enums.SlotInfo: No parameter help available
			- Slot_Statistic: bool: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Out_Of_Tolerance: int: decimal Percentage of measured bursts with failed limit check Range: 0 % to 100 %, Unit: %
			- Usefull_Part_Min: float: No parameter help available
			- Usefull_Part_Max: float: No parameter help available
			- Subvector: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
			ArgStruct.scalar_enum('Slot_Info', enums.SlotInfo),
			ArgStruct.scalar_bool('Slot_Statistic'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Usefull_Part_Min'),
			ArgStruct.scalar_float('Usefull_Part_Max'),
			ArgStruct('Subvector', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
			self.Slot_Info: enums.SlotInfo = None
			self.Slot_Statistic: bool = None
			self.Out_Of_Tolerance: int = None
			self.Usefull_Part_Min: float = None
			self.Usefull_Part_Max: float = None
			self.Subvector: List[float] = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:PVTime:AVERage:SVECtor \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.powerVsTime.average.svector.fetch(segment = repcap.Segment.Default) \n
		Returns special burst power results for segment <no> in list mode. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:PVTime:AVERage:SVECtor?', self.__class__.FetchStruct())
