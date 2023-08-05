from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 130 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def multiEval(self):
		"""multiEval commands group. 11 Sub-classes, 18 commands."""
		if not hasattr(self, '_multiEval'):
			from .Configure_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:BAND \n
		Snippet: value: enums.Band = driver.configure.get_band() \n
		Selects the GSM frequency band.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:BAND:BCCH
			- SENSe:GSM:SIGN<i>:BAND:TCH \n
			:return: band: G04 | G085 | G09 | G18 | G19 | GG08 G04: GSM400 G085: GSM850 G09: GSM900 G18: GSM1800 G19: GSM1900 GG08: GSMGT800
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:BAND \n
		Snippet: driver.configure.set_band(band = enums.Band.G04) \n
		Selects the GSM frequency band.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:BAND:BCCH
			- SENSe:GSM:SIGN<i>:BAND:TCH \n
			:param band: G04 | G085 | G09 | G18 | G19 | GG08 G04: GSM400 G085: GSM850 G09: GSM900 G18: GSM1800 G19: GSM1900 GG08: GSMGT800
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:BAND {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:CHANnel \n
		Snippet: value: int = driver.configure.get_channel() \n
		Selects the channel number. The channel number must be valid for the current frequency band, for dependencies see 'GSM
		Frequency Bands and Channels'. The corresponding center frequency (method RsCmwGsmMeas.Configure.RfSettings.frequency) is
		calculated and set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:ENABle
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:MAIO
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:HSN
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:SEQuence \n
			:return: channel: decimal GSM channel number Range: depends on frequency band
		"""
		response = self._core.io.query_str('CONFigure:GSM:MEASurement<Instance>:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:GSM:MEASurement<Instance>:CHANnel \n
		Snippet: driver.configure.set_channel(channel = 1) \n
		Selects the channel number. The channel number must be valid for the current frequency band, for dependencies see 'GSM
		Frequency Bands and Channels'. The corresponding center frequency (method RsCmwGsmMeas.Configure.RfSettings.frequency) is
		calculated and set.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:GSM:SIGN<i>:RFSettings:CHANnel
			- CONFigure:GSM:SIGN<i>:RFSettings:CHCCombined:TCH:CSWitched
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:ENABle
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:MAIO
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:HSN
			- CONFigure:GSM:SIGN<i>:RFSettings:HOPPing:SEQuence \n
			:param channel: decimal GSM channel number Range: depends on frequency band
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:GSM:MEASurement<Instance>:CHANnel {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
