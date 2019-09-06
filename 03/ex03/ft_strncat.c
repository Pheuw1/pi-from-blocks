/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/07 21:11:39 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/07 21:20:14 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int ft_strlen(char *str)
{
	int i;
	i = 0;
	while (str[i])
	{
		i++;
	}
	return(i);
}

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	int l;
	int i;

	l = ft_strlen(dest);
	i = 0;
	while (src[i] && i < nb)
	{
		dest[l + i] = src[i];
		i++;
	}
	return(dest);
}

int main ()
{
	char dest[500] = "tots bruh moment when you say :";
	char src[] = "this is a test isn't it"; 
	printf("%s", ft_strncat(dest,src,15));
	return(0);
}
