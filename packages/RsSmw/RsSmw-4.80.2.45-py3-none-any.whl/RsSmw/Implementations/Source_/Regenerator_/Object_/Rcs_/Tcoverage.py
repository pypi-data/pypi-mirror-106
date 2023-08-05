from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcoverage:
	"""Tcoverage commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcoverage", core, parent)

	def set(self, test_coverage: float, objectIx=repcap.ObjectIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:TCOVerage \n
		Snippet: driver.source.regenerator.object.rcs.tcoverage.set(test_coverage = 1.0, objectIx = repcap.ObjectIx.Default) \n
		No command help available \n
			:param test_coverage: No help available
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')"""
		param = Conversions.decimal_value_to_str(test_coverage)
		objectIx_cmd_val = self._base.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:TCOVerage {param}')

	def get(self, objectIx=repcap.ObjectIx.Default) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect<CH>:RCS:TCOVerage \n
		Snippet: value: float = driver.source.regenerator.object.rcs.tcoverage.get(objectIx = repcap.ObjectIx.Default) \n
		No command help available \n
			:param objectIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Object')
			:return: test_coverage: No help available"""
		objectIx_cmd_val = self._base.get_repcap_cmd_value(objectIx, repcap.ObjectIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:OBJect{objectIx_cmd_val}:RCS:TCOVerage?')
		return Conversions.str_to_float(response)
