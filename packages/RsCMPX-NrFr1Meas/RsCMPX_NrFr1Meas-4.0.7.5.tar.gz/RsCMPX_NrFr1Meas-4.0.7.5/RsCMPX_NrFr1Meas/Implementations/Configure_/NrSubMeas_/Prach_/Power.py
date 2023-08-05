from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	def get_hdmode(self) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:POWer:HDMode \n
		Snippet: value: bool = driver.configure.nrSubMeas.prach.power.get_hdmode() \n
		No command help available \n
			:return: high_dynamic_mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:PRACh:POWer:HDMode?')
		return Conversions.str_to_bool(response)

	def set_hdmode(self, high_dynamic_mode: bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:POWer:HDMode \n
		Snippet: driver.configure.nrSubMeas.prach.power.set_hdmode(high_dynamic_mode = False) \n
		No command help available \n
			:param high_dynamic_mode: No help available
		"""
		param = Conversions.bool_to_str(high_dynamic_mode)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:POWer:HDMode {param}')
