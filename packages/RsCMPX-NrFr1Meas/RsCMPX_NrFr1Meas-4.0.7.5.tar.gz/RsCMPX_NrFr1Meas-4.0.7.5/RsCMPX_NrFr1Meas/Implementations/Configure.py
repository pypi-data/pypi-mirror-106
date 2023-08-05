from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 204 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def nrSubMeas(self):
		"""nrSubMeas commands group. 9 Sub-classes, 2 commands."""
		if not hasattr(self, '_nrSubMeas'):
			from .Configure_.NrSubMeas import NrSubMeas
			self._nrSubMeas = NrSubMeas(self._core, self._base)
		return self._nrSubMeas

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
