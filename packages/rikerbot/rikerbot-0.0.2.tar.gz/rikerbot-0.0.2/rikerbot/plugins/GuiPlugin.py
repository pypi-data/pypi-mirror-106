from rikerbot.PluginBase import CPluginBase, pl_announce
from .CGuiCore import GuiCore

@pl_announce('Gui')
class GuiPlugin(CPluginBase):
  requires = ('Event', 'IO')
  core = GuiCore
