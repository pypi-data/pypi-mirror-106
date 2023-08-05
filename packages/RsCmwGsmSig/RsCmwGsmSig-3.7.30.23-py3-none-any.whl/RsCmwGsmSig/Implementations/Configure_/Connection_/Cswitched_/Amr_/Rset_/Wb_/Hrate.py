from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hrate:
	"""Hrate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hrate", core, parent)

	# noinspection PyTypeChecker
	def get_epsk(self) -> List[enums.WbCodec]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:WB:HRATe:EPSK \n
		Snippet: value: List[enums.WbCodec] = driver.configure.connection.cswitched.amr.rset.wb.hrate.get_epsk() \n
		Configures up to three supported modes for the half-rate wideband AMR codec (8PSK modulation) , i.e. assigns data rates
		to the modes. The three data rates must be different from each other. They are automatically sorted in descending order
		so that rate (mode 3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test model to less
		than 3 supported modes. \n
			:return: codec_mode: C0660 | C0885 | C1265 | ON | OFF Comma-separated list of 3 values: data rates for mode 3 to 1 6.6 kbit/s, 8.85 kbit/s, or 12.65 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:WB:HRATe:EPSK?')
		return Conversions.str_to_list_enum(response, enums.WbCodec)

	def set_epsk(self, codec_mode: List[enums.WbCodec]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:WB:HRATe:EPSK \n
		Snippet: driver.configure.connection.cswitched.amr.rset.wb.hrate.set_epsk(codec_mode = [WbCodec.C0660, WbCodec.ON]) \n
		Configures up to three supported modes for the half-rate wideband AMR codec (8PSK modulation) , i.e. assigns data rates
		to the modes. The three data rates must be different from each other. They are automatically sorted in descending order
		so that rate (mode 3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test model to less
		than 3 supported modes. \n
			:param codec_mode: C0660 | C0885 | C1265 | ON | OFF Comma-separated list of 3 values: data rates for mode 3 to 1 6.6 kbit/s, 8.85 kbit/s, or 12.65 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		param = Conversions.enum_list_to_str(codec_mode, enums.WbCodec)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:WB:HRATe:EPSK {param}')
