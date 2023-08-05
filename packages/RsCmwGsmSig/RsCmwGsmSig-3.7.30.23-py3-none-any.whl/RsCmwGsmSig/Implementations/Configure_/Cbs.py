from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbs:
	"""Cbs commands group definition. 12 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbs", core, parent)

	@property
	def cbch(self):
		"""cbch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbch'):
			from .Cbs_.Cbch import Cbch
			self._cbch = Cbch(self._core, self._base)
		return self._cbch

	@property
	def drx(self):
		"""drx commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_drx'):
			from .Cbs_.Drx import Drx
			self._drx = Drx(self._core, self._base)
		return self._drx

	@property
	def message(self):
		"""message commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_message'):
			from .Cbs_.Message import Message
			self._message = Message(self._core, self._base)
		return self._message

	def clone(self) -> 'Cbs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
