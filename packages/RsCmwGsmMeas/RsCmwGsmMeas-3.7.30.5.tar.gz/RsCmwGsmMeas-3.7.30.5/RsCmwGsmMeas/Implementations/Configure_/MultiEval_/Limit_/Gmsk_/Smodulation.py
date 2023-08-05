from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smodulation:
	"""Smodulation commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smodulation", core, parent)

	@property
	def mpoint(self):
		"""mpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpoint'):
			from .Smodulation_.Mpoint import Mpoint
			self._mpoint = Mpoint(self._core, self._base)
		return self._mpoint

	# noinspection PyTypeChecker
	class RpowerStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Minimum: float: numeric Low reference power value Range: 0 dBm to 43 dBm, Unit: dBm
			- Maximum: float: numeric High reference power value Range: 0 dBm to 43 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Maximum')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Minimum: float = None
			self.Maximum: float = None

	def get_rpower(self) -> RpowerStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SMODulation:RPOWer \n
		Snippet: value: RpowerStruct = driver.configure.multiEval.limit.gmsk.smodulation.get_rpower() \n
		Defines two reference power values for the modulation scheme GMSK. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SMODulation:MPOint<no>. \n
			:return: structure: for return value, see the help for RpowerStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SMODulation:RPOWer?', self.__class__.RpowerStruct())

	def set_rpower(self, value: RpowerStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SMODulation:RPOWer \n
		Snippet: driver.configure.multiEval.limit.gmsk.smodulation.set_rpower(value = RpowerStruct()) \n
		Defines two reference power values for the modulation scheme GMSK. These values are relevant in the context of
		CONFigure:GSM:MEAS<i>:MEValuation:LIMit:GMSK:SMODulation:MPOint<no>. \n
			:param value: see the help for RpowerStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:GMSK:SMODulation:RPOWer', value)

	def clone(self) -> 'Smodulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Smodulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
