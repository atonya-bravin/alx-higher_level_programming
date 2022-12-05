#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - checks whether a linked list is empty
 *
 * @head: the head of the linked list
 *
 * Return: 0(not empty) or 1(empty)
 */
int is_palindrome(listint_t **head)
{
	if (*head || *head == NULL)
		return (1);
	return (0);
}
