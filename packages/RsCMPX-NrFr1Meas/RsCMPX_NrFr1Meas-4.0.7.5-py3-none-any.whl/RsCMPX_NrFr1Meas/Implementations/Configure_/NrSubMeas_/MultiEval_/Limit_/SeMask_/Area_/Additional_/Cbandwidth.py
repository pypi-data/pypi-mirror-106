from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbandwidth:
	"""Cbandwidth commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: ChannelBw, default value after init: ChannelBw.Bw5"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbandwidth", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_channelBw_get', 'repcap_channelBw_set', repcap.ChannelBw.Bw5)

	def repcap_channelBw_set(self, enum_value: repcap.ChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelBw.Default
		Default value after init: ChannelBw.Bw5"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_channelBw_get(self) -> repcap.ChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class CbandwidthStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the channel bandwidth
			- Frequency_End: float: Stop frequency of the area, relative to the edges of the channel bandwidth
			- Level: float: Upper limit for the area
			- Rbw: enums.RbwB: Resolution bandwidth to be used for the area Only a subset of the values is allowed, depending on table and bw. K030: 30 kHz K100: 100 kHz M1: 1 MHz PC1: 1 % of channel bandwidth PC2: 2 % of channel bandwidth"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.RbwB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.RbwB = None

	def set(self, structure: CbandwidthStruct, area=repcap.Area.Default, addTable=repcap.AddTable.Default, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:ADDitional<table>:CBANdwidth<bw> \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.seMask.area.additional.cbandwidth.set(value = [PROPERTY_STRUCT_NAME](), area = repcap.Area.Default, addTable = repcap.AddTable.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines additional requirements for the emission mask area number <area> (for NR SA) . The activation state, the area
		borders, an upper limit and the resolution bandwidth must be specified. The emission mask applies to the channel
		bandwidth <bw>. Several tables of additional requirements are available. \n
			:param structure: for set value, see the help for CbandwidthStruct structure arguments.
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param addTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Additional')
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')"""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		addTable_cmd_val = self._base.get_repcap_cmd_value(addTable, repcap.AddTable)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:ADDitional{addTable_cmd_val}:CBANdwidth{channelBw_cmd_val}', structure)

	def get(self, area=repcap.Area.Default, addTable=repcap.AddTable.Default, channelBw=repcap.ChannelBw.Default) -> CbandwidthStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:ADDitional<table>:CBANdwidth<bw> \n
		Snippet: value: CbandwidthStruct = driver.configure.nrSubMeas.multiEval.limit.seMask.area.additional.cbandwidth.get(area = repcap.Area.Default, addTable = repcap.AddTable.Default, channelBw = repcap.ChannelBw.Default) \n
		Defines additional requirements for the emission mask area number <area> (for NR SA) . The activation state, the area
		borders, an upper limit and the resolution bandwidth must be specified. The emission mask applies to the channel
		bandwidth <bw>. Several tables of additional requirements are available. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:param addTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Additional')
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
			:return: structure: for return value, see the help for CbandwidthStruct structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		addTable_cmd_val = self._base.get_repcap_cmd_value(addTable, repcap.AddTable)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:ADDitional{addTable_cmd_val}:CBANdwidth{channelBw_cmd_val}?', self.__class__.CbandwidthStruct())

	def clone(self) -> 'Cbandwidth':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbandwidth(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
