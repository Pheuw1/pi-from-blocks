/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/07 00:02:26 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/14 00:01:04 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while (str[i] != 0)
		i++;
	return (i);
}

char	*ft_strcat(char *dest, char *src)
{
	int l;
	int i;

	l = ft_strlen(dest);
	i = 0;
	while (src[i] != 0)
	{
		dest[l + i] = src[i];
		i++;
	}
	dest[i] = 0;
	return (dest);
}
