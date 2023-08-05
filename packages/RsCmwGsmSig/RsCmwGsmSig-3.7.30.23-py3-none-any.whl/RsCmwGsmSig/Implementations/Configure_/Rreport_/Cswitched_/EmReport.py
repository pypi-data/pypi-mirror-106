from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmReport:
	"""EmReport commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("emReport", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RREPort:CSWitched:EMReport:ENABle \n
		Snippet: value: bool = driver.configure.rreport.cswitched.emReport.get_enable() \n
		Enables or disables MS enhanced measurement reports. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:RREPort:CSWitched:EMReport:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:RREPort:CSWitched:EMReport:ENABle \n
		Snippet: driver.configure.rreport.cswitched.emReport.set_enable(enable = False) \n
		Enables or disables MS enhanced measurement reports. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:RREPort:CSWitched:EMReport:ENABle {param}')
