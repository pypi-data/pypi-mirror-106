from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	def get_tch(self) -> float:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:LEVel:TCH \n
		Snippet: value: float = driver.prepare.handover.level.get_tch() \n
		Defines the absolute TCH/PDCH level in the destination GSM band. \n
			:return: level: Range: Depending on RF connector (-130 dBm to 0 dBm for RFx COM) ; please also notice the ranges quoted in the data sheet. , Unit: dBm
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:LEVel:TCH?')
		return Conversions.str_to_float(response)

	def set_tch(self, level: float) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:LEVel:TCH \n
		Snippet: driver.prepare.handover.level.set_tch(level = 1.0) \n
		Defines the absolute TCH/PDCH level in the destination GSM band. \n
			:param level: Range: Depending on RF connector (-130 dBm to 0 dBm for RFx COM) ; please also notice the ranges quoted in the data sheet. , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:LEVel:TCH {param}')
