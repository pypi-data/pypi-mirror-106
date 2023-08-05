#ifndef RKR_GUI_CORE_HPP
#define RKR_GUI_CORE_HPP

#include <wx/wxprec.h>
#ifndef WX_PRECOMP
#include <wx/wx.h>
#endif

#include <memory>
#include <thread>

#include "event_core.hpp"
#include "exec_core.hpp"
#include "plugin_base.hpp"
#include "plugin_loader.hpp"

namespace rkr {

enum { ID_X, ID_Y, ID_Z };

class GuiCore;

class RkrFrame : public wxFrame {
public:
  RkrFrame();

private:
};

class RkrGuiApp : public wxApp {
public:
  RkrGuiApp(GuiCore* guicore);

private:
  bool OnInit();
  int OnExit();
  GuiCore* guicore;
};

class GuiCore : public PluginBase {
  friend class RkrGuiApp;

public:
  GuiCore(rkr::PluginLoader& ploader, bool ownership = false);

  void start_gui(int argc = 0, char** argv = nullptr);

private:
  static void run_gui(GuiCore* guicore, int argc, char** argv);
  ExecCore* exec;
  bool app_dead {false};
  void kill_handler();
};

} // namespace rkr

#endif // RKR_GUI_CORE_HPP
