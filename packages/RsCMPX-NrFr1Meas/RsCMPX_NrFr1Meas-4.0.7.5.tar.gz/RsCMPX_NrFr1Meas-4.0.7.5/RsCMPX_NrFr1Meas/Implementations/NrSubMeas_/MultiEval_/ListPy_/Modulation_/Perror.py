from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perror:
	"""Perror commands group definition. 42 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("perror", core, parent)

	@property
	def rms(self):
		"""rms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Perror_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Perror_.Peak import Peak
			self._peak = Peak(self._core, self._base)
		return self._peak

	@property
	def dmrs(self):
		"""dmrs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dmrs'):
			from .Perror_.Dmrs import Dmrs
			self._dmrs = Dmrs(self._core, self._base)
		return self._dmrs

	def clone(self) -> 'Perror':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Perror(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
