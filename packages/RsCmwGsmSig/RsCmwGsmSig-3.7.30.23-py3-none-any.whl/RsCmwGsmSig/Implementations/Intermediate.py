from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Intermediate:
	"""Intermediate commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("intermediate", core, parent)

	@property
	def ber(self):
		"""ber commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ber'):
			from .Intermediate_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def bler(self):
		"""bler commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bler'):
			from .Intermediate_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	def clone(self) -> 'Intermediate':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Intermediate(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
