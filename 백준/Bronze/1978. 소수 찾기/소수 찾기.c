#include <stdio.h>
#include <stdlib.h>

int find(int a);

int main(void)
{
	int N;
	int *array;
	int result = 0;

	scanf("%d", &N);
	array = (int *)malloc(N * sizeof(int));

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &array[i]);
	}
	for (int j = 0; j < N; j++)
	{
		result = result + find(array[j]);
	}

	printf("%d", result);


	free(array);

	return 0;

}
int find(int a)
{
	int count = 0;

	if (a == 1)
		return 0;
	if (a == 2)
		return 1;

	for (int i = 2; i < a ; i++)
	{
		if (a%i == 0)
			return 0;

	}

	return 1;

}