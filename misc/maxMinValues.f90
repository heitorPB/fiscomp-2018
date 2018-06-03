program integerkinds
        use iso_c_binding
        implicit none

        integer                     :: i
        integer(kind = c_short)     :: short_int
        integer(kind = c_int)       :: normal_int
        integer(kind = c_long)      :: long_int
        integer(kind = c_long_long) :: long_long_int
        integer(kind = c_int8_t)    :: int8
        integer(kind = c_int16_t)   :: int16
        integer(kind = c_int32_t)   :: int32
        integer(kind = c_int64_t)   :: int64
        integer(kind = c_int128_t)  :: int128

        real                       :: r
        real(kind = c_float)       :: f
        real(kind = c_double)      :: d
        real(kind = c_long_double) :: ld
        real(kind = c_float128)    :: qd

        print *, "Maximum integers:"
        print *, 'Default:        ', huge(i)
        print *, 'c_short_int:    ', huge(short_int)
        print *, 'c_normal_int:   ', huge(normal_int)
        print *, 'c_long_int:     ', huge(long_int)
        print *, 'c_long_long_int:', huge(long_long_int)
        print *, 'c_int8:         ', huge(int8)
        print *, 'c_int16:        ', huge(int16)
        print *, 'c_int32:        ', huge(int32)
        print *, 'c_int64:        ', huge(int64)
        print *, 'c_int128:        ', huge(int128)

        print *,''
        print *, "Maximum floats:"

        print *, "Default:      ", huge(r)
        print *, "c_float:      ", huge(f)
        print *, "c_double:     ", huge(d)
        print *, "c_long_double:", huge(ld)
        print *, "c_float128:   ", huge(qd)

        print *, ""
        print *, "Minimum floats:"

        print *, "Default:      ", tiny(r)
        print *, "c_float:      ", tiny(f)
        print *, "c_double:     ", tiny(d)
        print *, "c_long_double:", tiny(ld)
        print *, "c_float128:   ", tiny(qd)

        print *, ""
        print *, "Smallest distance between floats:"

        print *, "Default:      ", spacing(r)
        print *, "c_float:      ", spacing(f)
        print *, "c_double:     ", spacing(d)
        print *, "c_long_double:", spacing(ld)
        print *, "c_float128:   ", spacing(qd)
end program integerkinds
