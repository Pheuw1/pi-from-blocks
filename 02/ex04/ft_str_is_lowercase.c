/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_lowercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/06 17:40:34 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 21:34:35 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_lowercase(char *str)
{
	int i;

	i = 0;
	while (str[i] != 0)
	{
		if (str[i] <= 97 || str[i] >= 122)
		{
			return (0);
		}
		i++;
	}
	return (1);
}
