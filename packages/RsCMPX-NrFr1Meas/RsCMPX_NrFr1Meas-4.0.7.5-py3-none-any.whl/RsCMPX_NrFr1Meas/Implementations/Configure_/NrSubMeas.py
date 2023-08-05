from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrSubMeas:
	"""NrSubMeas commands group definition. 204 total commands, 9 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrSubMeas", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .NrSubMeas_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	@property
	def bwConfig(self):
		"""bwConfig commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bwConfig'):
			from .NrSubMeas_.BwConfig import BwConfig
			self._bwConfig = BwConfig(self._core, self._base)
		return self._bwConfig

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .NrSubMeas_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def ulDl(self):
		"""ulDl commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ulDl'):
			from .NrSubMeas_.UlDl import UlDl
			self._ulDl = UlDl(self._core, self._base)
		return self._ulDl

	@property
	def cc(self):
		"""cc commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .NrSubMeas_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def ccall(self):
		"""ccall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccall'):
			from .NrSubMeas_.Ccall import Ccall
			self._ccall = Ccall(self._core, self._base)
		return self._ccall

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .NrSubMeas_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def multiEval(self):
		"""multiEval commands group. 12 Sub-classes, 26 commands."""
		if not hasattr(self, '_multiEval'):
			from .NrSubMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def prach(self):
		"""prach commands group. 8 Sub-classes, 11 commands."""
		if not hasattr(self, '_prach'):
			from .NrSubMeas_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:BAND \n
		Snippet: value: enums.Band = driver.configure.nrSubMeas.get_band() \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . For Signal Path =
		Network, use [CONFigure:]SIGNaling:NRADio:CELL:RFSettings:FBINdicator. \n
			:return: band: TDD: OB34 | OB38 | ... | OB41 | OB48 | OB50 | OB51 | OB77 | ... | OB84 | OB86
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:BAND \n
		Snippet: driver.configure.nrSubMeas.set_band(band = enums.Band.OB1) \n
		Selects the operating band (OB) . The allowed input range depends on the duplex mode (FDD or TDD) . For Signal Path =
		Network, use [CONFigure:]SIGNaling:NRADio:CELL:RFSettings:FBINdicator. \n
			:param band: TDD: OB34 | OB38 | ... | OB41 | OB48 | OB50 | OB51 | OB77 | ... | OB84 | OB86
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:BAND {param}')

	def get_ncarrier(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NCARrier \n
		Snippet: value: int = driver.configure.nrSubMeas.get_ncarrier() \n
		No command help available \n
			:return: number: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, number: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NCARrier \n
		Snippet: driver.configure.nrSubMeas.set_ncarrier(number = 1) \n
		No command help available \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NCARrier {param}')

	def clone(self) -> 'NrSubMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrSubMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
