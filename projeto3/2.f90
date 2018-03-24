program projetil
        implicit none
        integer, parameter :: dp = kind(0.d0)

        real(dp), parameter :: g  = 9.8_dp       ! m/s^2
        real(dp), parameter :: pi = acos(-1._dp)

        ! input parameters:
        real(dp) :: v0          ! m/s
        real(dp) :: theta       ! degrees
        real(dp) :: gamma2      ! gamma/m actually
        real(dp) :: alpha       ! 
        real(dp) :: a           ! K / m
        real(dp) :: T0          ! K
        real(dp) :: dt          ! s

        real(dp) :: x0, x, y0, y
        real(dp) :: vx0, vy0, vx, vy, v
        real(dp) :: friction

        write(*, *) "# enter: v0, theta, gamma2, a, alpha, T0, dt"
        read(*, *) v0, theta, gamma2, a, alpha, T0, dt

        theta = theta * pi / 180
        x0 = 0
        y0 = 0
        x  = 0
        y  = 0
        vx0 = v0 * cos(theta)
        vy0 = v0 * sin(theta)

        write(*, *) "# x (m)   y (m)"
        write(*, *) x, y
        do while(y >= 0)
                x  = x0 + vx0 * dt
                y  = y0 + vy0 * dt
                v = sqrt(vx0**2 + vy0**2)
                friction = gamma2 * (1._dp - a * y0 / T0)**alpha * v
                vx = vx0 - friction * vx0 * dt
                vy = vy0 - friction * vy0 * dt - g * dt

                x0  = x
                y0  = y
                vx0 = vx
                vy0 = vy

                write(*, *) x, y
        end do

end program projetil