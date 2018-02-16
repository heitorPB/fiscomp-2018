program derivatives
        implicit none

        integer, parameter :: dp = kind(0d0)

        real(dp), parameter :: x0 = 1           ! point to calculate derivative of f
        real(dp) :: df_exact                    ! exact value of derivative
        real(dp) :: e_dff, e_dft, e_d3s, e_dd3s ! deviation from exact value
        real(dp) :: h = 1                       ! initial step size

        print "(A1, A19, 4A20)", "#", "h", "e_dff", "e_dft", "e_d3s", "e_dd3s"
        do while (h > 1.d-8)
                df_exact = df(x0)
                e_dff  = abs(df_exact - dff(x0, h))
                e_dft  = abs(df_exact - dft(x0, h))
                e_d3s  = abs(df_exact - d3s(x0, h))
                e_dd3s = abs(ddf(x0) - dd3s(x0, h))

                print "(5F20.16)", h, e_dff, e_dft, e_d3s, e_dd3s
                h = h / 2
        end do


contains
real(dp) function f(x)
        real(dp), intent(in) :: x

        f = exp(2 * x) * cos(x / 4)
end function f


! exact derivative of f(x)
real(dp) function df(x)
        real(dp), intent(in) :: x

        df = exp(2 * x) * (2 * cos(x / 4) - sin(x / 4) / 4)
end function df


! exact second derivative of f(x)
real(dp) function ddf(x)
        real(dp), intent(in) :: x

        ddf = exp(2 * x) * (63 * cos(x / 4) / 16 - sin(x / 4))
end function ddf


! numeric aproximations for the derivative of f(x):
! derivada para frente de 2 pontos
real(dp) function dff(x, h)
        real(dp), intent(in) :: x
        real(dp), intent(in) :: h

        dff = (f(x + h) - f(x) ) / h
end function dff


! derivada para trás de 2 pontos
real(dp) function dft(x, h)
        real(dp), intent(in) :: x
        real(dp), intent(in) :: h

        dft = (f(x) - f(x - h) ) / h
end function dft


! derivada simétrica de 3 pontos
real(dp) function d3s(x, h)
        real(dp), intent(in) :: x
        real(dp), intent(in) :: h

        d3s = (f(x + h) - f(x - h) ) / (2 * h)
end function d3s


! derivada segunda simétrica de três pontos
real(dp) function dd3s(x, h)
        real(dp), intent(in) :: x
        real(dp), intent(in) :: h

        dd3s = (f(x + h) - 2 * f(x) + f(x - h)) / h**2
end function dd3s
end program derivatives