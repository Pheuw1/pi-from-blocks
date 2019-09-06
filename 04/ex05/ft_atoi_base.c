/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/08 23:40:28 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/14 20:47:48 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// make basel take a modified str without spaces and -/+
// cc spms has to return char *
// have to count minuses with other function
// --------------------------------------------------------
// last step done mostly
// problem with first char of base
// function starts reading number from it, ex : f13650e55 = e55;
// problem either coming from power of || createintar(more likely)

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

unsigned int	power_of(unsigned int nb, int power)
{
    if (power >= 1)
        return(nb * power_of(nb, power - 1));
    else
        return 1;
}

char	*sneakybastard(char *str, char *base)
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

int	*createintar(char *str, char *base)
{
	static int ar[100];
	int i;
	int j;
	int sl;
	int f;

	i = 0;
	j = 0;
	sl = 0;
	f = 0;
	while (str[sl])
		sl++;

	while (str[i])
	{
		f = 0;
		while (base[j])
		{	
			if (base[j] == str[i])
			{
				printf("%c",base[j]);
				ar[sl - 1 - i] = j + 1;
			}
			j++;
		}
		j = 0;
		i++;
	}
	return ar;
}

int	countpm(char *str)
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

char	*removespw(char *str)
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
		dest[k]	= str[k + i];
		k++;
	}
	return (dest);
}

int 	ft_atoi_base(char *str, char *base)
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
		//printf("\n%d",ar[j] - 1);
		//printf("\n p : %d", power_of(bl,(j)));
		//printf("\n%d",n);
		j++;
	}
	if (m %2 == 1)
		n = n * -1;
	return(n);
}

int main()
{
	
	char str[] = "31";
	char base[] = "0123456789";
	printf("\n result :%d\n",ft_atoi_base(str,base));
	return(0);
}
