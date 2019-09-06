//#include "ft_stock_str.h"

typedef struct s_stock_str
{
        int size;
        char *str;
        char *copy;
}t_stock_str;

int main()
{
	t_stock_str ts;
	char a[] = "Hey";
	char b[] = "Its me";

	ts.size = 4;
	ts.str = a;
	ts.copy = b;

	printf("%s",ts.str);
	return 0;
}

