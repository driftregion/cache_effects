#ifndef ARR_SIZE
#error "need ARR_SIZE defined"
#endif

int main(int ac, char **av)
{
	int arr[ARR_SIZE] = {};

	if (av[1][0] == '1')
	{
		for (int i = 0; i < (sizeof(arr)/sizeof(int)); i++) arr[i] *= 3;
	}
	if (av[1][0] == '2')
	{
		for (int i = 0; i < (sizeof(arr)/sizeof(int)); i+=16) arr[i] *= 3;
	}
	return 0;
}

