from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	# noinspection PyTypeChecker
	class HighStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Valid: bool: OFF | ON OFF: use individual thresholds defined by separate commands ON: use common threshold defined by this command
			- High: int: Range: 0 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('High')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.High: int = None

	def get_high(self) -> HighStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:ALL:THResholds:HIGH \n
		Snippet: value: HighStruct = driver.configure.ncell.all.thresholds.get_high() \n
		Configures a common reselection high threshold value applicable to all technologies. Alternatively to a common threshold
		you can also use individual thresholds.
		They are defined per technology via the commands CONFigure:GSM:SIGN<i>:NCELl:<Technology>:THResholds:HIGH. The parameter
		<Valid> selects whether common or individual thresholds are used. \n
			:return: structure: for return value, see the help for HighStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:NCELl:ALL:THResholds:HIGH?', self.__class__.HighStruct())

	def set_high(self, value: HighStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:NCELl:ALL:THResholds:HIGH \n
		Snippet: driver.configure.ncell.all.thresholds.set_high(value = HighStruct()) \n
		Configures a common reselection high threshold value applicable to all technologies. Alternatively to a common threshold
		you can also use individual thresholds.
		They are defined per technology via the commands CONFigure:GSM:SIGN<i>:NCELl:<Technology>:THResholds:HIGH. The parameter
		<Valid> selects whether common or individual thresholds are used. \n
			:param value: see the help for HighStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:NCELl:ALL:THResholds:HIGH', value)
