#include <stdio.h>

void BubbleSort(int a[], int n) {
  int i, j, temp;
  int num = 0;
  for(i=0; i<n-1; i++)
  {
    for(j=0; j<n-1-i; j++)
    {
      num++;
      if(a[j] > a[j+1])
      {
        temp = a[j];
        a[j] = a[j+1];
        a[j+1] = temp;
      }
    }
  }
  printf("1, compare counts = %d\n", num);
}

void BubbleSort2(int array[], int len) {
  int exchange = len - 1;
  int num = 0;
  int i = 0;

  while(exchange) {
    int bound = exchange;
    exchange = 0;

    for(i=0; i<bound; i++) {
      num++;
      if (array[i] > array[i+1]) {
        int temp = array[i];
        array[i] = array[i+1];
        array[i+1] = temp;
        exchange = i;
      }
    }
  }
  printf("2, compare counts = %d\n", num);
}

int main(void) {
  int array1[10] = {4, 7, 2, 6, 1, 12, 0, 36, 21, 17};
  int array2[10] = {4, 7, 2, 6, 1, 12, 0, 36, 21, 17};

  BubbleSort(array1, 10);
  BubbleSort2(array2, 10);

  return 0;
}
