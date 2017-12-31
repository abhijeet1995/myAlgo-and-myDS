//Print level order traversal line by line

#include<stdio.h>
#include<stdlib.h>

typedef struct tnode{
  struct tnode *left;
  int data;
  struct tnode *right;
}tnode;

int front=0, rear=0;
tnode *queue[50];

//int a=0;

void push(tnode* n){
    if(rear==50)
      printf("\nOverflow!!");
    else
      queue[rear++]=n;
}

tnode* pop(){
        front++;
        return(queue[front-1]);
}

int isempty(){
  if(rear==front)
    return 0;
  else
    return 1;
}

tnode* add(int n){
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
  else if((*link)->data > n)
    append(&((*link)->left), n);
  else
    append(&((*link)->right), n);
}

void bfs(tnode *link){
  tnode *temp=NULL;
  //tnode *got=(tnode *)malloc(sizeof(tnode ));
  if(link==NULL){
    printf("empty\n");
    return;
  }
  push(link);
  //push(got);
  while(isempty()){
    temp=pop();
    //printf("inside while\n");
    /*if(temp==got){
      //printf("inside while-if\n");
      printf("\n");
      //a++;
      //printf("%d\n",a);
      //printf("\n%d\n",isempty());
      if(!isempty())
        break;
      else
        push(got);
      //printf("after break\n");
    }*/
    //else{
      //printf("inside while-else\n");
      printf("%d\t",temp->data);
      push(temp->left);
      push(temp->right);
    //}
  }
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
  append(&tree, 10);
  append(&tree, 9);
  append(&tree, 1);
  bfs(tree);
  //printf("depth of the given tree is %d\n",a);
  return 0;
}
