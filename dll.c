
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node *head = NULL;

struct Node *createNode(int value) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

void create(int n){
int value;
printf("enter the value for the  node: ");
for (int i=0;i<n;i++){
scanf("%d",&value);
struct Node*newNode = createNode(value);
if (head==NULL){
head = newNode;}
else{
struct Node*current = head;
while(current->next!=NULL){
current=current->next;
}
current->next=newNode;
newNode->prev=current;
}}
}

void display() {
    struct Node *current = head;
    if (current == NULL) {
        printf("List is empty.\n");        
        return;
    }

    printf("Doubly Linked List: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void addAtBeginning(int value) {
    struct Node *newNode = createNode(value);
    if (head == NULL) {
        head = newNode;
    } else {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    printf("Element %d added at the beginning.\n", value);
}

void addAtEnd(int value) {
    struct Node *newNode = createNode(value);
    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
    printf("Element %d added at the end.\n", value);
}

void addAnywhere(int value, int position) {
    if (position <= 0) {
        printf("Invalid position.\n");
        return;
    }

    if (position == 1) {
        addAtBeginning(value);
        return;
    }

    struct Node *newNode = createNode(value);
    struct Node *current = head;
    int currentPosition = 1;

    while (current != NULL && currentPosition < position - 1) {
        current = current->next;
        currentPosition++;
    }

    if (current == NULL) {
        printf("Position out of range.\n");
        return;
    }

    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;

    printf("Element %d added at position %d.\n", value, position);
}

void deleteAtBeginning() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node *temp = head;
    head = head->next;
    if (head != NULL) {
        head->prev = NULL;
    }
    free(temp);

    printf("Element deleted from the beginning.\n");
}

void deleteAtEnd() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    if (current->prev != NULL) {
        current->prev->next = NULL;
    } else {
        head = NULL;
    }

    free(current);
    printf("Element deleted from the end.\n");
}

void deleteAnywhere(int position) {
    if (position <= 0) {
        printf("Invalid position.\n");
        return;
    }

    if (position == 1) {
        deleteAtBeginning();
        return;
    }

    struct Node *current = head;
    int currentPosition = 1;

    while (current != NULL && currentPosition < position) {
        current = current->next;
        currentPosition++;
    }

    if (current == NULL) {
        printf("Position out of range.\n");
        return;
    }

    if (current->prev != NULL) {
        current->prev->next = current->next;
    } else {
        head = current->next;
    }

    if (current->next != NULL) {
        current->next->prev = current->prev;
    }

    free(current);
    printf("Element deleted from position %d.\n", position);
}

int main() {
    int choice, value, position,n;

    while (1) {
        printf("\n1. Display\n2. Add at Beginning\n3. Add at End\n4. Add Anywhere\n5. Delete at Beginning\n6. Delete at End\n7. Delete Anywhere\n8. create\n9. exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                display();
                break;
            case 2:
                printf("Enter the value to add: ");
                scanf("%d", &value);
                addAtBeginning(value);
                break;
            case 3:
                printf("Enter the value to add: ");
                scanf("%d", &value);
                addAtEnd(value);
                break;
            case 4:
                printf("Enter the value to add: ");
                scanf("%d", &value);
                printf("Enter the position: ");
                scanf("%d", &position);
                addAnywhere(value, position);
                break;
            case 5:
                deleteAtBeginning();
                break;
            case 6:
                deleteAtEnd();
                break;
            case 7:
                printf("Enter the position: ");
                scanf("%d", &position);
 deleteAnywhere(position);
                break;
           case 8:
printf("enter the no. of nodes");
scanf("%d",&n);
                create(n);
                break;
            case 9:
                exit(0);
            default:
                printf("Invalid choice.\n");
        }
    }
return 0;
}