#ifndef DUMMY_UTIL_HH
#define DUMMY_UTIL_HH

namespace dummy {
  class Util {
  public:
    void increment();
    int get_count() const;

  private:
    int count_ = 0;
  };

  void Initialize();
  void Finalize();
  void Increment();
  int GetCount();
}

#endif
