from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("correctionTable", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .CorrectionTable_.All import All
			self._all = All(self._core, self._base)
		return self._all

	def delete(self, name: str) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle \n
		Snippet: driver.system.attenuation.correctionTable.delete(name = '1') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'DELete:SYSTem:ATTenuation:CTABle {param}')

	def clone(self) -> 'CorrectionTable':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionTable(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
