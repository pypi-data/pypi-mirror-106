from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrSubMeas:
	"""NrSubMeas commands group definition. 15 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrSubMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 2 Sub-classes, 7 commands."""
		if not hasattr(self, '_multiEval'):
			from .NrSubMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_prach'):
			from .NrSubMeas_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	def clone(self) -> 'NrSubMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrSubMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
