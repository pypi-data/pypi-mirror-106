from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 5 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	@property
	def mbep(self):
		"""mbep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mbep'):
			from .Cswitched_.Mbep import Mbep
			self._mbep = Mbep(self._core, self._base)
		return self._mbep

	@property
	def cbep(self):
		"""cbep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cbep'):
			from .Cswitched_.Cbep import Cbep
			self._cbep = Cbep(self._core, self._base)
		return self._cbep

	def get_nr_blocks(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:CSWitched:NRBLocks \n
		Snippet: value: int = driver.sense.rreport.cswitched.get_nr_blocks() \n
		Returns the number of blocks that theR&S CMW received in the UL since the beginning of the measurement. \n
			:return: nr_rec_blocks: Range: 0 to 63
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:CSWitched:NRBLocks?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
