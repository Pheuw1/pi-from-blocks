/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 23:20:41 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/13 20:31:53 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_ultimate_range(int **range, int min, int max)
{
    int *iar;
    int i;
    int j;
	
    iar = (int *)malloc((max - min)* sizeof(int));
    i = min;
    j = 0;

	if (min >= max)
		range = 0;
		
    while (i < max)
    {
        iar[j] = i;
        i++;
        j++;
    }

	*range = iar;
	return (max - min);
}

int main()
{
	int i = 0;
	int **range;
	range = malloc(1 * sizeof(int *));
	prinf("%d",ft_ultimate_range(range,15000,20000));
	return(0);
}
