from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psdu:
	"""Psdu commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("psdu", core, parent)

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_length'):
			from .Psdu_.Length import Length
			self._length = Length(self._core, self._base)
		return self._length

	@property
	def crc(self):
		"""crc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_crc'):
			from .Psdu_.Crc import Crc
			self._crc = Crc(self._core, self._base)
		return self._crc

	def clone(self) -> 'Psdu':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Psdu(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
