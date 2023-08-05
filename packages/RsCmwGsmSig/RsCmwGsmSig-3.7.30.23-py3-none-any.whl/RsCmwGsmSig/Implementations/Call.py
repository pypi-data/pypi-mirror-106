from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Call:
	"""Call commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("call", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cswitched'):
			from .Call_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	@property
	def pswitched(self):
		"""pswitched commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pswitched'):
			from .Call_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	@property
	def handover(self):
		"""handover commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_handover'):
			from .Call_.Handover import Handover
			self._handover = Handover(self._core, self._base)
		return self._handover

	def clone(self) -> 'Call':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Call(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
