/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/08 21:46:03 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/09 02:00:48 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	basel(char *str)
{
	int i;
	int c;

	i = 0;
	while(str[i])
	{
		c = i + 1;
		while ((str[i] != str[c]) && str[c] != '\0')
		{
			if (str[c] == '\0')
				c = i;
			c++;
		}
		if (str[i] == str[c])
		{	
			return(1);
		}
		i++;
	}
	return(i);

}

void	pc(char a)
{
	write(1,&a,1);
}

void	ft_putnbr_base(int nbr, char *base)
{
	unsigned int n;
	int			bl;
	int 		 i;

	bl = basel(base);

	if (nbr < 0)
	{
		pc('-');
		n = nbr * -1;
	}
	else
		n = nbr;
	
	i = n % bl;
	if (bl > 1)
	{
		if (n >= bl)
			ft_putnbr_base(n/bl,base);
	
		pc(base[i]);
	}
}

int main()
{
	char str[] = "010";
	ft_putnbr_base(81,str);
	return(0);
}
