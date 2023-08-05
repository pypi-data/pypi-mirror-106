from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsrQam:
	"""HsrQam commands group definition. 4 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: HsrQAM, default value after init: HsrQAM.QAM16"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hsrQam", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_hsrQAM_get', 'repcap_hsrQAM_set', repcap.HsrQAM.QAM16)

	def repcap_hsrQAM_set(self, enum_value: repcap.HsrQAM) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HsrQAM.Default
		Default value after init: HsrQAM.QAM16"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_hsrQAM_get(self) -> repcap.HsrQAM:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def mbep(self):
		"""mbep commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbep'):
			from .HsrQam_.Mbep import Mbep
			self._mbep = Mbep(self._core, self._base)
		return self._mbep

	@property
	def cbep(self):
		"""cbep commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbep'):
			from .HsrQam_.Cbep import Cbep
			self._cbep = Cbep(self._core, self._base)
		return self._cbep

	def clone(self) -> 'HsrQam':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HsrQam(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
