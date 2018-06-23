program decaimento
        use iso_c_binding
        implicit none

        real(kind = c_double) :: dt
        real(kind = c_double) :: t
        real(kind = c_double) :: tau
        real(kind = c_double) :: tmax
        real(kind = c_double) :: random

        integer :: i
        integer :: N
        integer :: N0

        call random_seed()

        write(*, *) "# entre com N0, tau, dt, tmax"
        read(*, *) N0, tau, dt, tmax

        N = N0
        t = 0
        write(*, *) t, N

        do while (t < tmax .and. N > 0)
                do i = 1, N
                        call random_number(random)
                        if (random < dt / tau) then
                                N = N - 1
                        end if
                end do

                t = t + dt
                write(*, *) t, N
        end do
end program decaimento