#include "dummy_util.hh"
#include <assert.h>
#include "pybind11/pybind11.h"

void
dummy::Util::increment()
{
  count_ += 1;
}

int
dummy::Util::get_count() const
{
  return count_;
}

namespace {
  static dummy::Util* THE_THING = nullptr;
};

void
dummy::Initialize()
{
  assert(THE_THING == nullptr);
  THE_THING = new Util();
  assert(THE_THING != nullptr);
}

void
dummy::Finalize()
{
  assert(THE_THING != nullptr);
  delete THE_THING;
  THE_THING = nullptr;
}

PYBIND11_MODULE(dummy_util, m)
{
  m.doc() = R"pbdoc(demo of lifetime management)pbdoc";
  m.def(
    "initialize", &dummy::Initialize, R"pbdoc(initialize the library)pbdoc");
  m.def("finalize", &dummy::Finalize, R"pbdoc(finalize the library)pbdoc");
}
