#include<stdio.h>
#include<stdlib.h>

typedef struct tnode{
  struct tnode *left;
  int data;
  struct tnode *right;
}tnode;

int flag=1;

tnode * add(int n){
  tnode *temp = NULL;
  temp = (tnode *)malloc(sizeof(tnode ));
  temp->data = n;
  temp->left = NULL;
  temp->right = NULL;
  return(temp);
}

void check(tnode *link1, tnode *link2){
  if(flag==0)
    return;
  if((link1==NULL && link2!=NULL) || (link1!=NULL && link2==NULL)){
    flag=0;
    return;
  }
  if(link1==NULL && link2==NULL)
    return;
  check(link1->left, link2->left);
  if(link1->data!=link2->data){
    flag=0;
    return;
  }
  check(link1->right, link2->right);
}

void append(tnode **link, int n){
  if(*link==NULL)
    *link=add(n);
  else if ((*link)->data > n)
    append(&((*link)->left), n);
  else
    append(&((*link)->right), n);
}

int main(void ){
  tnode *tree=NULL, *tree1=NULL;
  append(&tree, 5);
  append(&tree, 3);
  append(&tree, 7);
  append(&tree, 2);
  append(&tree, 4);
  append(&tree, 6);
  append(&tree, 8);
  append(&tree1, 5);
  append(&tree1, 3);
  append(&tree1, 7);
  append(&tree1, 2);
  append(&tree1, 4);
  append(&tree1, 6);
  check(tree,tree1);
  if(flag==0)
    printf("both the trees are different\n");
  else
    printf("both the trees are same\n");
  return 0;
}
