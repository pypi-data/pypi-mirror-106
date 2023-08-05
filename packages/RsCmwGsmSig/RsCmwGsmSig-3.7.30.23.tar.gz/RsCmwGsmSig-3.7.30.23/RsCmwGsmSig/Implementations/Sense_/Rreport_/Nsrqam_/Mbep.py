from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbep:
	"""Mbep commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mbep", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Mbep_.Range import Range
			self._range = Range(self._core, self._base)
		return self._range

	def get(self, nsrQAM=repcap.NsrQAM.Default) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:NSRQam<ModOrder>:MBEP \n
		Snippet: value: int = driver.sense.rreport.nsrqam.mbep.get(nsrQAM = repcap.NsrQAM.Default) \n
		Returns the 'Mean BEP', reported by the MS as dimensionless index for a 16-QAM or 32-QAM modulated DL signal with normal
		symbol rate (NSR) . \n
			:param nsrQAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'Nsrqam')
			:return: mean_bep_qam_nsr: Range: 0 to 31"""
		nsrQAM_cmd_val = self._base.get_repcap_cmd_value(nsrQAM, repcap.NsrQAM)
		response = self._core.io.query_str(f'SENSe:GSM:SIGNaling<Instance>:RREPort:NSRQam{nsrQAM_cmd_val}:MBEP?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Mbep':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbep(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
