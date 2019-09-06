/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/08 01:31:42 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/08 01:58:31 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void pc(char a)
{
	write(1,&a,1);
}

void	ft_putnbr(int nb)
{	
	unsigned int	n;
	
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

int main()
{
	ft_putnbr(5315468);
	return(0);
}
