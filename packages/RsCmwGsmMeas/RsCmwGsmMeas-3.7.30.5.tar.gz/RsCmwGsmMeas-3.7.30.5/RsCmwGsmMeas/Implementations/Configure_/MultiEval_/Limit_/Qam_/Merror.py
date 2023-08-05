from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Merror:
	"""Merror commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("merror", core, parent)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Values: List[float]: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Values', DataType.FloatList, None, False, False, 3),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 7)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Values: List[float] = None
			self.Selection: List[bool] = None

	def set(self, structure: MerrorStruct, qamOrder=repcap.QamOrder.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:MERRor \n
		Snippet: driver.configure.multiEval.limit.qam.merror.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default) \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the magnitude error. \n
			:param structure: for set value, see the help for MerrorStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:MERRor', structure)

	def get(self, qamOrder=repcap.QamOrder.Default) -> MerrorStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.multiEval.limit.qam.merror.get(qamOrder = repcap.QamOrder.Default) \n
		Defines and activates upper limits for the RMS, peak and 95th percentile values of the magnitude error. \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for MerrorStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:MERRor?', self.__class__.MerrorStruct())
