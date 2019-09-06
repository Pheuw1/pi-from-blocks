//#include "ft_stock_str.h"

typedef struct s_stock_str
{
        int size;
        char *str;
        char *copy;
}	t_stock_str;


int	sl(char *str)
{
	int i;

	while(str[i])
		i++;
	return i;
}

char	*mc(char *str)
{
	int i;
	int l;
	char *c;
	
	i = 0;
	l = sl(str);
	c = malloc(sl + 1 * sizeof(char));
	while (str[i])
	{
		c[i] = str[i];
		i++;
	}
	return c;
	
}
 
struct	s_stock_str	*ft_strs_to_tab(int ac, char **av)
{
	t_stock_str *ar;
	int i;
	
	ar = malloc(sizeof(t_stock_str) * ac);
	i = 0;

	while (i <= ac)
	{
		ar[i].size = ac - 1;
		ar[i].str = av[i];
		ar[i].copy = mc(av[i]);		
		i++;
	}
	return ar;

}	
