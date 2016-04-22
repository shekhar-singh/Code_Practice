#include <stdio.h>

int main(void) {
    int arr[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int totalDaysInThisYear = -1, m;  /* Parity would make totalDaysInThisYear = 0 */
    for(m = 1; m <= 12; ++m) {
        const int parity = (m < 3);
        printf("%d\n", (totalDaysInThisYear + parity) % 7);
        totalDaysInThisYear+= arr[m - 1];
    }
    return 0;
}
