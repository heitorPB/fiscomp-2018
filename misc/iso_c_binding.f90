program test
        use iso_c_binding ! modules before implicit none
        implicit none
        character(*), parameter :: f1 = "(A, I3)"
        character(*), parameter :: f2 = "(A, I2)"
        character(*), parameter :: f3 = "(A, I3, F33.30)"

        ! kind parameters to use C convention
        ! for real types
        real(kind = c_float)       :: f  = 1
        real(kind = c_double)      :: d  = 1
        real(kind = c_long_double) :: ld = 1
        real(kind = c_float128)    :: qd = 1 ! NOT fortran standard!
        ! for integer types
        integer(kind = c_short)     :: short_int  = 1
        integer(kind = c_int)       :: normal_int = 1
        integer(kind = c_long)      :: long_int   = 1
        integer(kind = c_long_long) :: long_long_int = 1
        integer(kind = c_int8_t)    :: int8   = 1
        integer(kind = c_int16_t)   :: int16  = 1
        integer(kind = c_int32_t)   :: int32  = 1
        integer(kind = c_int64_t)   :: int64  = 1
        integer(kind = c_int128_t)  :: int128 = 1 ! NOT fortran standard!

        print *, "Real kinds:"
        print f1, "kind(c_float):      ", c_float
        print f1, "kind(c_double):     ", c_double
        print f1, "kind(c_long_double):", c_long_double
        print f1, "kind(c_float128):   ", c_float128

        print *, ""
        print *, "Integer kinds:"
        print f2, "kind(c_short):    ", c_short
        print f2, "kind(c_int):      ", c_int
        print f2, "kind(c_long):     ", c_long
        print f2, "kind(c_long_long):", c_long_long
        print f2, "kind(c_int8_t):   ", c_int8_t
        print f2, "kind(c_int16_t):  ", c_int16_t
        print f2, "kind(c_int32_t):  ", c_int32_t
        print f2, "kind(c_int64_t):  ", c_int64_t
        print f2, "kind(c_int128_t): ", c_int128_t

        print *, ""
        print *, "{f, d, ld, qd} = 1"
        print *, ""

        print f3, "kind(f + d):     ", kind(f + d),      f + d
        print f3, "kind(f + qd):    ", kind(f + qd),     f + qd
        print f3, "kind(f + 5):     ", kind(f + 5),      f + 5
        print f3, "kind(d * 5):     ", kind(d * 5),      d * 5
        print f3, "kind(5 / 9 * d): ", kind(5 / 9 * d),  5 / 9 * d
        print f3, "kind(qd * 5 / 9):", kind(qd * 5 / 9), qd * 5 / 9
        print f3, "kind(d + 5 / 9): ", kind(d + 5 / 9),  d + 5 / 9

        ! useless stuff to get rid of  [some] warnings
        f  = 1
        d  = 1
        ld = 1
        qd = 1
        short_int  = 1
        normal_int = 1
        long_int   = 1
        long_long_int = 1
        int8   = 1
        int16  = 1
        int32  = 1
        int64  = 1
        int128 = 1 ! NOT fortran standard!

end program test