/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush0X.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/03 19:44:53 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/04 18:51:02 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// include args as params of main

#include <unistd.h>

void	ft_putchar(char a)
{
	write(1, &a, 1);
}

void	ft_printline(char l, char m, char r, int x)
{	
	int i;
	
	i = 1;
	if (i == 1)	{
		ft_putchar(l);
		i++;
	}
	while (i>1	&&	i<x)	{
		ft_putchar(m);
		i++;
	}	
	if (i == x)
		ft_putchar(r);
}

void	rush(int x, int y)
{
	int j;

	j = 1;

	if (y!=0	&&	x!=0)	{
		if (j == 1)	{
			ft_printline('@', '!', '@', x);
			ft_putchar('\n');
			j++;
		}
		while (j>1	&&	j<y)	
		{
			ft_printline('~', 'O', '~', x);
			ft_putchar('\n');
			j++;
		}
		if (j == y)	{
			ft_printline('@', '!', '@', x);
		}
	}
	write(1,"\n",1);

}

int main()
{
	rush(50,50);	
	return(0);
}
