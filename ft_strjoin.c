/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/13 20:51:22 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/13 23:03:35 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int slp(char **strs, int size)
{
	int i;
	int l;

	i = 0;
	l = 0;
	while (i < size)
	{
		l += sl(strs[i]);
		i++;
	}
	return l;
}

int	sl(char *str)
{
	int i;

	i = 0;
	while (str[i])
		i++;

	return i;
}

char    *cat(char *dest, char *src)
{
    int l;
    int i;

    l = sl(dest);
    i = 0;
    while (src[i] != 0)
    {
        dest[l + i] = src[i];
        i++;
    }
	dest[l + i] = 0;
    return(dest);
}

char *ft_strjoin(int size, char **strs, char *sep)
{
	int i;
	int m;
	char *ar;
	
	i = 0;
	m = slp(strs, size);
	printf("m = %d\n",m);
	ar = malloc(m + (size - 1 * sl(sep)) * sizeof(char));
	
	while (i < size)
	{
		cat(ar,strs[i]);
		if (i < size - 1)
			cat(ar,sep);
		i++;
	}

	return (ar);
}

int main()
{
	char s1[] = "Hello ";
	char s2[] = "I want ";
	char s3[] = "bees.";
	char s4[] = "I WANT THEM NOW ";
	char s5[] = "GIVE ME BEESEES ";
	char s6[] = "AAAA!!!!!";
	char sep[] = "~~~~~~~~~~~~_|*@*|_~~~~~~~~~~~~";
	char **strs;
	strs = malloc(6 * sizeof(char *));
	strs[0] = s1;
	strs[1] = s2;
	strs[2] = s3;
	strs[3] = s4;
	strs[4] = s5;
	strs[5] = s6;
	printf("%s",ft_strjoin(6,strs,sep));
	free(strs);
	return(0);
}
