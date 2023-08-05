from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqImbalance:
	"""IqImbalance commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqImbalance", core, parent)

	# noinspection PyTypeChecker
	class IqImbalanceStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Value: float: No parameter help available
			- Selection: List[bool]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Value'),
			ArgStruct('Selection', DataType.BooleanList, None, False, False, 3)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Value: float = None
			self.Selection: List[bool] = None

	def set(self, structure: IqImbalanceStruct, qamOrder=repcap.QamOrder.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IQIMbalance \n
		Snippet: driver.configure.multiEval.limit.qam.iqImbalance.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default) \n
		Defines and activates upper limits for the I/Q imbalance values. \n
			:param structure: for set value, see the help for IqImbalanceStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:IQIMbalance', structure)

	def get(self, qamOrder=repcap.QamOrder.Default) -> IqImbalanceStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:IQIMbalance \n
		Snippet: value: IqImbalanceStruct = driver.configure.multiEval.limit.qam.iqImbalance.get(qamOrder = repcap.QamOrder.Default) \n
		Defines and activates upper limits for the I/Q imbalance values. \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IqImbalanceStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:IQIMbalance?', self.__class__.IqImbalanceStruct())
