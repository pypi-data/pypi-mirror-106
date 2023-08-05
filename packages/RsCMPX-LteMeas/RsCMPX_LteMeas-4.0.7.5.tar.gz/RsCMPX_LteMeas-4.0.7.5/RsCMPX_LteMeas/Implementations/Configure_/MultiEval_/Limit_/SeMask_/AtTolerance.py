from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AtTolerance:
	"""AtTolerance commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: EutraBand, default value after init: EutraBand.Nr30"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("atTolerance", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_eutraBand_get', 'repcap_eutraBand_set', repcap.EutraBand.Nr30)

	def repcap_eutraBand_set(self, enum_value: repcap.EutraBand) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EutraBand.Default
		Default value after init: EutraBand.Nr30"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_eutraBand_get(self) -> repcap.EutraBand:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, add_test_tol: float, eutraBand=repcap.EutraBand.Default) -> None:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance<EUTRAband> \n
		Snippet: driver.configure.multiEval.limit.seMask.atTolerance.set(add_test_tol = 1.0, eutraBand = repcap.EutraBand.Default) \n
		Defines additional test tolerances for the emission masks. The tolerance is added to the power values of all general and
		additional spectrum emission masks. A positive tolerance value relaxes the limits. For operating bands below 3 GHz, there
		is no additional test tolerance. You can define different additional test tolerances for bands above 3 GHz and for bands
		above 5 GHz. \n
			:param add_test_tol: Additional test tolerance
			:param eutraBand: optional repeated capability selector. Default value: Nr30 (settable in the interface 'AtTolerance')"""
		param = Conversions.decimal_value_to_str(add_test_tol)
		eutraBand_cmd_val = self._base.get_repcap_cmd_value(eutraBand, repcap.EutraBand)
		self._core.io.write(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance{eutraBand_cmd_val} {param}')

	def get(self, eutraBand=repcap.EutraBand.Default) -> float:
		"""SCPI: CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance<EUTRAband> \n
		Snippet: value: float = driver.configure.multiEval.limit.seMask.atTolerance.get(eutraBand = repcap.EutraBand.Default) \n
		Defines additional test tolerances for the emission masks. The tolerance is added to the power values of all general and
		additional spectrum emission masks. A positive tolerance value relaxes the limits. For operating bands below 3 GHz, there
		is no additional test tolerance. You can define different additional test tolerances for bands above 3 GHz and for bands
		above 5 GHz. \n
			:param eutraBand: optional repeated capability selector. Default value: Nr30 (settable in the interface 'AtTolerance')
			:return: add_test_tol: Additional test tolerance"""
		eutraBand_cmd_val = self._base.get_repcap_cmd_value(eutraBand, repcap.EutraBand)
		response = self._core.io.query_str(f'CONFigure:LTE:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance{eutraBand_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AtTolerance':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AtTolerance(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
