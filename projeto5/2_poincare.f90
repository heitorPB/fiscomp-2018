program caos
        use iso_c_binding
        implicit none

        real(c_double) :: r
        real(c_double) :: x0
        real(c_double) :: x1, x2

        integer :: i, j

        read(*, *) r
        read(*, *) x0

        x1 = g(r, x0)
        x2 = g(r, x1)
        write(*, *) x0, x1, x2
        do i = 1, 1000
                x0 = x1
                x1 = x2
                x2 = g(r, x2)
                write(*, *) x0, x1, x2
        end do


contains
real(c_double) function g(r, x)
        implicit none

        real(c_double), intent(in) :: r
        real(c_double), intent(in) :: x

        g = r * x * (1 - x)
end function g
end program caos