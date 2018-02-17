program bissecao
        implicit none
        integer, parameter :: dp = kind(0.d0)

        integer, parameter  :: N = 1024
        real(dp), parameter :: tol = 1.d-8      ! desired precision

        integer :: i
        real(dp) :: T
        real(dp) :: x1, x2, x3

        print "(A2, A19, A20)", "#", "T", "x+"
        do i = 0, N
                T = i / real(N, dp)
                x1 = 1.d-4 ! f(x1) < 0
                x2 = 1     ! f(x2) > 0

                do while (abs(x1 - x2) / 2 > tol)
                        x3 = (x1 + x2) / 2
                        if (f(x3, T) > 0) then
                                x2 = x3
                        else
                                x1 = x3
                        end if
                end do


                print "(2F20.16)", T, x1
        end do


contains
real(dp) function f(m, T)
        real(dp), intent(in) :: m
        real(dp), intent(in) :: T

        f = m - tanh(m / T)
end function f
end program bissecao