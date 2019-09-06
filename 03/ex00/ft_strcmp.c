/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/06 21:56:41 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/13 23:54:32 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
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