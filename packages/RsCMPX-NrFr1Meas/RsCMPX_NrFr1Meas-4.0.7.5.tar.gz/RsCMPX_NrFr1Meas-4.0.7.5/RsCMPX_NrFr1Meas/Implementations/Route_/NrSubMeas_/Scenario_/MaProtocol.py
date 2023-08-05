from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaProtocol:
	"""MaProtocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maProtocol", core, parent)

	def set(self, controler: str = None) -> None:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario:MAPRotocol \n
		Snippet: driver.route.nrSubMeas.scenario.maProtocol.set(controler = '1') \n
		No command help available \n
			:param controler: No help available
		"""
		param = ''
		if controler:
			param = Conversions.value_to_quoted_str(controler)
		self._core.io.write(f'ROUTe:NRSub:MEASurement<Instance>:SCENario:MAPRotocol {param}'.strip())
