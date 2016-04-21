#include<stdio.h>

int main()
{
int y,m,d;

scanf("%d%d%d",&y,&m,&d);
dow(y,m,d);
return 0;
}

int dow(int y, int m, int d){ 
  int c,z;

  static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4}; 
  z = (y + t[m-1] + d + c) % 7;
  printf("%d",z);
  return 0;
}

