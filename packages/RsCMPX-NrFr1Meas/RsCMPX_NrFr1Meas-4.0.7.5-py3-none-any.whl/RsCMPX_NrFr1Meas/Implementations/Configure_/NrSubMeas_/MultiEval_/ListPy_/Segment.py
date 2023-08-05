from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 9 total commands, 9 Sub-groups, 0 group commands
	Repeated Capability: SEGMent, default value after init: SEGMent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("segment", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_sEGMent_get', 'repcap_sEGMent_set', repcap.SEGMent.Nr1)

	def repcap_sEGMent_set(self, enum_value: repcap.SEGMent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SEGMent.Default
		Default value after init: SEGMent.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_sEGMent_get(self) -> repcap.SEGMent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def setup(self):
		"""setup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_setup'):
			from .Segment_.Setup import Setup
			self._setup = Setup(self._core, self._base)
		return self._setup

	@property
	def puschConfig(self):
		"""puschConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_puschConfig'):
			from .Segment_.PuschConfig import PuschConfig
			self._puschConfig = PuschConfig(self._core, self._base)
		return self._puschConfig

	@property
	def fdistance(self):
		"""fdistance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdistance'):
			from .Segment_.Fdistance import Fdistance
			self._fdistance = Fdistance(self._core, self._base)
		return self._fdistance

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Segment_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def seMask(self):
		"""seMask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seMask'):
			from .Segment_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Segment_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pmonitor(self):
		"""pmonitor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmonitor'):
			from .Segment_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Segment_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .Segment_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
