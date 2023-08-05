from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crc:
	"""Crc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("crc", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.Result:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.sinfo.phr.crc.fetch() \n
		Returns the PHR checksum for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: crc: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)

	# noinspection PyTypeChecker
	def read(self) -> enums.Result:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC \n
		Snippet: value: enums.Result = driver.uwbMeas.multiEval.sinfo.phr.crc.read() \n
		Returns the PHR checksum for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: crc: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:CRC?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)
