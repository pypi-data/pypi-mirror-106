from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Additional:
	"""Additional commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("additional", core, parent)

	def set(self, dmrs_length: int, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pusch.additional.set(dmrs_length = 1, carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <no>, allocation <a>. \n
			:param dmrs_length: Length of the DM-RS in symbols. The maximum value is limited by the 'maxLength' setting for the bandwidth part.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')"""
		param = Conversions.decimal_value_to_str(dmrs_length)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: value: int = driver.configure.nrSubMeas.cc.allocation.pusch.additional.get(carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: dmrs_length: Length of the DM-RS in symbols. The maximum value is limited by the 'maxLength' setting for the bandwidth part."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional?')
		return Conversions.str_to_int(response)
