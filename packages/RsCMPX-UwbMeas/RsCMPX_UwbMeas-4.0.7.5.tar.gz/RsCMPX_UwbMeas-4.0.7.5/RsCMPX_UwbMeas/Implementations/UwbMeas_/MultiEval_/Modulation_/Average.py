from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Freq_Offset_Hz: float: No parameter help available
			- Freq_Offset: float: No parameter help available
			- Chip_Clock_Error: float: No parameter help available
			- Pulse_Nsme: float: No parameter help available
			- Sym_Mod_Accuracy: float: No parameter help available
			- Side_Lobe_Peak: float: No parameter help available
			- Pulse_Ml_Width: float: No parameter help available
			- Sym_Time_Jitter: float: RMS time jitter value averaged over all the detected preamble symbols
			- Sym_Phase_Jitter: float: RMS phase jitter value averaged over all the detected preamble symbols
			- Chip_Time_Jitter: float: No parameter help available
			- Chip_Phase_Jitter: float: No parameter help available
			- Symbol_Evm: float: No parameter help available
			- Chip_Evm: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Freq_Offset_Hz'),
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct.scalar_float('Chip_Clock_Error'),
			ArgStruct.scalar_float('Pulse_Nsme'),
			ArgStruct.scalar_float('Sym_Mod_Accuracy'),
			ArgStruct.scalar_float('Side_Lobe_Peak'),
			ArgStruct.scalar_float('Pulse_Ml_Width'),
			ArgStruct.scalar_float('Sym_Time_Jitter'),
			ArgStruct.scalar_float('Sym_Phase_Jitter'),
			ArgStruct.scalar_float('Chip_Time_Jitter'),
			ArgStruct.scalar_float('Chip_Phase_Jitter'),
			ArgStruct.scalar_float('Symbol_Evm'),
			ArgStruct.scalar_float('Chip_Evm')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Freq_Offset_Hz: float = None
			self.Freq_Offset: float = None
			self.Chip_Clock_Error: float = None
			self.Pulse_Nsme: float = None
			self.Sym_Mod_Accuracy: float = None
			self.Side_Lobe_Peak: float = None
			self.Pulse_Ml_Width: float = None
			self.Sym_Time_Jitter: float = None
			self.Sym_Phase_Jitter: float = None
			self.Chip_Time_Jitter: float = None
			self.Chip_Phase_Jitter: float = None
			self.Symbol_Evm: float = None
			self.Chip_Evm: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:AVERage \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.average.fetch() \n
		Return the current, average, extreme and standard deviation single value results for the selected packet number <PPDU>.
		The values described below are returned by FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:AVERage?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:AVERage \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.modulation.average.read() \n
		Return the current, average, extreme and standard deviation single value results for the selected packet number <PPDU>.
		The values described below are returned by FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:AVERage?', self.__class__.ResultData())
