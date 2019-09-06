/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: gmehdevi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/08/07 21:21:22 by gmehdevi          #+#    #+#             */
/*   Updated: 2019/08/12 17:01:46 by gmehdevi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


char *ft_strstr(char *str, char *to_find )
{
	int i;
	int o;
	
	i = 0;
	o = 0;
	while (str[i] && to_find[o])
	{
		while (to_find[o] == str[i + o])
		{	
			o++;
		}
		if (to_find[o] != 0)
			o = 0;
		i++;
	}
	if (o == 0)
		return 0;

	return(&str[i-1]);
}

int main()
{
	char dest[] = "obama made my frogs gay";
	char src[] = "fru";
	printf("%s",ft_strstr(dest,src));
	return(0);

}
