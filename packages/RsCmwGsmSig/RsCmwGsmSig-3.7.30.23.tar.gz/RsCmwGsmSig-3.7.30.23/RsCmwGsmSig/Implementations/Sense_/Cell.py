from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cell", core, parent)

	@property
	def pswitched(self):
		"""pswitched commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pswitched'):
			from .Cell_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	def get_fnumber(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CELL:FNUMber \n
		Snippet: value: int = driver.sense.cell.get_fnumber() \n
		No command help available \n
			:return: frame_number: No help available
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CELL:FNUMber?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_cerror(self) -> enums.ConnectError:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CELL:CERRor \n
		Snippet: value: enums.ConnectError = driver.sense.cell.get_cerror() \n
		Returns error information related to the active CS/PS connection. \n
			:return: connection_error: NERRor | REJected | RLTimeout | PTIMeout | STIMeout | IGNored | ATIMeout NERRor: no error REJected: connection rejected RLTimeout: radio link timeout PTIMeout: paging timeout STIMeout: signaling timeout IGNored: connection ignored ATIMeout: alerting timeout
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CELL:CERRor?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectError)

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
