from __future__ import annotations
from typing import TYPE_CHECKING, List

from panels.toolkits_panel import ToolkitsPanel
from panels.editor_panel import EditorPanel
from panels.level_selector_panel import LevelSelectorPanel

if TYPE_CHECKING:
	from component import Component

class PanelDirector:
	def __init__(self, loaded_components: List[Component]) -> None:
		self._loaded_components = loaded_components
		self._level_selector_panel: LevelSelectorPanel = LevelSelectorPanel(panel_director=self)
		self._toolkits_panel: ToolkitsPanel = ToolkitsPanel(panel_director=self, components_list=loaded_components)
		self._editor_panel: EditorPanel = EditorPanel(panel_director=self)

	@property
	def level_selector_panel(self) -> LevelSelectorPanel:
		return self._level_selector_panel

	@property
	def toolkits_panel(self) -> ToolkitsPanel:
		return self._toolkits_panel

	@property
	def editor_panel(self) -> EditorPanel:
		return self._editor_panel
