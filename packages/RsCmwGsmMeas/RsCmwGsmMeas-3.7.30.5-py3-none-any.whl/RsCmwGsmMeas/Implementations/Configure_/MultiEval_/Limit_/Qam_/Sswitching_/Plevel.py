from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plevel:
	"""Plevel commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("plevel", core, parent)

	# noinspection PyTypeChecker
	class PlevelStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: List[bool]: No parameter help available
			- Power_Level: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, False, 10),
			ArgStruct('Power_Level', DataType.FloatList, None, False, False, 10)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Power_Level: List[float] = None

	def set(self, structure: PlevelStruct, qamOrder=repcap.QamOrder.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:SSWitching:PLEVel \n
		Snippet: driver.configure.multiEval.limit.qam.sswitching.plevel.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default) \n
		Define and activate reference power values for the modulation schemes 8PSK and 16-QAM. These values are relevant in the
		context of CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SSWitching:MPOint<no> and
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:QAM<m>:SSWitching:MPOint<no>. \n
			:param structure: for set value, see the help for PlevelStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:SSWitching:PLEVel', structure)

	def get(self, qamOrder=repcap.QamOrder.Default) -> PlevelStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:SSWitching:PLEVel \n
		Snippet: value: PlevelStruct = driver.configure.multiEval.limit.qam.sswitching.plevel.get(qamOrder = repcap.QamOrder.Default) \n
		Define and activate reference power values for the modulation schemes 8PSK and 16-QAM. These values are relevant in the
		context of CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SSWitching:MPOint<no> and
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:QAM<m>:SSWitching:MPOint<no>. \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for PlevelStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:SSWitching:PLEVel?', self.__class__.PlevelStruct())
