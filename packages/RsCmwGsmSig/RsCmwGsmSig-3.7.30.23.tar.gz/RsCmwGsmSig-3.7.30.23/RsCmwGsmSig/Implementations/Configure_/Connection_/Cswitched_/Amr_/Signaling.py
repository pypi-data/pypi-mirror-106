from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signaling:
	"""Signaling commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("signaling", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SignalingMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:SIGNaling:MODE \n
		Snippet: value: enums.SignalingMode = driver.configure.connection.cswitched.amr.signaling.get_mode() \n
		Specifies AMR signaling mode. \n
			:return: signaling_mode: LTRR | RATScch L3 RR, RATSCCH
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:SIGNaling:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SignalingMode)

	def set_mode(self, signaling_mode: enums.SignalingMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:SIGNaling:MODE \n
		Snippet: driver.configure.connection.cswitched.amr.signaling.set_mode(signaling_mode = enums.SignalingMode.LTRR) \n
		Specifies AMR signaling mode. \n
			:param signaling_mode: LTRR | RATScch L3 RR, RATSCCH
		"""
		param = Conversions.enum_scalar_to_str(signaling_mode, enums.SignalingMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:SIGNaling:MODE {param}')
