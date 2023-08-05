from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:NCCorr:CURRent \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.ncCorr.current.fetch() \n
		Returns the values of the normalized cross correlation trace. The current and average values can be retrieved. See also
		'Square Normalized Cross Correlation'. \n
		Suppressed linked return values: reliability \n
			:return: correlation: Comma-separated list of cross correlation values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:NCCorr:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:NCCorr:CURRent \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.ncCorr.current.read() \n
		Returns the values of the normalized cross correlation trace. The current and average values can be retrieved. See also
		'Square Normalized Cross Correlation'. \n
		Suppressed linked return values: reliability \n
			:return: correlation: Comma-separated list of cross correlation values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:NCCorr:CURRent?', suppressed)
		return response
