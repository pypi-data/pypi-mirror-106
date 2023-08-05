from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 13 total commands, 8 Sub-groups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, enum_value: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def txBwidth(self):
		"""txBwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_txBwidth'):
			from .Cc_.TxBwidth import TxBwidth
			self._txBwidth = TxBwidth(self._core, self._base)
		return self._txBwidth

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Cc_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cc_.Cbandwidth import Cbandwidth
			self._cbandwidth = Cbandwidth(self._core, self._base)
		return self._cbandwidth

	@property
	def plcId(self):
		"""plcId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plcId'):
			from .Cc_.PlcId import PlcId
			self._plcId = PlcId(self._core, self._base)
		return self._plcId

	@property
	def taPosition(self):
		"""taPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taPosition'):
			from .Cc_.TaPosition import TaPosition
			self._taPosition = TaPosition(self._core, self._base)
		return self._taPosition

	@property
	def bwPart(self):
		"""bwPart commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwPart'):
			from .Cc_.BwPart import BwPart
			self._bwPart = BwPart(self._core, self._base)
		return self._bwPart

	@property
	def nallocations(self):
		"""nallocations commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nallocations'):
			from .Cc_.Nallocations import Nallocations
			self._nallocations = Nallocations(self._core, self._base)
		return self._nallocations

	@property
	def allocation(self):
		"""allocation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_allocation'):
			from .Cc_.Allocation import Allocation
			self._allocation = Allocation(self._core, self._base)
		return self._allocation

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
