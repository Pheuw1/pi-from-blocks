# include <stdio.h>
# include <stdlib.h>

int basel(char *str)
{
        int i;
        int j;
        int c;

        i = 0;
        j = 0;
        c = j + 1;
        while (str[i])
                i++;
        while (j < i - 1)
        {
                while (str[c])
                {
                        if (str[c] == str[j])
                                return 0;
                        c++;
                }
                j ++;
                c = j + 1;
        }

        return i;
}

int     countpm(char *str)
{
        int i;
        int m;

        i = 0;
        m = 0;

        while (str[i] == 32 || (str[i] >= 9 && str[i] <= 12))
                i++;

        while (str[i] == 45 || str[i] == 43) 
        {
                if (str[i] == 45) 
                        m++;
                i++;
        }
        return(m);
}

unsigned int    power_of(unsigned int nb, int power)
{
    if (power >= 1)
        return(nb * power_of(nb, power - 1));
    else
        return 1;
}

char    *sneakybastard(char *str, char *base)
{
        int i;
        int j;
        int f;
        static char bastard[30];

        i = 0;
        j = 0;
        f = 0;
        while (str[i])
        {
                f = 0;
                while (base[j])
                {
                        if (str[i] == base[j])
                        {
                                bastard[i] = str[i];
                                f = 1;
                        }
                        j++;
                }
                if (f != 1)
                        return bastard;
                j = 0;
                i++;    
        }
        return bastard;
}

char    *removespw(char *str)
{
        int i;
        int k;
        static char dest[100];

        i = 0;
        k = 0;
        while (str[i] == 32 || (str[i] >= 9 && str[i] <= 12) 
                || (str[i] == 45 || str[i] == 43))
                i++;

        while (str[k + i]) 
        {
                dest[k] = str[k + i]; 
                k++;
        }
        return (dest);
}

int     *createintar(char *str, char *base)
{
        static int ar[100];
        int i;
        int j;
        int sl; 

        i = 0;
        j = 0;
        sl = 0;
        while (str[sl])
                sl++;

        while (str[i])
        {
                while (base[j])
                {       
                        if (base[j] == str[i])
                        {
                                ar[sl - 1 - i] = j + 1;
                        }
                        j++;
                }
                j = 0;
                i++;
        }
        return ar;
}

char	*ft_nbr_base(int nbr, char *base)
{
        unsigned int n;
        int bl;
	static char ab[30];
	int i;
	
	bl = basel(base);
	i = 0;
	if (bl < 2)
	{
		ab[i] = '0';
		return ab;	
	}
	while (nbr >= bl)
	{
        	n = nbr % bl;
		ab[i] = base[n];
		i++;
		nbr = nbr/bl;
	}
	n = nbr % bl;
	ab[i] = base[n];
	printf("this is ab :%s\n",ab);
	return ab;
}

int     ft_atoi_base(char *str, char *base)
{
        unsigned int n;
        int bl;
        int *ar;
        int j;
        int m;

        n = 0;
        j = 0;
        m = countpm(str);
        str = sneakybastard(removespw(str), base);
        bl = basel(base);
        ar = createintar(str,base);
        if (bl < 2)
                return 0;
        while (ar[j])
        {
                n += (ar[j] - 1) * power_of(bl,(j));
                j++;
        }	
        if (m %2 == 1)
                n = n * -1;
        return(n);
}


char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	int atoib;
	char *cdb;
	static char fint[30];
	int l;
	int i;
	
	cdb = malloc(sizeof(char) * 30);
	atoib = ft_atoi_base(nbr, base_from);
	printf("this is atoib : %d\n",atoib);
	cdb = ft_nbr_base(atoib, base_to);
	printf("this is cdb :%s",cdb);
	i = 0;
	l = 0;
	while (cdb[l])
		l++;
	while (i <= l - 1) 
	{
		fint[i] = cdb[l - 1 - i]; 
		i++;
	}
	return fint;
}

int main (int ac, char **av)
{
	if (ac >= 2)
		printf("\nresult : %s\n",ft_convert_base(av[1],av[2],av[3]));
	else
		printf("gimme a number its base and the base you want to convert it to >:(\n");
	return 0;
}
