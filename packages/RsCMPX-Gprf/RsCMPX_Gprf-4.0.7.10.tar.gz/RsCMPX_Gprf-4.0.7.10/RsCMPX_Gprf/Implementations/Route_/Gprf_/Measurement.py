from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 9 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_scenario'):
			from .Measurement_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Measurement_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	def get_spath(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<instance>:SPATh \n
		Snippet: value: str = driver.route.gprf.measurement.get_spath() \n
		Selects the signal path for the measured signal, for signal input via an IF unit. Send the command to the R&S CMX500. For
		possible values, see method RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SPATh?')
		return trim_str_response(response)

	def set_spath(self, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<instance>:SPATh \n
		Snippet: driver.route.gprf.measurement.set_spath(signal_path = '1') \n
		Selects the signal path for the measured signal, for signal input via an IF unit. Send the command to the R&S CMX500. For
		possible values, see method RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SPATh {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.MeasScenario: No parameter help available
			- Master: str: No parameter help available
			- Rf_Connector: enums.RfConnector: No parameter help available
			- Rf_Converter: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.MeasScenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Rf_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.MeasScenario = None
			self.Master: str = None
			self.Rf_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance> \n
		Snippet: value: ValueStruct = driver.route.gprf.measurement.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
