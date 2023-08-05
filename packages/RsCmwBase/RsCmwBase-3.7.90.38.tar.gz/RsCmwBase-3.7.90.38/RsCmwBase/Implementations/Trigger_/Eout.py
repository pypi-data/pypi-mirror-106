from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eout:
	"""Eout commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: Eout, default value after init: Eout.Eout1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eout", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_eout_get', 'repcap_eout_set', repcap.Eout.Eout1)

	def repcap_eout_set(self, enum_value: repcap.Eout) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Eout.Default
		Default value after init: Eout.Eout1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_eout_get(self) -> repcap.Eout:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Eout_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Eout_.Source import Source
			self._source = Source(self._core, self._base)
		return self._source

	def clone(self) -> 'Eout':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eout(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
