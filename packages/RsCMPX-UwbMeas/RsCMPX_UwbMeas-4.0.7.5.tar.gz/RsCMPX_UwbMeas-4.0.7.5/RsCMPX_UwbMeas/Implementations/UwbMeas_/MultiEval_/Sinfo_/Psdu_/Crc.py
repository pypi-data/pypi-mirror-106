from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crc:
	"""Crc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("crc", core, parent)

	def fetch(self) -> bool:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC \n
		Snippet: value: bool = driver.uwbMeas.multiEval.sinfo.psdu.crc.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: crc: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC?', suppressed)
		return Conversions.str_to_bool(response)

	def read(self) -> bool:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC \n
		Snippet: value: bool = driver.uwbMeas.multiEval.sinfo.psdu.crc.read() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: crc: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PSDU:CRC?', suppressed)
		return Conversions.str_to_bool(response)
