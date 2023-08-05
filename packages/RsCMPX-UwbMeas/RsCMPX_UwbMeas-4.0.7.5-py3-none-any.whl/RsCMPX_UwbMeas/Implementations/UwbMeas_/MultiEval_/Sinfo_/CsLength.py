from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsLength:
	"""CsLength commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("csLength", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:CSLength \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.csLength.fetch() \n
		Returns the length 31, 91 or 127 of the code sequence for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: cs_length: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:CSLength?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:CSLength \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.csLength.read() \n
		Returns the length 31, 91 or 127 of the code sequence for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: cs_length: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:CSLength?', suppressed)
		return Conversions.str_to_int(response)
