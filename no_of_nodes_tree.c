#include<stdio.h>
#include<stdlib.h>

typedef struct tnode{
  struct tnode *left;
  int data;
  struct tnode *right;
}tnode;

tnode * add(int n){
  tnode *temp = NULL;
  temp = (tnode *)malloc(sizeof(tnode ));
  temp->data = n;
  temp->left = NULL;
  temp->right = NULL;
  return(temp);
}

void append(tnode **link, int n){
  if(*link==NULL)
    *link=add(n);
  else if ((*link)->data > n)
    append(&((*link)->left), n);
  else
    append(&((*link)->right), n);
}

void traverse(tnode *link){
  printf("%d\t",link->data);
  if(link->left!=NULL)
    traverse(link->left);
  if(link->right!=NULL)
    traverse(link->right);
}

int size_of(tnode *temp){
  if(temp!=NULL)
    return(size_of(temp->left)+1+size_of(temp->right));
  else
    return 0;
}

int main(void ){
  tnode *tree=NULL;
  append(&tree, 5);
  append(&tree, 3);
  append(&tree, 7);
  append(&tree, 2);
  append(&tree, 4);
  append(&tree, 6);
  append(&tree, 8);
  printf("size of given tree is %d\n",size_of(tree));
  traverse(tree);
  return 0;
}
