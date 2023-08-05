from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Area:
	"""Area commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Area, default value after init: Area.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("area", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_area_get', 'repcap_area_set', repcap.Area.Nr1)

	def repcap_area_set(self, enum_value: repcap.Area) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Area.Default
		Default value after init: Area.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_area_get(self) -> repcap.Area:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Enable: bool: No parameter help available
			- Area: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Area')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Area: float = None

	def set(self, structure: AreaStruct, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA<nr> \n
		Snippet: driver.configure.uwbMeas.multiEval.tsMask.limit.area.set(value = [PROPERTY_STRUCT_NAME](), area = repcap.Area.Default) \n
		Activates and defines an upper limit for the two areas of the spectral mask. \n
			:param structure: for set value, see the help for AreaStruct structure arguments.
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')"""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write_struct(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA{area_cmd_val}', structure)

	def get(self, area=repcap.Area.Default) -> AreaStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA<nr> \n
		Snippet: value: AreaStruct = driver.configure.uwbMeas.multiEval.tsMask.limit.area.get(area = repcap.Area.Default) \n
		Activates and defines an upper limit for the two areas of the spectral mask. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TSMask:LIMit:AREA{area_cmd_val}?', self.__class__.AreaStruct())

	def clone(self) -> 'Area':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Area(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
