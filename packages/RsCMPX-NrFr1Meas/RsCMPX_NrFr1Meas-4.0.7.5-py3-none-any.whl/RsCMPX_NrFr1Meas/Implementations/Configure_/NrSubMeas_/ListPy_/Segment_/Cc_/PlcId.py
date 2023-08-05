from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlcId:
	"""PlcId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("plcId", core, parent)

	def set(self, physical_cell_id: int, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:PLCid \n
		Snippet: driver.configure.nrSubMeas.listPy.segment.cc.plcId.set(physical_cell_id = 1, sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies the physical cell ID of carrier <cc> in segment <no>. \n
			:param physical_cell_id: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')"""
		param = Conversions.decimal_value_to_str(physical_cell_id)
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:PLCid {param}')

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:PLCid \n
		Snippet: value: int = driver.configure.nrSubMeas.listPy.segment.cc.plcId.get(sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		Specifies the physical cell ID of carrier <cc> in segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: physical_cell_id: No help available"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:PLCid?')
		return Conversions.str_to_int(response)
