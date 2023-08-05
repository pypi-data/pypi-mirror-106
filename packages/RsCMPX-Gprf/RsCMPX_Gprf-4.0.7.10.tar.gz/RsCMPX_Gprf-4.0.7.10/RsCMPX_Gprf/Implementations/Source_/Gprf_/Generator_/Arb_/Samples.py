from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Samples:
	"""Samples commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("samples", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Range_Py: enums.Range: FULL: The full ARB file is processed. SUB: The subrange defined by the Start and Stop parameters is processed.
			- Start: int: The beginning (first sample) of the subrange.
			- Stop: int: The end (last sample) of the subrange."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Range_Py', enums.Range),
			ArgStruct.scalar_int('Start'),
			ArgStruct.scalar_int('Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Range_Py: enums.Range = None
			self.Start: int = None
			self.Stop: int = None

	# noinspection PyTypeChecker
	def get_range(self) -> RangeStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe \n
		Snippet: value: RangeStruct = driver.source.gprf.generator.arb.samples.get_range() \n
		Defines the range of samples in the loaded ARB file that are processed. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe?', self.__class__.RangeStruct())

	def set_range(self, value: RangeStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe \n
		Snippet: driver.source.gprf.generator.arb.samples.set_range(value = RangeStruct()) \n
		Defines the range of samples in the loaded ARB file that are processed. \n
			:param value: see the help for RangeStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:ARB:SAMPles:RANGe', value)

	def get_value(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:SAMPles \n
		Snippet: value: float = driver.source.gprf.generator.arb.samples.get_value() \n
		Queries the number of samples in the loaded waveform file. The R&S CMX500 supports waveform files with a size up to 512
		MB. \n
			:return: samples: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:SAMPles?')
		return Conversions.str_to_float(response)
