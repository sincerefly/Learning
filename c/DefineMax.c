#include <stdio.h>
#define MAX(a, b) ((a)>(b)?(a):(b))

int main(void) {
  printf("%d\n", MAX(5, 6));
  return 0;
}
