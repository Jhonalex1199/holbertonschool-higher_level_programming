#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
listint_t *i = list;

if (i == NULL || i->next == NULL)
{
return (0);
}
while (i != NULL && i->next != NULL && list)
{
list = list->next;
i = i->next->next;
if (i == list)
{
return (1);
}
}
return (0);
}
