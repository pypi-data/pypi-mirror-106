#include "gui_core.hpp"

namespace rkr {

RkrFrame::RkrFrame() : wxFrame(nullptr, wxID_ANY, "Rikerbot") {
  wxPanel* panel = new wxPanel(this, wxID_ANY);
  auto sizer = new wxBoxSizer(wxHORIZONTAL);
  panel->SetSizer(sizer);
  sizer->Add(new wxTextCtrl(panel, ID_X), wxEXPAND | wxALL, 5);
  sizer->Add(new wxTextCtrl(panel, ID_Y), wxEXPAND | wxALL, 5);
  sizer->Add(new wxTextCtrl(panel, ID_Z), wxEXPAND | wxALL, 5);
}

RkrGuiApp::RkrGuiApp(GuiCore* guicore) : guicore(guicore) {}

int RkrGuiApp::OnExit() {
  // This is almost definitely unsafe on some platform because of memory
  // reordering, but we're closing the application anyway so who cares
  guicore->app_dead = true;
  guicore->exec->stop();
  return 0;
}

bool RkrGuiApp::OnInit() {
  (new RkrFrame())->Show(true);
  return true;
}

GuiCore::GuiCore(rkr::PluginLoader& ploader, bool ownership) :
    PluginBase("rkr::GuiCore *") {

  ploader.provide("Gui", this, ownership);
  EventCore* ev = static_cast<EventCore*>(ploader.require("Event"));

  exec = static_cast<ExecCore*>(ploader.require("Exec"));

  ev->register_callback("kill",
      [&](ev_id_type, const void*) {kill_handler();});

  start_gui();

}

void GuiCore::start_gui(int argc, char **argv) {
  std::thread(GuiCore::run_gui, this, argc, argv).detach();
}

void GuiCore::run_gui(GuiCore* guicore, int argc, char **argv) {
  wxApp::SetInstance(new RkrGuiApp(guicore));
  wxEntry(argc, argv);
}

void GuiCore::kill_handler() {
  if(!app_dead)
    wxTheApp->CallAfter([]{wxTheApp->GetTopWindow()->Close();});
}

}
