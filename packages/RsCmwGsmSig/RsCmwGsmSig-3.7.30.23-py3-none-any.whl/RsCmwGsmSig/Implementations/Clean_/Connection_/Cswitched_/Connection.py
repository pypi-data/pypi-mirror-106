from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	@property
	def attempt(self):
		"""attempt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attempt'):
			from .Connection_.Attempt import Attempt
			self._attempt = Attempt(self._core, self._base)
		return self._attempt

	@property
	def reject(self):
		"""reject commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reject'):
			from .Connection_.Reject import Reject
			self._reject = Reject(self._core, self._base)
		return self._reject

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
