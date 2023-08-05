from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sswitching:
	"""Sswitching commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sswitching", core, parent)

	@property
	def mpoint(self):
		"""mpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpoint'):
			from .Sswitching_.Mpoint import Mpoint
			self._mpoint = Mpoint(self._core, self._base)
		return self._mpoint

	# noinspection PyTypeChecker
	class PlevelStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: List[bool]: No parameter help available
			- Power_Level: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, False, 10),
			ArgStruct('Power_Level', DataType.FloatList, None, False, False, 10)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Power_Level: List[float] = None

	def get_plevel(self) -> PlevelStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SSWitching:PLEVel \n
		Snippet: value: PlevelStruct = driver.configure.multiEval.limit.gmsk.sswitching.get_plevel() \n
		Defines and activates reference power values for the modulation scheme GMSK. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SSWitching:MPOint<no>. \n
			:return: structure: for return value, see the help for PlevelStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SSWitching:PLEVel?', self.__class__.PlevelStruct())

	def set_plevel(self, value: PlevelStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SSWitching:PLEVel \n
		Snippet: driver.configure.multiEval.limit.gmsk.sswitching.set_plevel(value = PlevelStruct()) \n
		Defines and activates reference power values for the modulation scheme GMSK. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SSWitching:MPOint<no>. \n
			:param value: see the help for PlevelStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SSWitching:PLEVel', value)

	def clone(self) -> 'Sswitching':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sswitching(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
