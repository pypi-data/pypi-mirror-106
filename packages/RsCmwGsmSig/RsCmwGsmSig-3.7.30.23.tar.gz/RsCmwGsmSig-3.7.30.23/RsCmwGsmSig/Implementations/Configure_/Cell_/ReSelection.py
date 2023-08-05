from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReSelection:
	"""ReSelection commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reSelection", core, parent)

	@property
	def quality(self):
		"""quality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_quality'):
			from .ReSelection_.Quality import Quality
			self._quality = Quality(self._core, self._base)
		return self._quality

	def get_tre_selection(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:TRESelection \n
		Snippet: value: int = driver.configure.cell.reSelection.get_tre_selection() \n
		Sets the time hysteresis for the cell reselection algorithm. \n
			:return: tre_selection: Range: 5 s to 20 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:TRESelection?')
		return Conversions.str_to_int(response)

	def set_tre_selection(self, tre_selection: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:TRESelection \n
		Snippet: driver.configure.cell.reSelection.set_tre_selection(tre_selection = 1) \n
		Sets the time hysteresis for the cell reselection algorithm. \n
			:param tre_selection: Range: 5 s to 20 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(tre_selection)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:TRESelection {param}')

	def get_hysteresis(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:HYSTeresis \n
		Snippet: value: int = driver.configure.cell.reSelection.get_hysteresis() \n
		Sets the hysteresis for the cell reselection algorithm. \n
			:return: hysteresis: Range: 0 dB to 14 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:HYSTeresis?')
		return Conversions.str_to_int(response)

	def set_hysteresis(self, hysteresis: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<instance>:CELL:RESelection:HYSTeresis \n
		Snippet: driver.configure.cell.reSelection.set_hysteresis(hysteresis = 1) \n
		Sets the hysteresis for the cell reselection algorithm. \n
			:param hysteresis: Range: 0 dB to 14 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CELL:RESelection:HYSTeresis {param}')

	def clone(self) -> 'ReSelection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReSelection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
