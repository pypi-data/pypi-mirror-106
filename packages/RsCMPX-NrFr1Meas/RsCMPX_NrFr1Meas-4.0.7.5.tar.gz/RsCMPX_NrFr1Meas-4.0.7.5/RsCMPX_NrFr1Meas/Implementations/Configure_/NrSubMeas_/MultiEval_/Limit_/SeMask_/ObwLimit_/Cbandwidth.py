from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


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

	def set(self, obw_limit: float or bool, channelBw=repcap.ChannelBw.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CBANdwidth<bw> \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.seMask.obwLimit.cbandwidth.set(obw_limit = 1.0, channelBw = repcap.ChannelBw.Default) \n
		Defines an upper limit for the occupied bandwidth, depending on the channel bandwidth (for NR SA) . \n
			:param obw_limit: No help available
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')"""
		param = Conversions.decimal_or_bool_value_to_str(obw_limit)
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CBANdwidth{channelBw_cmd_val} {param}')

	def get(self, channelBw=repcap.ChannelBw.Default) -> float or bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CBANdwidth<bw> \n
		Snippet: value: float or bool = driver.configure.nrSubMeas.multiEval.limit.seMask.obwLimit.cbandwidth.get(channelBw = repcap.ChannelBw.Default) \n
		Defines an upper limit for the occupied bandwidth, depending on the channel bandwidth (for NR SA) . \n
			:param channelBw: optional repeated capability selector. Default value: Bw5 (settable in the interface 'Cbandwidth')
			:return: obw_limit: No help available"""
		channelBw_cmd_val = self._base.get_repcap_cmd_value(channelBw, repcap.ChannelBw)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:OBWLimit:CBANdwidth{channelBw_cmd_val}?')
		return Conversions.str_to_float_or_bool(response)

	def clone(self) -> 'Cbandwidth':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbandwidth(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
