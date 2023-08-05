from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rpower:
	"""Rpower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rpower", core, parent)

	# noinspection PyTypeChecker
	class RpowerStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Minimum: float: numeric Low reference power value Range: 0 dBm to 43 dBm, Unit: dBm
			- Maximum: float: numeric High reference power value Range: 0 dBm to 43 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Maximum')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Minimum: float = None
			self.Maximum: float = None

	def set(self, structure: RpowerStruct, qamOrder=repcap.QamOrder.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:SMODulation:RPOWer \n
		Snippet: driver.configure.multiEval.limit.qam.smodulation.rpower.set(value = [PROPERTY_STRUCT_NAME](), qamOrder = repcap.QamOrder.Default) \n
		Define two reference power values for the modulation schemes 8PSK and 16-QAM. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:EPSK:SMODulation:MPOint<no> and
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:QAM<m>:SMODulation:MPOint<no>. \n
			:param structure: for set value, see the help for RpowerStruct structure arguments.
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')"""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:SMODulation:RPOWer', structure)

	def get(self, qamOrder=repcap.QamOrder.Default) -> RpowerStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM<ModOrder>:SMODulation:RPOWer \n
		Snippet: value: RpowerStruct = driver.configure.multiEval.limit.qam.smodulation.rpower.get(qamOrder = repcap.QamOrder.Default) \n
		Define two reference power values for the modulation schemes 8PSK and 16-QAM. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:EPSK:SMODulation:MPOint<no> and
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:QAM<m>:SMODulation:MPOint<no>. \n
			:param qamOrder: optional repeated capability selector. Default value: Nr16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for RpowerStruct structure arguments."""
		qamOrder_cmd_val = self._base.get_repcap_cmd_value(qamOrder, repcap.QamOrder)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:QAM{qamOrder_cmd_val}:SMODulation:RPOWer?', self.__class__.RpowerStruct())
