/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/07 22:02:42 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/08 00:28:33 by gmehdevi         ###   ########.fr       */
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


unsigned int ft_strlcat(char *dest, char *src, unsigned int size)
{
	int i;
	int c;
	int l;

	l = ft_strlen(dest) - 1;
	i = 0;
	c = 0;
	

	while(c != size - l)
	{
		dest[l + c] = src[c];
		c++;
	}
	dest[c] = 0;
	return(c);
}


int main()
{
	int x;
	x = 0;
	char dest[100] = "01234567890123456789012345";
	char src[] = "is not something i'm sure of yet";
	while(dest[x])
	{
		x++;
	}
	printf("%d",ft_strlcat(dest,src,100));
	return(0);
}
