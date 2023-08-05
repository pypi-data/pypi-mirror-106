%module CGuiCore
%{
#include "gui_core.hpp"
%}

%feature ("flatnested");

%include <stdint.i>
%include <std_string.i>

%include "plugin_base.hpp"
%include "gui_core.hpp"
