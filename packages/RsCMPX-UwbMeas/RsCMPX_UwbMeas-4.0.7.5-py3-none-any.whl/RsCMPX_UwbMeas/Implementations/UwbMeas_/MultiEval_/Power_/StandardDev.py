from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Preamble_Power: float: No parameter help available
			- Pre_Peak_Power: float: No parameter help available
			- Data_Power: float: No parameter help available
			- Data_Peak_Power: float: No parameter help available
			- Max_Spec_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Preamble_Power'),
			ArgStruct.scalar_float('Pre_Peak_Power'),
			ArgStruct.scalar_float('Data_Power'),
			ArgStruct.scalar_float('Data_Peak_Power'),
			ArgStruct.scalar_float('Max_Spec_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Preamble_Power: float = None
			self.Pre_Peak_Power: float = None
			self.Data_Power: float = None
			self.Data_Peak_Power: float = None
			self.Max_Spec_Power: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:SDEViation \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.standardDev.fetch() \n
		Return the current, average, extreme and standard deviation single value results for the selected packet number <PPDU>.
		The values described below are returned by FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:SDEViation?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:POWer:SDEViation \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.power.standardDev.read() \n
		Return the current, average, extreme and standard deviation single value results for the selected packet number <PPDU>.
		The values described below are returned by FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:POWer:SDEViation?', self.__class__.ResultData())
