from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sinfo:
	"""Sinfo commands group definition. 18 total commands, 7 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sinfo", core, parent)

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_drate'):
			from .Sinfo_.Drate import Drate
			self._drate = Drate(self._core, self._base)
		return self._drate

	@property
	def phr(self):
		"""phr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_phr'):
			from .Sinfo_.Phr import Phr
			self._phr = Phr(self._core, self._base)
		return self._phr

	@property
	def asSymbols(self):
		"""asSymbols commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_asSymbols'):
			from .Sinfo_.AsSymbols import AsSymbols
			self._asSymbols = AsSymbols(self._core, self._base)
		return self._asSymbols

	@property
	def csLength(self):
		"""csLength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_csLength'):
			from .Sinfo_.CsLength import CsLength
			self._csLength = CsLength(self._core, self._base)
		return self._csLength

	@property
	def psdu(self):
		"""psdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Sinfo_.Psdu import Psdu
			self._psdu = Psdu(self._core, self._base)
		return self._psdu

	@property
	def dlength(self):
		"""dlength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlength'):
			from .Sinfo_.Dlength import Dlength
			self._dlength = Dlength(self._core, self._base)
		return self._dlength

	@property
	def cindex(self):
		"""cindex commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cindex'):
			from .Sinfo_.Cindex import Cindex
			self._cindex = Cindex(self._core, self._base)
		return self._cindex

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Data_Rate: float: No parameter help available
			- Phr_Crc: enums.Result: No parameter help available
			- Analysed_Sync_Sym: int: No parameter help available
			- Cs_Length: int: No parameter help available
			- Psdu_Length: int: No parameter help available
			- Delta_Length: int: No parameter help available
			- Code_Index: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Data_Rate'),
			ArgStruct.scalar_enum('Phr_Crc', enums.Result),
			ArgStruct.scalar_int('Analysed_Sync_Sym'),
			ArgStruct.scalar_int('Cs_Length'),
			ArgStruct.scalar_int('Psdu_Length'),
			ArgStruct.scalar_int('Delta_Length'),
			ArgStruct.scalar_int('Code_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Data_Rate: float = None
			self.Phr_Crc: enums.Result = None
			self.Analysed_Sync_Sym: int = None
			self.Cs_Length: int = None
			self.Psdu_Length: int = None
			self.Delta_Length: int = None
			self.Code_Index: int = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.sinfo.fetch() \n
		Return the current single value results for the selected packet number <PPDU>. The values described below are returned by
		FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.sinfo.read() \n
		Return the current single value results for the selected packet number <PPDU>. The values described below are returned by
		FETCh and READ commands. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo?', self.__class__.ResultData())

	def clone(self) -> 'Sinfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sinfo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
