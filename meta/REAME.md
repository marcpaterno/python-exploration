# meta

This is a project that demostrates the use of Python metaclasses.

Our goal is to support the creation of classes which each have an instance variable 
*short_variables* which is a list of the names of the instance variables with names
that are one or two characters long.

Example of use:

    from tracked import Tracked
    class TypeA(Tracked):
      def __init__(self):
        a = 1      # Should be in list
        b = "cow"  # Should be in list
        long = 1.5 # Should not be in list

    a = TypeA()
    assert len(a.short_variables == 2)
    assert a.short_variables == ["a", "b"]
 