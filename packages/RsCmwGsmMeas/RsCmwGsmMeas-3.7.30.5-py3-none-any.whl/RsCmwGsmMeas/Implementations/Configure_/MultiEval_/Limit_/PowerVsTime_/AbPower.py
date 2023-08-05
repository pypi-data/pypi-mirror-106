from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AbPower:
	"""AbPower commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: AbPower, default value after init: AbPower.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("abPower", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_abPower_get', 'repcap_abPower_set', repcap.AbPower.Nr1)

	def repcap_abPower_set(self, enum_value: repcap.AbPower) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AbPower.Default
		Default value after init: AbPower.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_abPower_get(self) -> repcap.AbPower:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class AbPowerStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Start_Pcl: int: integer Number of first TPCL to which the limits are applied Range: 0 to 31
			- End_Pcl: int: integer Number of last TPCL to which the limits are applied Range: 0 to 31
			- Lower_Limit: float: numeric Range: -10 dB to 0 dB, Unit: dB
			- Upper_Limit: float: numeric Range: 0 dB to 10 dB, Unit: dB
			- Enable: bool: OFF | ON ON: Enable limits for the given no OFF: Disable limits for the given no"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Pcl'),
			ArgStruct.scalar_int('End_Pcl'),
			ArgStruct.scalar_float('Lower_Limit'),
			ArgStruct.scalar_float('Upper_Limit'),
			ArgStruct.scalar_bool('Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Pcl: int = None
			self.End_Pcl: int = None
			self.Lower_Limit: float = None
			self.Upper_Limit: float = None
			self.Enable: bool = None

	def set(self, structure: AbPowerStruct, abPower=repcap.AbPower.Default) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:ABPower<nr> \n
		Snippet: driver.configure.multiEval.limit.powerVsTime.abPower.set(value = [PROPERTY_STRUCT_NAME](), abPower = repcap.AbPower.Default) \n
		Defines and activates limits for the average burst power, i.e. tolerances for ranges of template power control levels
		(TPCLs) . \n
			:param structure: for set value, see the help for AbPowerStruct structure arguments.
			:param abPower: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AbPower')"""
		abPower_cmd_val = self._base.get_repcap_cmd_value(abPower, repcap.AbPower)
		self._core.io.write_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:ABPower{abPower_cmd_val}', structure)

	def get(self, abPower=repcap.AbPower.Default) -> AbPowerStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:ABPower<nr> \n
		Snippet: value: AbPowerStruct = driver.configure.multiEval.limit.powerVsTime.abPower.get(abPower = repcap.AbPower.Default) \n
		Defines and activates limits for the average burst power, i.e. tolerances for ranges of template power control levels
		(TPCLs) . \n
			:param abPower: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AbPower')
			:return: structure: for return value, see the help for AbPowerStruct structure arguments."""
		abPower_cmd_val = self._base.get_repcap_cmd_value(abPower, repcap.AbPower)
		return self._core.io.query_struct(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:LIMit:PVTime:ABPower{abPower_cmd_val}?', self.__class__.AbPowerStruct())

	def clone(self) -> 'AbPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AbPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
