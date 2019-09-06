#ifndef FT_BOOLEAN
#define FT_BOOLEAN
#include <unistd.h>
#define FALSE	0
#define TRUE	1
#define EVEN_MSG "I have an even number of arguments.\n"
#define	ODD_MSG "I have an odd number of arguments.\n"
typedef int	t_bool;
#define EVEN(var) (var % 2)
#define SUCCESS 0
#endif
