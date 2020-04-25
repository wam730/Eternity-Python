#include<stdio.h>
#include<cstdlib>
int main()
{
	int i, j, k, m, n;
	for (i = 1; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			for (k = 0; k < 10; k++)
			{
				m = i * i * i + j * j * j + k * k * k;
				n = 100 * i + 10 * j + k;
				if (m == n)
				{
					printf("%d\n", m);
				}
			}
		}
	}
	system("pause");
	return 0;
}