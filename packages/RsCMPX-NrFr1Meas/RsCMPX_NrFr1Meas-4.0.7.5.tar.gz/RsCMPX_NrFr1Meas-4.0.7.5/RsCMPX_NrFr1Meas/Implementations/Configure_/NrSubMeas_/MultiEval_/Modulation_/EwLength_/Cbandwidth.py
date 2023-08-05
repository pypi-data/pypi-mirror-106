from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


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
			- Cyc_Prefix_Norm_15: int: Samples for normal CP, 15-kHz SC spacing
			- Cyc_Prefix_Norm_30: int: Samples for normal CP, 30-kHz SC spacing
			- Cyc_Prefix_Norm_60: int: Samples for normal CP, 60-kHz SC spacing
			- Cyc_Prefix_Extend: int: Samples for extended CP, 60-kHz SC spacing"""
		__meta_args_list = [
			ArgStruct.scalar_int('Cyc_Prefix_Norm_15'),
			ArgStruct.scalar_int('Cyc_Prefix_Norm_30'),
			ArgStruct.scalar_int('Cyc_Prefix_Norm_60'),
			ArgStruct.scalar_int('Cyc_Prefix_Extend')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cyc_Prefix_Norm_15: int = None
			self.Cyc_Prefix_Norm_30: int = None
			self.Cyc_Prefix_Norm_60: int = None
			self.Cyc_Prefix_Extend: int = None

	def set(self, structure: CbandwidthStruct, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: driver.configure.nrSubMeas.multiEval.modulation.ewLength.cbandwidth.set(value = [PROPERTY_STRUCT_NAME](), channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the cyclic prefix (CP) type and
		the SC spacing. \n
			:param structure: for set value, see the help for CbandwidthStruct structure arguments.
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')"""
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val}', structure)

	def get(self, channelBw=repcap.ChannelBw.Default) -> CbandwidthStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth<bw> \n
		Snippet: value: CbandwidthStruct = driver.configure.nrSubMeas.multiEval.modulation.ewLength.cbandwidth.get(channelBw = repcap.ChannelBw.Default) \n
		Specifies the EVM window length in samples for a selected channel bandwidth, depending on the cyclic prefix (CP) type and
		the SC spacing. \n
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
			:return: structure: for return value, see the help for CbandwidthStruct structure arguments."""
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:MODulation:EWLength:CBANdwidth{channelBw_cmd_val}?', self.__class__.CbandwidthStruct())

	def clone(self) -> 'Cbandwidth':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbandwidth(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
