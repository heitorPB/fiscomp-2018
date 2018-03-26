program pendulo
        implicit none
        integer, parameter :: dp = kind(0.d0)
        real(dp), parameter :: pi = acos(-1._dp)

        real(dp) :: theta
        real(dp) :: m
        real(dp) :: L
        real(dp) :: g
        real(dp) :: dt, tmax, t

        real(dp) :: theta_i
        real(dp) :: w, w_i

        real(dp) :: E_k, E_g

        ! for Euler-Cromer method:
        real(dp) :: E_ck, E_cg
        real(dp) :: thetac, thetac_i
        real(dp) :: wc, wc_i

        write(*, *) "# Enter theta_0 (degrees), m (kg), L (m), g (m/s^2), dt (s), tmax (s)"
        read(*, *) theta, m, L, g, dt, tmax

        theta = theta * pi / 180._dp

        t    = 0
        w    = 0
        w_i  = 0
        wc   = 0
        wc_i = 0
        theta_i  = theta
        thetac_i = theta
        thetac   = theta
        write(*, *) "# t (s), theta (rad), E_k (J), E_g (J), thetac, Ec_k, Ec_g"
        do while (t <= tmax)
                w = w_i - g * sin(theta) * dt / L
                theta = theta_i + w_i * dt

                E_k = m * L**2 * w**2 / 2
                E_g = m * g * L * (1 - cos(theta))

                ! euler-cromer
                wc = wc_i - g * sin(thetac) * dt / L
                thetac = thetac_i + wc * dt

                E_ck = m * L**2 * wc**2 / 2
                E_cg = m * g * L * (1 - cos(thetac))

                write(*, *) t, theta, E_k, E_g, thetac, E_ck, E_cg

                theta_i = theta
                w_i = w
                thetac_i = thetac
                wc_i = wc
                t = t + dt
        end do

end program pendulo