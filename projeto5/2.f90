program caos
        use iso_c_binding
        implicit none

        real(c_double) :: r
        real(c_double) :: x0
        real(c_double) :: x1

        integer :: i, j

        read(*, *) x0

        do j = -2101, 4001
                r = real(j, c_double) / 1d3

                x1 = x0
                do i = 1, 137
                        x1 = g(r, x1)
                end do
                do i = 1, 666 + 137 + 42
                        x1 = g(r, x1)
                        write(*, *) x1, r
                end do
        end do


contains
real(c_double) function g(r, x)
        implicit none

        real(c_double), intent(in) :: r
        real(c_double), intent(in) :: x

        g = r * x * (1 - x)
end function g
end program caos