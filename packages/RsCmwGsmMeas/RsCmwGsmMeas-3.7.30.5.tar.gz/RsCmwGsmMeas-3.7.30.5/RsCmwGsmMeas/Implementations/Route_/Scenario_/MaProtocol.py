from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaProtocol:
	"""MaProtocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maProtocol", core, parent)

	def set(self, controler: str = None) -> None:
		"""SCPI: ROUTe:GSM:MEASurement<Instance>:SCENario:MAPRotocol \n
		Snippet: driver.route.scenario.maProtocol.set(controler = '1') \n
		Activates the Measure@ProtocolTest scenario and optionally selects the controlling protocol test application. The signal
		routing and analyzer settings are ignored by the measurement application. Configure the corresponding settings within the
		protocol test application used in parallel. \n
			:param controler: string String parameter selecting the protocol test application e.g., 'Protocol Test1'
		"""
		param = ''
		if controler:
			param = Conversions.value_to_quoted_str(controler)
		self._core.io.write(f'ROUTe:GSM:MEASurement<Instance>:SCENario:MAPRotocol {param}'.strip())
