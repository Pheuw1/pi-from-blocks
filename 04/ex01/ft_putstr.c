/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/08 01:06:43 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/08 01:13:56 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include<unistd.h>


void	ft_putstr(char *str)
{
	int i;
	i = 0;
	while(str[i])
	{
		write(1,&str[i],1);
		i++;
	}
}

int main()
{
	char dest[] = "Obama made my frogs gay";
	ft_putstr(dest);
	return(0);
}
