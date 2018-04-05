program bike
        implicit none
        integer, parameter :: dp = kind(0.d0)

        real(dp), parameter :: P = 400  ! Watts
        real(dp), parameter :: m = 70   ! kg
        real(dp), parameter :: A = 1./3 ! m2

        real(dp) :: rho         ! kg / m3
        real(dp) :: dt          ! s
        real(dp) :: tmax        ! s
        real(dp) :: v0          ! m / s

        real(dp) :: v, vi, t

        write(*, *) "# Enter v0, rho, tmax, dt"
        read(*, *) v0, rho, tmax, dt

        write(*, *) "# t (s)           v (m/s)"
        t = 0
        vi = v0
        write(*, *) t, v0
        do while (t <= tmax)
                v = vi + P * dt / (m * vi) - rho * A * vi**2 * dt / (2 * m)
                t = t + dt
                write(*, *) t, v
                vi = v
        end do
end program bike