from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 6 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Scenario_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .Scenario_.MaProtocol import MaProtocol
			self._maProtocol = MaProtocol(self._core, self._base)
		return self._maProtocol

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RfConnector: RF connector for the input path Single R&S CMW500: RFnC for RF n COM CMWflexx: RabC for CMW a, connector RF b COM
			- Rf_Converter: enums.RxConverter: RX module for the input path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.gprf.measurement.scenario.get_salone() \n
		Selects the signal path for the measured signal, for signal input via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.gprf.measurement.scenario.set_salone(value = SaloneStruct()) \n
		Selects the signal path for the measured signal, for signal input via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone', value)

	def get_cspath(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: str = driver.route.gprf.measurement.scenario.get_cspath() \n
		No command help available \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath?')
		return trim_str_response(response)

	def set_cspath(self, master: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.gprf.measurement.scenario.set_cspath(master = '1') \n
		No command help available \n
			:param master: No help available
		"""
		param = Conversions.value_to_quoted_str(master)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:CSPath {param}')

	# noinspection PyTypeChecker
	class MaiqStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RfConnector: No parameter help available
			- Rf_Converter: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	# noinspection PyTypeChecker
	def get_maiq(self) -> MaiqStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ \n
		Snippet: value: MaiqStruct = driver.route.gprf.measurement.scenario.get_maiq() \n
		No command help available \n
			:return: structure: for return value, see the help for MaiqStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ?', self.__class__.MaiqStruct())

	def set_maiq(self, value: MaiqStruct) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ \n
		Snippet: driver.route.gprf.measurement.scenario.set_maiq(value = MaiqStruct()) \n
		No command help available \n
			:param value: see the help for MaiqStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:MEASurement<Instance>:SCENario:MAIQ', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.MeasScenario:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.MeasScenario = driver.route.gprf.measurement.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.MeasScenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
