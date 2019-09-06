/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 22:44:08 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 23:11:34 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	fstrlen(char *str)
{
	int i;
	
	i = 0;
	while (str[i]) 
		i++;

	return (i);
}

char	*ft_strdup(char *src)
{
	int i;
	char *dest;
	
	i = 0;
	dest = (char *)malloc((fstrlen(src)) * sizeof(char));

	while (src[i])
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = 0;
	return (dest);
}
