#include <stdio.h>
int main() {
	int A, B, V, day;
	scanf("%d %d %d", &A, &B, &V);
	day = (V - B) / (A - B);
	if ((V - B) % (A - B) != 0) day++;
	printf("%d\n", day);
}