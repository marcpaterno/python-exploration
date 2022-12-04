.PHONY: all clean format

CXXFLAGS+=-std=c++17 -O0 -g -Wall -Wextra
CPPFLAGS+=-I ${CONDA_PREFIX}/include -I ${CONDA_PREFIX}/include/python3.11
LDFLAGS+=-L${CONDA_PREFIX}/lib -undefined dynamic_lookup

all: dummy_util.cpython-311-darwin.so

clean:
	rm -f *.so *.o
	rm -rf dummy_util.cpython-311-darwin.so.dSYM/

dummy_util.cpython-311-darwin.so: dummy_util.cc
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(LDFLAGS) -shared -o $@ $<

format:
	clang-format -i -style=file *.cc *.hh
