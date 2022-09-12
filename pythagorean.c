#include <stdio.h>
#include <math.h>

int main() {
	int A, B;
	double C; 
	printf("Enter side A length: \n");
	scanf("%d", &A);
	printf("Enter side B length: \n");
	scanf("%d", &B);
	C =sqrt((double)(A*A)+(B*B));
	printf("Length of side C: %.2lf\n", C);
	return 0;
}
