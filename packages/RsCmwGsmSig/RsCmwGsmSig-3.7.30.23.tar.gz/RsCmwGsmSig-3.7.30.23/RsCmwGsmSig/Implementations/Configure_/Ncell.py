from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncell:
	"""Ncell commands group definition. 9 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ncell", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .Ncell_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def lte(self):
		"""lte commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Ncell_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def gsm(self):
		"""gsm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Ncell_.Gsm import Gsm
			self._gsm = Gsm(self._core, self._base)
		return self._gsm

	@property
	def wcdma(self):
		"""wcdma commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wcdma'):
			from .Ncell_.Wcdma import Wcdma
			self._wcdma = Wcdma(self._core, self._base)
		return self._wcdma

	@property
	def tdscdma(self):
		"""tdscdma commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdscdma'):
			from .Ncell_.Tdscdma import Tdscdma
			self._tdscdma = Tdscdma(self._core, self._base)
		return self._tdscdma

	def clone(self) -> 'Ncell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ncell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
