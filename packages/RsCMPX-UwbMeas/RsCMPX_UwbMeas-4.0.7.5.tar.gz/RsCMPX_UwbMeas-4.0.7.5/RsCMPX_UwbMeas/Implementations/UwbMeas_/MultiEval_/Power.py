from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 60 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Power_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Power_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Power_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_minimum'):
			from .Power_.Minimum import Minimum
			self._minimum = Minimum(self._core, self._base)
		return self._minimum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Power_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def ppower(self):
		"""ppower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppower'):
			from .Power_.Ppower import Ppower
			self._ppower = Ppower(self._core, self._base)
		return self._ppower

	@property
	def ppPower(self):
		"""ppPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppPower'):
			from .Power_.PpPower import PpPower
			self._ppPower = PpPower(self._core, self._base)
		return self._ppPower

	@property
	def dpower(self):
		"""dpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpower'):
			from .Power_.Dpower import Dpower
			self._dpower = Dpower(self._core, self._base)
		return self._dpower

	@property
	def dpPower(self):
		"""dpPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpPower'):
			from .Power_.DpPower import DpPower
			self._dpPower = DpPower(self._core, self._base)
		return self._dpPower

	@property
	def msPower(self):
		"""msPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_msPower'):
			from .Power_.MsPower import MsPower
			self._msPower = MsPower(self._core, self._base)
		return self._msPower

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
