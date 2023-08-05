from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbep:
	"""Cbep commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbep", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Cbep_.Range import Range
			self._range = Range(self._core, self._base)
		return self._range

	def get(self, hsrQAM=repcap.HsrQAM.Default) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:HSRQam<ModOrder>:CBEP \n
		Snippet: value: int = driver.sense.rreport.hsrQam.cbep.get(hsrQAM = repcap.HsrQAM.Default) \n
		Returns the 'CV BEP', reported by the MS as dimensionless index for a 16-QAM or 32-QAM modulated DL signal with higher
		symbol rate (HSR) . \n
			:param hsrQAM: optional repeated capability selector. Default value: QAM16 (settable in the interface 'HsrQam')
			:return: cv_bep_qam_hsr: Range: 0 to 7"""
		hsrQAM_cmd_val = self._base.get_repcap_cmd_value(hsrQAM, repcap.HsrQAM)
		response = self._core.io.query_str(f'SENSe:GSM:SIGNaling<Instance>:RREPort:HSRQam{hsrQAM_cmd_val}:CBEP?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Cbep':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbep(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
