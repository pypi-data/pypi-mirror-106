from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 4 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	@property
	def ber(self):
		"""ber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ber'):
			from .Ber_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Ber_.Absolute import Absolute
			self._absolute = Absolute(self._core, self._base)
		return self._absolute

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Ber_.Count import Count
			self._count = Count(self._core, self._base)
		return self._count

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator' In list mode, a zero reliability indicator indicates that the results in all measured segments are valid. A non-zero value indicates that an error occurred in at least one of the measured segments.
			- Seg_Reliability: List[int]: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Statistic_Expire: List[int]: No parameter help available
			- Slot_Info: List[enums.SlotInfo]: No parameter help available
			- Slot_Statistic: List[bool]: ON | OFF ON: Averaging over different burst type OFF: Uniform burst type in the averaging range
			- Ber: List[float]: float % bit error rate Range: 0 % to 100 %, Unit: %
			- Ber_Absolute: List[int or bool]: decimal Total number of detected bit errors The BER measurement evaluates: 114 data bits per GMSK-modulated normal burst 306 data bits per 8PSK-modulated burst. Range: 0 to no. of measured bits
			- Ber_Count: List[int or bool]: decimal Total number of measured bursts Range: 0 to StatisticCount For StatisticCount, see [CMDLINK: CONFigure:GSM:MEASi:MEValuation:SCOunt:BER CMDLINK]"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Seg_Reliability', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Statistic_Expire', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Slot_Info', DataType.EnumList, enums.SlotInfo, False, True, 1),
			ArgStruct('Slot_Statistic', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Ber', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ber_Absolute', DataType.IntegerExtList, None, False, True, 1),
			ArgStruct('Ber_Count', DataType.IntegerExtList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: List[int] = None
			self.Statistic_Expire: List[int] = None
			self.Slot_Info: List[enums.SlotInfo] = None
			self.Slot_Statistic: List[bool] = None
			self.Ber: List[float] = None
			self.Ber_Absolute: List[int or bool] = None
			self.Ber_Count: List[int or bool] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.ber.fetch() \n
		Returns the BER results in list mode. The values listed below in curly brackets {} are returned for each measured
		segment: {...}seg 1, {...}seg 2, ..., {...}seg n. The position of measured segments within the range of configured
		segments and their number n is determined by method RsCmwGsmMeas.Configure.MultiEval.ListPy.lrange. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:GSM:MEASurement<Instance>:MEValuation:LIST:BER?', self.__class__.FetchStruct())

	def clone(self) -> 'Ber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
