/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/08 02:02:27 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/14 01:30:37 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int ft_atoi(char *str)
{
	int i;
	int m;
	int n;

	i = 0;
	m = 0;
	n = 0;
	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 12))
	{
		i++;
	}
	while (str[i] == 45 || str[i] == 43)
	{	
		if (str[i] == 45)
			m++;		
		i++;	
	}
	while (str[i] >= 48 && str[i] <= 57)
	{
		n = (n * 10) + (str[i] - 48);
		i++;
	}		
	if (m % 2 == 1)
		n = n * -1;
	return(n);
}
int main()
{
	char src[] = "  -+-+--+-+-+-+-+-+--1234)567aajsbdkajbsdkj0    \n2";
	printf("%d",ft_atoi(src));
	return(0);
}
