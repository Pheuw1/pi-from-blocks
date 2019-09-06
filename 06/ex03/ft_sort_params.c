/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 19:21:09 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 19:28:06 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ftstr(char *str)
{
	int i;

	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
}

int	ft_strcmp(char *s1, char *s2)
{
	int i;
	int x;

	i = 0;
	x = 0;
	while (s1[i] != 0 || s2[i] != 0)
	{
		x += s2[i] - s1[i];
		i++;
		if (x != 0)
		{
			return (x);
		}
	}
	return (x);
}

int	main(int argc, char **argv)
{
	int i;

	char *temp;
		
	if (argc >= 2)
	{
		i = 2;
		while (argv[i])
		{
			if (ft_strcmp(argv[i - 1], argv[i]) < 0)
			{	
				temp = argv[i - 1];
				argv[i - 1] = argv[i];
				argv[i] = temp;
				i = 1;
			}

			i++;
		}

		i = 1;	
		while (argv[i])
		{
			ftstr(argv[i]);
			write(1,"\n",1);
			i++;
		}
	}
	return(0);
}
