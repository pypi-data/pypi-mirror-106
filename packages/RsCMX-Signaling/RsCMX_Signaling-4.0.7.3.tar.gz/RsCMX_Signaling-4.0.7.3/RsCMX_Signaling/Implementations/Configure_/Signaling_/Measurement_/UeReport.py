from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeReport:
	"""UeReport commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ueReport", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .UeReport_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	# noinspection PyTypeChecker
	def get_enable(self) -> enums.CellsToMeasure:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:ENABle \n
		Snippet: value: enums.CellsToMeasure = driver.configure.signaling.measurement.ueReport.get_enable() \n
		Selects whether the UE must send measurement reports and for which cells. \n
			:return: cells_to_measure: OFF: no measurement reports ALL: reporting for all cells LTE: reporting for LTE cells only NRADio: reporting for NR cells only
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:ENABle?')
		return Conversions.str_to_scalar_enum(response, enums.CellsToMeasure)

	def set_enable(self, cells_to_measure: enums.CellsToMeasure) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:ENABle \n
		Snippet: driver.configure.signaling.measurement.ueReport.set_enable(cells_to_measure = enums.CellsToMeasure.ALL) \n
		Selects whether the UE must send measurement reports and for which cells. \n
			:param cells_to_measure: OFF: no measurement reports ALL: reporting for all cells LTE: reporting for LTE cells only NRADio: reporting for NR cells only
		"""
		param = Conversions.enum_scalar_to_str(cells_to_measure, enums.CellsToMeasure)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:ENABle {param}')

	# noinspection PyTypeChecker
	def get_rinterval(self) -> enums.ReportInterval:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RINTerval \n
		Snippet: value: enums.ReportInterval = driver.configure.signaling.measurement.ueReport.get_rinterval() \n
		Configures the interval between two consecutive measurement reports (120 ms to 30 minutes) . \n
			:return: report_interval: I1: 120 ms, I2: 240 ms, I3: 480 ms, I4: 640 ms I5: 1024 ms, I6: 2048 ms, I7: 5120 ms, I8: 10240 ms I9: 20480 ms, I10: 40960 ms, I11: 1 min, I12: 6 min I13: 12 min, I14: 30 min
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:UEReport:RINTerval?')
		return Conversions.str_to_scalar_enum(response, enums.ReportInterval)

	def set_rinterval(self, report_interval: enums.ReportInterval) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:UEReport:RINTerval \n
		Snippet: driver.configure.signaling.measurement.ueReport.set_rinterval(report_interval = enums.ReportInterval.I1) \n
		Configures the interval between two consecutive measurement reports (120 ms to 30 minutes) . \n
			:param report_interval: I1: 120 ms, I2: 240 ms, I3: 480 ms, I4: 640 ms I5: 1024 ms, I6: 2048 ms, I7: 5120 ms, I8: 10240 ms I9: 20480 ms, I10: 40960 ms, I11: 1 min, I12: 6 min I13: 12 min, I14: 30 min
		"""
		param = Conversions.enum_scalar_to_str(report_interval, enums.ReportInterval)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:UEReport:RINTerval {param}')

	def clone(self) -> 'UeReport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeReport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
