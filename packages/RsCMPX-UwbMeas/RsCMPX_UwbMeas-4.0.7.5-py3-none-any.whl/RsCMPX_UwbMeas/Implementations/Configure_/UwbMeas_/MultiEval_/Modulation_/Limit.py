from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	# noinspection PyTypeChecker
	class FoffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get_foffset(self) -> FoffsetStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:FOFFset \n
		Snippet: value: FoffsetStruct = driver.configure.uwbMeas.multiEval.modulation.limit.get_foffset() \n
		Specifies a positive or negative frequency offset to be added to the channel center frequency (method RsCMPX_UwbMeas.
		Configure.UwbMeas.RfSettings.frequency) . \n
			:return: structure: for return value, see the help for FoffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:FOFFset?', self.__class__.FoffsetStruct())

	def set_foffset(self, value: FoffsetStruct) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:FOFFset \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.set_foffset(value = FoffsetStruct()) \n
		Specifies a positive or negative frequency offset to be added to the channel center frequency (method RsCMPX_UwbMeas.
		Configure.UwbMeas.RfSettings.frequency) . \n
			:param value: see the help for FoffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:FOFFset', value)

	# noinspection PyTypeChecker
	class CcErrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get_cc_error(self) -> CcErrorStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:CCERor \n
		Snippet: value: CcErrorStruct = driver.configure.uwbMeas.multiEval.modulation.limit.get_cc_error() \n
		Activates and defines an upper limit for the chip clock error. \n
			:return: structure: for return value, see the help for CcErrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:CCERor?', self.__class__.CcErrorStruct())

	def set_cc_error(self, value: CcErrorStruct) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:CCERor \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.set_cc_error(value = CcErrorStruct()) \n
		Activates and defines an upper limit for the chip clock error. \n
			:param value: see the help for CcErrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:CCERor', value)

	# noinspection PyTypeChecker
	class SmAccuracyStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get_sm_accuracy(self) -> SmAccuracyStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SMACcuracy \n
		Snippet: value: SmAccuracyStruct = driver.configure.uwbMeas.multiEval.modulation.limit.get_sm_accuracy() \n
		Activates and defines a lower limit for the symbol modulation accuracy. \n
			:return: structure: for return value, see the help for SmAccuracyStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SMACcuracy?', self.__class__.SmAccuracyStruct())

	def set_sm_accuracy(self, value: SmAccuracyStruct) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SMACcuracy \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.set_sm_accuracy(value = SmAccuracyStruct()) \n
		Activates and defines a lower limit for the symbol modulation accuracy. \n
			:param value: see the help for SmAccuracyStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SMACcuracy', value)

	# noinspection PyTypeChecker
	class SlPeakStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get_sl_peak(self) -> SlPeakStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SLPeak \n
		Snippet: value: SlPeakStruct = driver.configure.uwbMeas.multiEval.modulation.limit.get_sl_peak() \n
		Activates and defines an upper limit for the pulse side lobe peak. \n
			:return: structure: for return value, see the help for SlPeakStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SLPeak?', self.__class__.SlPeakStruct())

	def set_sl_peak(self, value: SlPeakStruct) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SLPeak \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.set_sl_peak(value = SlPeakStruct()) \n
		Activates and defines an upper limit for the pulse side lobe peak. \n
			:param value: see the help for SlPeakStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:SLPeak', value)

	# noinspection PyTypeChecker
	class PmlWidthStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get_pml_width(self) -> PmlWidthStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth \n
		Snippet: value: PmlWidthStruct = driver.configure.uwbMeas.multiEval.modulation.limit.get_pml_width() \n
		Activates and defines a lower limit for the pulse main lobe width. \n
			:return: structure: for return value, see the help for PmlWidthStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth?', self.__class__.PmlWidthStruct())

	def set_pml_width(self, value: PmlWidthStruct) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.set_pml_width(value = PmlWidthStruct()) \n
		Activates and defines a lower limit for the pulse main lobe width. \n
			:param value: see the help for PmlWidthStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth', value)
