from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr:
	"""Nr commands group definition. 12 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nr", core, parent)

	@property
	def negativ(self):
		"""negativ commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_negativ'):
			from .Nr_.Negativ import Negativ
			self._negativ = Negativ(self._core, self._base)
		return self._negativ

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Nr_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def positiv(self):
		"""positiv commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_positiv'):
			from .Nr_.Positiv import Positiv
			self._positiv = Positiv(self._core, self._base)
		return self._positiv

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Nr_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	def clone(self) -> 'Nr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
