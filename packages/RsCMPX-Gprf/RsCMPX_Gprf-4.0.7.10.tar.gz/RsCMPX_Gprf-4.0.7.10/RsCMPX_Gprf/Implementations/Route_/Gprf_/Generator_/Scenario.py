from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tx_Connector: enums.TxConnector: RF connector for the output path Single R&S CMW500: RFnC for RF n COM RFnO for RF n OUT CMWflexx: RabC for CMW a, connector RF b COM RabO for CMW a, connector RF b OUT
			- Rf_Converter: enums.TxConverter: TX module for the output path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.gprf.generator.scenario.get_salone() \n
		Selects the signal path for the generated signal, for signal output via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM, RF 2 COM, RF 1 OUT are compatible with TX 1 and TX 3.
			- RF 3 COM, RF 4 COM, RF 3 OUT are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: driver.route.gprf.generator.scenario.set_salone(value = SaloneStruct()) \n
		Selects the signal path for the generated signal, for signal output via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM, RF 2 COM, RF 1 OUT are compatible with TX 1 and TX 3.
			- RF 3 COM, RF 4 COM, RF 3 OUT are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:SALone', value)

	# noinspection PyTypeChecker
	class IqOutStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tx_Connector: enums.TxConnector: No parameter help available
			- Tx_Converter: enums.TxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_iq_out(self) -> IqOutStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut \n
		Snippet: value: IqOutStruct = driver.route.gprf.generator.scenario.get_iq_out() \n
		No command help available \n
			:return: structure: for return value, see the help for IqOutStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut?', self.__class__.IqOutStruct())

	def set_iq_out(self, value: IqOutStruct) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut \n
		Snippet: driver.route.gprf.generator.scenario.set_iq_out(value = IqOutStruct()) \n
		No command help available \n
			:param value: see the help for IqOutStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GPRF:GENerator<Instance>:SCENario:IQOut', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.GenScenario:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario \n
		Snippet: value: enums.GenScenario = driver.route.gprf.generator.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:GENerator<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.GenScenario)
