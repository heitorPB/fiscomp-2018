program integrals
        implicit none

        integer, parameter :: dp = kind(0d0)

        real(dp), parameter :: a = 0, b = 1     ! integration interval

        real(dp) :: exact
        real(dp) :: diff_trap
        real(dp) :: diff_simp

        integer :: N
        integer :: i

        exact = integral(a, b)

        print "(A1, A19, 2A20)", "#", "h", "e_trapezoid", "e_simpson"
        do i = 1, 28
                N = 2**i

                diff_trap = abs(trap(a, b, N) - exact)
                diff_simp = abs(simp(a, b, N) - exact)

                print "(3F20.16)", (b - a)/N, diff_trap, diff_simp
        end do


        contains
real(dp) function f(x)
        real(dp), intent(in) :: x

        f = exp(2 * x) * sin(x)
end function f


! exact value of integral from a to b
real(dp) function integral(a, b)
        real(dp), intent(in) :: a
        real(dp), intent(in) :: b

        integral = (exp(2*a)*(cos(a) - 2*sin(a)) - exp(2*b)*(cos(b) - 2*sin(b))) / 5
end function integral


! numeric approximations of the integral
! trapezoid rule
real(dp) function trap(a, b, N)
        real(dp), intent(in) :: a
        real(dp), intent(in) :: b
        integer,  intent(in) :: N

        integer :: i
        real(dp) :: h
        h = (b - a) / N

        trap = (f(a) + f(b)) / 2
        do i = 1, N - 1
                trap = trap + f(a + i * h)
        end do
        trap = trap * h
end function trap


! simpson rule
real(dp) function simp(a, b, N)
        real(dp), intent(in) :: a
        real(dp), intent(in) :: b
        integer,  intent(in) :: N

        integer :: i
        real(dp) :: h
        h = 1._dp / N

        simp = f(a) + f(b)
        do i = 1, N - 1
                simp = simp + (3 - (-1)**i) * f(a + i * h)
        end do
        simp = simp * h / 3
end function simp
end program integrals