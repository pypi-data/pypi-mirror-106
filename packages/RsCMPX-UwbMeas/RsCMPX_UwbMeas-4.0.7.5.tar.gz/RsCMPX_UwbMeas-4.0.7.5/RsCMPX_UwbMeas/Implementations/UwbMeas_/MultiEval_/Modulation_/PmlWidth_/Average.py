from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.pmlWidth.average.fetch() \n
		Returns the width of the main lobe at a cross correlation magnitude of 0.8 for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: width: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.pmlWidth.average.read() \n
		Returns the width of the main lobe at a cross correlation magnitude of 0.8 for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: width: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus2:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage \n
		Snippet: value: enums.ResultStatus2 = driver.uwbMeas.multiEval.modulation.pmlWidth.average.calculate() \n
		Returns the width of the main lobe at a cross correlation magnitude of 0.8 for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: width: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:PMLWidth:AVERage?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
