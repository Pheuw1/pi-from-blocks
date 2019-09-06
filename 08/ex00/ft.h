

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void    ft_swap(int *a, int *b)
{
        int c;

        c = *a;
        *a = *b;
        *b = c;
}

void    ft_putstr(char *str)
{
        int i;

        i = 0;
        while (str[i] != '\0')
        {
                ft_putchar(str[i]);
                i++;
        }
}

int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while(str[i])
		i++;
	return i;
}

int     ft_strcmp(char *s1, char *s2)
{
        int i;
        int x;

        x = 0;
        while (s1[i] != 0 || s2[i] != 0)
        {
                x = s2[i] - s1[i];
                i++;
                if (x != 0)
                        return (x);
        }
        return (x);
}

