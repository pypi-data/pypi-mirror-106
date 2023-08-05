from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clean:
	"""Clean commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("clean", core, parent)

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Clean_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def sms(self):
		"""sms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Clean_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def elog(self):
		"""elog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elog'):
			from .Clean_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	def clone(self) -> 'Clean':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clean(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
