//#include "ft_stock_str.h"


typedef struct s_stock_str
{
        int size;
        char *str;
        char *copy;
}t_stock_str;


int     sl(char *str)
{
        int i;

        while(str[i])
                i++;
        return i;
}

char    *mc(char *str)
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
 
struct  s_stock_str     *ft_strs_to_tab(int ac, char **av)
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


void	pc(char a)
{
	write(1, &a, 1);
}

void    ft_putstr(char *str)
{
        int i;
        i = 0;
        while(str[i])
        {
                write(1,&str[i],1);
                i++;
        }
}

void    ft_putnbr(int nb) 
{           
        unsigned int    n;  
            
        if (nb < 0)
        {   
                pc('-');
                n = nb *-1;
        }
        else
                n = nb;

        if (nb >= 10 || nb <= -10)
                ft_putnbr(n/10);
        pc(n%10 + 48);
}

void	ft_show_tab(struct s_stock_str *par)
{
	int i;

	i = 0;
	while (par[i].str)
	{
		ft_putstr(par[i].str);
		pc('\n');
		ft_putnbr(par[i].size);
		pc('\n');
		ft_putstr(par[i].copy);
		pc('\n');
		i++;
	}

	
}

int main(int argc, char **argv)
{
	ft_show_tab(ft_strs_to_tab(argc,argv));
	return 0;
}
