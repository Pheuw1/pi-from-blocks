/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 23:01:06 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 23:20:39 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	*ft_range(int min, int max)
{
	int *iar;
	int i;
	int j;

	iar = (int *)malloc((max - min)* sizeof(int));
	i = min;
	j = 0;
	while (i < max)
	{
		iar[j] = i;
		i++;
		j++;		
	}
	return (iar);
}

int main()
{
	ft_range(15000,19995);
	return 0;
}
