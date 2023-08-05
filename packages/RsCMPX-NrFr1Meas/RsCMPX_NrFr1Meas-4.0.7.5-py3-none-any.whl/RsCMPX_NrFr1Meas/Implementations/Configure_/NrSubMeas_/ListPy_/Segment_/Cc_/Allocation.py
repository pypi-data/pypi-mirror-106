from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Allocation:
	"""Allocation commands group definition. 3 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Allocation, default value after init: Allocation.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("allocation", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_allocation_get', 'repcap_allocation_set', repcap.Allocation.Nr1)

	def repcap_allocation_set(self, enum_value: repcap.Allocation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Allocation.Default
		Default value after init: Allocation.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_allocation_get(self) -> repcap.Allocation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Allocation_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	def clone(self) -> 'Allocation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Allocation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
