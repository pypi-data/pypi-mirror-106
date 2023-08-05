from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("generator", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.InstrumentType:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:TYPE \n
		Snippet: value: enums.InstrumentType = driver.configure.gprf.generator.get_type_py() \n
		No command help available \n
			:return: instrument_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:GENerator<Instance>:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.InstrumentType)

	def set_type_py(self, instrument_type: enums.InstrumentType) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:TYPE \n
		Snippet: driver.configure.gprf.generator.set_type_py(instrument_type = enums.InstrumentType.PROTocol) \n
		No command help available \n
			:param instrument_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(instrument_type, enums.InstrumentType)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:TYPE {param}')
