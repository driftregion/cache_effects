#ifndef ARR_SIZE
#error "need ARR_SIZE defined"
#endif

#ifndef K 
#error "need ARR_SIZE defined"
#endif

int main()
{
    int arr[ARR_SIZE] = {};

    for (int i = 0; i < (sizeof(arr)/sizeof(int)); i += K) arr[i] *= 3;
	return 0;
}

