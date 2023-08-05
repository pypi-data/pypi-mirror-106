from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 6 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("generator", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_scenario'):
			from .Generator_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Generator_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	def get_spath(self) -> str:
		"""SCPI: ROUTe:GPRF:GENerator<instance>:SPATh \n
		Snippet: value: str = driver.route.gprf.generator.get_spath() \n
		Selects the signal path for the generated signal, for signal output via an IF unit. Send the command to the R&S CMX500.
		For possible values, see method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.get_. \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SPATh?')
		return trim_str_response(response)

	def set_spath(self, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<instance>:SPATh \n
		Snippet: driver.route.gprf.generator.set_spath(signal_path = '1') \n
		Selects the signal path for the generated signal, for signal output via an IF unit. Send the command to the R&S CMX500.
		For possible values, see method RsCMPX_Gprf.Catalog.Gprf.Generator.Spath.get_. \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SPATh {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.GenScenario: No parameter help available
			- Master: str: No parameter help available
			- Tx_Connector: enums.TxConnector: No parameter help available
			- Rf_Converter: enums.TxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.GenScenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.GenScenario = None
			self.Master: str = None
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance> \n
		Snippet: value: ValueStruct = driver.route.gprf.generator.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:GENerator<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
