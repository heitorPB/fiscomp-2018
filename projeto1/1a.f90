program factorial
        implicit none

        integer, parameter :: huge_int = selected_int_kind(20)
        integer (kind = huge_int) :: n, fact

        integer, parameter :: double_precision = selected_real_kind(20)
        real (kind = double_precision) :: stirling, logfact
        real (kind = double_precision), parameter :: pi = atan2(0._double_precision, -1._double_precision)

        print *, "huge_int kind = ", huge_int
        print *, "double_precision kind = ", double_precision

        open(unit = 11, file = "facts.txt", status = "replace")
        write(11, "(A2, A35, A13, A13, A29)") "#n", "n!", "ln(n!)", "ln*(n!)", "[ln(n!) - ln*(n!)] / ln(n!)"

        fact = 1
        do n = 2, 30
                ! factorial of n
                fact = fact * n

                ! ln(n!)
                logfact = log(fact * 1d0)

                ! stirling aproximation of factorial of n
                stirling = n * log(n * 1d0) - n * 1.d0 + log(2 * pi * n) / 2d0

                write(11, "(I2, I35, F13.8, F13.8, F12.8)") n, fact, logfact, stirling, (logfact - stirling) / logfact
        end do

        close(unit = 11)

end program factorial