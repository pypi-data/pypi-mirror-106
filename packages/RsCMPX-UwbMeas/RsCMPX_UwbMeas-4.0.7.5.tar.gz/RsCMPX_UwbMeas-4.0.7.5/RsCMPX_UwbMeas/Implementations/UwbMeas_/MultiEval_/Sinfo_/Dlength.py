from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlength:
	"""Dlength commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dlength", core, parent)

	def fetch(self) -> int:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:DLENgth \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.dlength.fetch() \n
		Returns the oversampling factor (delta length) of the code sequence to create a preamble symbol for the selected packet
		number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: length: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:DLENgth?', suppressed)
		return Conversions.str_to_int(response)

	def read(self) -> int:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:DLENgth \n
		Snippet: value: int = driver.uwbMeas.multiEval.sinfo.dlength.read() \n
		Returns the oversampling factor (delta length) of the code sequence to create a preamble symbol for the selected packet
		number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: length: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:DLENgth?', suppressed)
		return Conversions.str_to_int(response)
