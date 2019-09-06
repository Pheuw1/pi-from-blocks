/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/06 12:05:59 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 21:10:49 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int c;
	int temp;

	c = 0;
	while (c <= size / 2)
	{
		temp = tab[size - c - 1];
		tab[size - c - 1] = tab[c];
		tab[c] = temp;
		c++;
	}
}
