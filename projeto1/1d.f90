program ordena
        implicit none

        integer :: N, M, i
        real, allocatable, dimension(:) :: lista

        print *, "Enter N"
        read *, N
        print *, "Enter M"
        read *, M

        if (N < 1) then
                print *, "Stupid value of N detected"
                stop "Bye"
        end if

        if (M > N .or. M < 0) then
                print *, "Stupid value of M detected"
                print *, "Setting M = N"
                M = N
        end if

        allocate(lista(N))
        read *, (lista(i), i = 1, N)

        call InsertionSort(lista, N, M)
        print *, (lista(i), i = 1, M)

        deallocate(lista)


contains
subroutine InsertionSort(list, N, M)
! https://en.wikipedia.org/wiki/Insertion_sort
! https://github.com/frigaut/yorick-imutil/blob/master/insort.c
        integer, intent(in) :: N, M
        real, intent(inout) :: list(N)

        integer :: i, j
        real :: temp

        do i = 1, M
                j = i
                temp = list(j)
                do while ( j > 1 .AND. list(j - 1) > temp)
                        list(j) = list(j - 1)
                        j = j - 1
                end do
                list(j) = temp
        end do
end subroutine InsertionSort
end program ordena