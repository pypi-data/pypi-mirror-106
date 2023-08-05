from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amr:
	"""Amr commands group definition. 25 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("amr", core, parent)

	@property
	def signaling(self):
		"""signaling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_signaling'):
			from .Amr_.Signaling import Signaling
			self._signaling = Signaling(self._core, self._base)
		return self._signaling

	@property
	def rset(self):
		"""rset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rset'):
			from .Amr_.Rset import Rset
			self._rset = Rset(self._core, self._base)
		return self._rset

	@property
	def cmode(self):
		"""cmode commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmode'):
			from .Amr_.Cmode import Cmode
			self._cmode = Cmode(self._core, self._base)
		return self._cmode

	@property
	def threshold(self):
		"""threshold commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_threshold'):
			from .Amr_.Threshold import Threshold
			self._threshold = Threshold(self._core, self._base)
		return self._threshold

	def clone(self) -> 'Amr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Amr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
