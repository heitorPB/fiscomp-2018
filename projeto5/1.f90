program fixedPoint
        use iso_c_binding
        implicit none

        real(c_double) :: x0, xi
        real(c_double) :: r
        real(c_double) :: eps
        real(c_double) :: d
        integer :: i

        read(*, *) r
        read(*, *) x0
        read(*, *) eps

        xi = x0 + eps
        d = abs(xi - x0)

        i = 0
        write(*, *) x0, i, d
        do i = 1, 50
                x0 = g(r, x0)
                xi = g(r, xi)
                d = abs(xi - x0)
                write(*, *) x0, i, d
        end do

contains
real(c_double) function g(r, x)
        implicit none

        real(c_double), intent(in) :: x
        real(c_double), intent(in) :: r

        g = r * x * (1 - x)
end function g
end program fixedPoint