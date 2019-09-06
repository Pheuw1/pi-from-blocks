/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   backtracking.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/11 17:12:53 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/11 23:15:33 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void	pc(char e)
{
	write(1,&e,1);
}

int ft_backtrack(int **m, int p1, int p2, int size ,int n)
{
    printf("p1:%d, p2:%d ,n:%d ,", p1,p2,n);
	
	if (p2 == size)
	{
		p1 += 1;	
		p2 = 0;
	}
	if (n != size)
		n++;
	else
		n = 1;
	
	if (p1 == size)
		return(1);
    

    while (n <= size)
    {
        if (n > 0)
        {	
			m[p1][p2] = n;
		 	return (ft_backtrack(m, p1, p2 + 1, size, n));	
		}
		else
		{	
			if (p2 == 0 && p1 != 0)
				return (ft_backtrack(m, p1 - 1, p2, size, n));
			if (p2 != 0)
				return (ft_backtrack(m, p1, p2 - 1, size, n));
			else 
				return (ft_backtrack(m, p1, p2, size, n));
		}
	}
    return (0);
}

int check_matrix(int **m)
{
	int i;
	int j;
	int c;
	
	i = 0;
	j = 0;	
}

int	**stotti(char *str)
{
	int i;
	int cu[4];
	int cd[4];
	int rl[4];
	int rr[4];
	int *all[4];

	i = 0;
	while (i < 4)
	{
		cu[i] = str[i];
		i++;
	}
	all[0] = cu;		
	while (i < 8)
	{
		cd[i] = str[i];
		i++;
	}
	all[1] = cd;	
	while(i < 12)
	{
		rl[i] = str[i];
		i++;
	}
	all[2] = rl;
	while(i < 16)
	{
		rr[i] = str[i];
		i++;
	}
	all[3] = rr;
	return(all);
}

int		valid_string(char *str)
{
	int i;
	int j;

	j = 0;
	i = 0;
	while (str[i])
	{
		if (!(str[i] == ' ' || (str[i] >= '1' && str[i] <= '4')))
			return (0);
		i++;	
	}
	i = 0;
	while (str[i])
	{
		if (str[i] >= '1' && str[i] <= '4')
			j++;
		i++;
	}
	if (j == 16)
		return (1);
	return (0);
}

int     **matrix(int size)
{
	int **m;
    int i;
    int j;
    int t;

    i = 0;
    j = 0;
    m = (int **)malloc(size * sizeof(int *));
 
    while(i < size)
    {
        m[i] = (int *)malloc(size * sizeof(int));
        while(j < size)
        {
            m[i][j] = 0;
            j++;
            t++;
        }
        j = 0;
        i++;
    }
    return (m);
}

void	printM(int **m, int size)
{
    int i;
    int j;

    i = 0;
    j = 0;
    while (i < size)
    {
        while (j < size)
        {
            pc(m[i][j] + 48);
            if (j != size - 1)
                pc(' ');
            j++;
        }
        pc('\n');
        i++;
        j = 0;
    }
}

int main()
{	
	int tab[] = {1,2,7,5,6,5,4,2,1,4,2,3,1,4,5,2,0};
	int **fag;
	fag = matrix(4);
	printf("\n%d\n",ft_backtrack(fag,0,0,4,0));
	printM(fag,4);
	return(0);
}
