from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 13 total commands, 0 Sub-groups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Power_Vs_Time: bool: OFF | ON Power vs. time ON: Evaluate results and show the view OFF: Do not evaluate results, hide the view (if applicable)
			- Evm: bool: OFF | ON Error vector magnitude
			- Magnitude_Error: bool: OFF | ON Magnitude error
			- Phase_Error: bool: OFF | ON Phase error
			- Iq: bool: OFF | ON I/Q constellation
			- Acp_Mod_Frequency: bool: OFF | ON ACP spectrum modulation frequency
			- Acp_Mod_Time: bool: OFF | ON ACP spectrum modulation time
			- Acp_Swit_Freq: bool: OFF | ON ACP spectrum switching frequency
			- Acp_Swit_Time: bool: OFF | ON ACP spectrum switching time
			- Mod_Scalar: bool: OFF | ON Scalar modulation results
			- Ber: bool: OFF | ON Bit error rate
			- Am_Pm: bool: OFF | ON AM-PM"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Power_Vs_Time'),
			ArgStruct.scalar_bool('Evm'),
			ArgStruct.scalar_bool('Magnitude_Error'),
			ArgStruct.scalar_bool('Phase_Error'),
			ArgStruct.scalar_bool('Iq'),
			ArgStruct.scalar_bool('Acp_Mod_Frequency'),
			ArgStruct.scalar_bool('Acp_Mod_Time'),
			ArgStruct.scalar_bool('Acp_Swit_Freq'),
			ArgStruct.scalar_bool('Acp_Swit_Time'),
			ArgStruct.scalar_bool('Mod_Scalar'),
			ArgStruct.scalar_bool('Ber'),
			ArgStruct.scalar_bool('Am_Pm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Power_Vs_Time: bool = None
			self.Evm: bool = None
			self.Magnitude_Error: bool = None
			self.Phase_Error: bool = None
			self.Iq: bool = None
			self.Acp_Mod_Frequency: bool = None
			self.Acp_Mod_Time: bool = None
			self.Acp_Swit_Freq: bool = None
			self.Acp_Swit_Time: bool = None
			self.Mod_Scalar: bool = None
			self.Ber: bool = None
			self.Am_Pm: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.multiEval.result.get_all() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:GSM:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult[:ALL] \n
		Snippet: driver.configure.multiEval.result.set_all(value = AllStruct()) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:GSM:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_power_vs_time(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: value: bool = driver.configure.multiEval.result.get_power_vs_time() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PVTime?')
		return Conversions.str_to_bool(response)

	def set_power_vs_time(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PVTime \n
		Snippet: driver.configure.multiEval.result.set_power_vs_time(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PVTime {param}')

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.multiEval.result.set_ev_magnitude(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_merror() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MERRor \n
		Snippet: driver.configure.multiEval.result.set_merror(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MERRor {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_perror() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PERRor \n
		Snippet: driver.configure.multiEval.result.set_perror(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:PERRor {param}')

	def get_sm_frequency(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMFRequency \n
		Snippet: value: bool = driver.configure.multiEval.result.get_sm_frequency() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMFRequency?')
		return Conversions.str_to_bool(response)

	def set_sm_frequency(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMFRequency \n
		Snippet: driver.configure.multiEval.result.set_sm_frequency(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMFRequency {param}')

	def get_sm_time(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMTime \n
		Snippet: value: bool = driver.configure.multiEval.result.get_sm_time() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMTime?')
		return Conversions.str_to_bool(response)

	def set_sm_time(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMTime \n
		Snippet: driver.configure.multiEval.result.set_sm_time(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SMTime {param}')

	def get_ss_frequency(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSFRequency \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ss_frequency() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSFRequency?')
		return Conversions.str_to_bool(response)

	def set_ss_frequency(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSFRequency \n
		Snippet: driver.configure.multiEval.result.set_ss_frequency(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSFRequency {param}')

	def get_ss_time(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSTime \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ss_time() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSTime?')
		return Conversions.str_to_bool(response)

	def set_ss_time(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSTime \n
		Snippet: driver.configure.multiEval.result.set_ss_time(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:SSTime {param}')

	def get_am_pm(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:AMPM \n
		Snippet: value: bool = driver.configure.multiEval.result.get_am_pm() \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:return: enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:AMPM?')
		return Conversions.str_to_bool(response)

	def set_am_pm(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:AMPM \n
		Snippet: driver.configure.multiEval.result.set_am_pm(enable = False) \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:param enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:AMPM {param}')

	def get_mscalar(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: value: bool = driver.configure.multiEval.result.get_mscalar() \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:return: enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MSCalar?')
		return Conversions.str_to_bool(response)

	def set_mscalar(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MSCalar \n
		Snippet: driver.configure.multiEval.result.set_mscalar(enable = False) \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:param enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:MSCalar {param}')

	def get_ber(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:BER \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ber() \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:return: enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:BER?')
		return Conversions.str_to_bool(response)

	def set_ber(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:BER \n
		Snippet: driver.configure.multiEval.result.set_ber(enable = False) \n
		Enables or disables the evaluation of the AM-PM results, the scalar modulation results, and the bit error rate (BER) . \n
			:param enable: ON | OFF ON: Evaluate results OFF: Do not evaluate results
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:BER {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:IQ \n
		Snippet: value: bool = driver.configure.multiEval.result.get_iq() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:return: enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:IQ \n
		Snippet: driver.configure.multiEval.result.set_iq(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement. The last
		mnemonic denotes the view type: Power vs. time, error vector magnitude, magnitude error, phase error, I/Q constellation,
		spectrum modulation frequency, spectrum modulation time, spectrum switching frequency, spectrum switching time. Use READ..
		.? queries to retrieve results for disabled views. \n
			:param enable: ON | OFF ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:MEValuation:RESult:IQ {param}')
