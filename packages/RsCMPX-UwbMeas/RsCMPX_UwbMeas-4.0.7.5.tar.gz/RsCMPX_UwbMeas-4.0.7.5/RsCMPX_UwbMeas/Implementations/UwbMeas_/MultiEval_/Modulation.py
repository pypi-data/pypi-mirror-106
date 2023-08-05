from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 132 total commands, 17 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Modulation_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Modulation_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_extreme'):
			from .Modulation_.Extreme import Extreme
			self._extreme = Extreme(self._core, self._base)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Modulation_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def foffset(self):
		"""foffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Modulation_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	@property
	def ccError(self):
		"""ccError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccError'):
			from .Modulation_.CcError import CcError
			self._ccError = CcError(self._core, self._base)
		return self._ccError

	@property
	def smAccuracy(self):
		"""smAccuracy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_smAccuracy'):
			from .Modulation_.SmAccuracy import SmAccuracy
			self._smAccuracy = SmAccuracy(self._core, self._base)
		return self._smAccuracy

	@property
	def slPeak(self):
		"""slPeak commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_slPeak'):
			from .Modulation_.SlPeak import SlPeak
			self._slPeak = SlPeak(self._core, self._base)
		return self._slPeak

	@property
	def pmlWidth(self):
		"""pmlWidth commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmlWidth'):
			from .Modulation_.PmlWidth import PmlWidth
			self._pmlWidth = PmlWidth(self._core, self._base)
		return self._pmlWidth

	@property
	def stJitter(self):
		"""stJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_stJitter'):
			from .Modulation_.StJitter import StJitter
			self._stJitter = StJitter(self._core, self._base)
		return self._stJitter

	@property
	def spJitter(self):
		"""spJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_spJitter'):
			from .Modulation_.SpJitter import SpJitter
			self._spJitter = SpJitter(self._core, self._base)
		return self._spJitter

	@property
	def ctJitter(self):
		"""ctJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ctJitter'):
			from .Modulation_.CtJitter import CtJitter
			self._ctJitter = CtJitter(self._core, self._base)
		return self._ctJitter

	@property
	def cpJitter(self):
		"""cpJitter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpJitter'):
			from .Modulation_.CpJitter import CpJitter
			self._cpJitter = CpJitter(self._core, self._base)
		return self._cpJitter

	@property
	def sevm(self):
		"""sevm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sevm'):
			from .Modulation_.Sevm import Sevm
			self._sevm = Sevm(self._core, self._base)
		return self._sevm

	@property
	def cevm(self):
		"""cevm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cevm'):
			from .Modulation_.Cevm import Cevm
			self._cevm = Cevm(self._core, self._base)
		return self._cevm

	@property
	def nmse(self):
		"""nmse commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nmse'):
			from .Modulation_.Nmse import Nmse
			self._nmse = Nmse(self._core, self._base)
		return self._nmse

	@property
	def fofh(self):
		"""fofh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fofh'):
			from .Modulation_.Fofh import Fofh
			self._fofh = Fofh(self._core, self._base)
		return self._fofh

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
