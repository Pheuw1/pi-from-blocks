/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_program_name.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/12 00:10:34 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 00:47:02 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void    ft_putstr(char *str)
{
    int i;
    i = 0;
    while(str[i])
    {
        write(1,&str[i],1);
        i++;
    }
}

int main(int argc, char **argv)
{
	ft_putstr(argv[0]);
	return(0);
}
