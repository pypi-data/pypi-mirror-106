from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("delay", core, parent)

	def set(self, waveform_marker: float, marker=repcap.Marker.Default) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker<no>:DELay \n
		Snippet: driver.source.gprf.generator.sequencer.wmarker.delay.set(waveform_marker = 1.0, marker = repcap.Marker.Default) \n
		Defines a delay time for the ARB output trigger events relative to the waveform marker <no> events. \n
			:param waveform_marker: No help available
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Wmarker')"""
		param = Conversions.decimal_value_to_str(waveform_marker)
		marker_cmd_val = self._base.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker{marker_cmd_val}:DELay {param}')

	def get(self, marker=repcap.Marker.Default) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker<no>:DELay \n
		Snippet: value: float = driver.source.gprf.generator.sequencer.wmarker.delay.get(marker = repcap.Marker.Default) \n
		Defines a delay time for the ARB output trigger events relative to the waveform marker <no> events. \n
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Wmarker')
			:return: waveform_marker: No help available"""
		marker_cmd_val = self._base.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker{marker_cmd_val}:DELay?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Marker_1: float: No parameter help available
			- Marker_2: float: No parameter help available
			- Marker_3: float: No parameter help available
			- Marker_4: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Marker_1'),
			ArgStruct.scalar_float('Marker_2'),
			ArgStruct.scalar_float('Marker_3'),
			ArgStruct.scalar_float('Marker_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Marker_1: float = None
			self.Marker_2: float = None
			self.Marker_3: float = None
			self.Marker_4: float = None

	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker:DELay:ALL \n
		Snippet: value: AllStruct = driver.source.gprf.generator.sequencer.wmarker.delay.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker:DELay:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker:DELay:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.wmarker.delay.set_all(value = AllStruct()) \n
		No command help available \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce:GPRF:GENerator<Instance>:SEQuencer:WMARker:DELay:ALL', value)
