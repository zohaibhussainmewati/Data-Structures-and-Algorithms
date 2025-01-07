/***************************************************************************************************************************************************************
*Title		: This the header file for the Red Black Tree
****************************************************************************************************************************************************************/
#ifndef RBT_H
#define RBT_H
#define SUCCESS 0
#define FAILURE -1

typedef int data_t;

typedef struct node
{
	struct node *left;
	data_t data;
	struct node *right;
	int color;
}tree_t;

/* keep all the prototypes of the functions here */

#endif
