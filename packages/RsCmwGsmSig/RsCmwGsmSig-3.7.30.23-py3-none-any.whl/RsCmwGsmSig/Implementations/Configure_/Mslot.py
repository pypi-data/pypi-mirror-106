from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mslot:
	"""Mslot commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mslot", core, parent)

	def get_uplink(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:MSLot:UL \n
		Snippet: value: int = driver.configure.mslot.get_uplink() \n
		Specifies the uplink measurement slot, i.e. the slot evaluated by measurements running in parallel to the 'GSM Signaling'
		application. \n
			:return: slot: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:MSLot:UL?')
		return Conversions.str_to_int(response)

	def set_uplink(self, slot: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:MSLot:UL \n
		Snippet: driver.configure.mslot.set_uplink(slot = 1) \n
		Specifies the uplink measurement slot, i.e. the slot evaluated by measurements running in parallel to the 'GSM Signaling'
		application. \n
			:param slot: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(slot)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:MSLot:UL {param}')
