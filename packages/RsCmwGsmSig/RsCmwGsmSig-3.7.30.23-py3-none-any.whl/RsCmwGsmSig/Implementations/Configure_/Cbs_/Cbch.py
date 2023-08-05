from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbch:
	"""Cbch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbch", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:CBCH:ENABle \n
		Snippet: value: bool = driver.configure.cbs.cbch.get_enable() \n
		Enables CBS generally. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CBS:CBCH:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CBS:CBCH:ENABle \n
		Snippet: driver.configure.cbs.cbch.set_enable(enable = False) \n
		Enables CBS generally. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CBS:CBCH:ENABle {param}')
