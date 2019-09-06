/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 10:12:53 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 10:24:40 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

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

int main(int argc, char **argv)
{
	int c;
	int j;

	j = 0;
	c = 1;
	while (argv[j])
		j++;
	while (c < j)
	{	
		ftstr(argv[j - c]);
		write(1,"\n",1);
		c++;
	}
	return 0;
}
