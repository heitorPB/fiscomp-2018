! calculates cos(x) using a taylor aprox
program cosine
        implicit none
        integer, parameter :: huge_int = selected_int_kind(20)
        integer, parameter :: long = selected_real_kind(16)

        real (kind = long), parameter :: pi = atan2(0d0, -1d0)
        real (kind = long) :: x
        real (kind = long) :: cosx
        real (kind = long) :: prec
        real (kind = long) :: diff

        integer :: n
        integer, parameter :: nmax = 1000

        x = 3 * pi / 8
        cosx = 1.d0
        prec = 1.d-6
        diff = 666
        n = 1

        do while (abs(diff) > prec .AND. n < nmax)
                diff = x**(2d0 * n) / REAL(factorial(2 * n), long)
                cosx = cosx + (-1)**n * diff

                n = n + 1
        end do

        print "(A5, A35, A30, A45)", "!x", "~cos(x)", "cos(x)", "relative difference"
        print *,  x, cosx, cos(x), abs(cosx - cos(x)) / cos(x)

contains
integer(kind = huge_int) function factorial(n)
        implicit none
        integer, parameter :: huge_int = selected_int_kind(20)

        integer, intent(in) :: n
        integer :: i

        factorial = n

        do i = n - 1, 1, -1
                factorial = factorial * int(i, huge_int)
        end do

        !print *, n, "! = ", factorial
end function factorial
end program cosine