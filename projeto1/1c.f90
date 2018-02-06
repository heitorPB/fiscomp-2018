program stat
        implicit none
        integer, parameter :: long = selected_real_kind(16)

        integer :: N ! number of numbers to read
        integer :: i

        real (kind = long), allocatable :: x(:), x2(:)
        real (kind = long) :: avg, avg_2, std_deviation

        read *, N
        allocate(x(N), x2(N))

        read *, (x(i), i = 1, N)

        avg = sum(x) / N        ! <x>
        x2 = x * x
        avg_2 = sum(x2) / N     ! <x^2>
        std_deviation = sqrt(avg_2 - avg**2)

        !print *, x
        !print *, x2
        print *, "<x> = ", avg
        print *, "<x^2> = ", avg_2
        print *, "\sigma_x = ", std_deviation

        deallocate(x, x2)
end program stat
