#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define ONE 1
#define MAX 100

typedef struct node
{
    int id;             // ID of user
    int numfren;        // number of friends of user
    char name[MAX];     // name of user
    int *friends;       // friends of user as an array
    struct node *right; // user to the right
    struct node *left;  // user to the left
} node;

struct node *retUser(char str[MAX])
{
    char name[MAX];
    char ID[MAX];
    char strfriends[MAX];

    // copied ID
    char *token = strtok(str, ",");
    strcpy(ID, token);

    // copied Name
    token = strtok(NULL, ",");
    strcpy(name, token);

    // copied friends' ID
    token = strtok(NULL, ",");
    strcpy(strfriends, token);
    // printf("%s\n",(strfriends));

    // creating user nodes
    int id = atoi(ID);
    struct node *user = malloc(sizeof(struct node));
    user->id = id;
    user->friends = (int *)malloc(MAX * sizeof(int));
    strcpy(user->name, name);

    // adding user's friend's IDs
    token = strtok(strfriends, "|");
    int i = 0;
    while (token != NULL)
    {

        int temp = atoi(token);
        user->friends[i] = temp;
        i++;
        token = strtok(NULL, "|");
    }
    user->numfren = i;
    if (i == 0)
    {
        user->friends[i] = -1;
    }

    return user;
}

// search for user with id=key
struct node *search(int key, struct node *users)
{
    if (users == NULL || users->id == key)
        return users;
    if (key > users->id)
        return (search(key, users->right));
    return (search(key, users->left));
}

// see document for explanattion
struct node *refineUser(struct node *user, struct node *users)
{
    user->left = user->right = NULL;
    node *cur = search(user->id, users);
    while (cur != NULL)
    {
        user->id = user->id + ONE;
    }
    if (user->numfren != 0)
    {
        int n, i, y;
        n = user->numfren;
        i = 0;
        while (i < n)
        {
            cur = search(user->friends[i], users);
            if (cur != NULL)
            {
                if (cur->numfren != 0)
                {
                    y = 0;
                    while (cur->friends[y] != '\0')
                        y = y + ONE;
                    cur->friends[y] = user->id;
                    cur->numfren = cur->numfren + ONE;
                }
                else
                {
                    cur->friends[0] = user->id;
                    cur->numfren = cur->numfren + ONE;
                }
                i = i + ONE;
            }
            else
            {
                for (int j = i; j < n - 1; j = j + ONE)
                {
                    user->friends[j] = user->friends[j + ONE];
                }
                user->friends[n - ONE] = '\0';
                user->numfren = user->numfren - ONE;
                n = n - ONE;
            }
        }
    }

    if (user->numfren == 0)
    {
        user->friends[0] = -1;
    }
    return user;
}

// insert user with id
struct node *insertUser(struct node *root, int id, struct node *user)
{
    user->left = user->right = NULL;
    if (root == NULL)
    {
        root = user;
        return root;
    }
    node *cur = root;
    node *prev = NULL;
    while (cur != NULL)
    {
        prev = cur;
        if (id > cur->id)
            cur = cur->right;
        else
            cur = cur->left;
    }
    if (id > prev->id)
        prev->right = user;
    else
        prev->left = user;

    return root;
}

// prints friends list
void friends(int id, struct node *users)
{
    int i;
    node *cur = search(id, users);
    if (cur->numfren > 0)
    {
        for (i = 0; i < cur->numfren; i = i + ONE)
        {
            printf("%d\n", cur->friends[i]);
        }
    }
    else
    {
        printf("%d \n", -1);
        return;
    }
}

// find child node with minimum value (inorder successor) - helper to delete node
struct node *minValueNode(struct node *node)
{
    node = node->right;
    while (node->left != NULL)
    {
        node = node->left;
    }
    return node;
}

// deletes itself from its friend's nodes
void deleteFriends(int key, struct node *users)
{
    if (users == NULL)
    {
        return;
    }
    deleteFriends(key, users->left);
    int n, i, j;
    n = users->numfren;
    i = 0;
    while (users->friends[i] != key && i < n)
    {
        i = i + ONE;
    }
    if (users->friends[i] == key)
    {
        for (j = i; j < n - 1; j = j + ONE)
        {
            users->friends[j] = users->friends[j + ONE];
        }
        users->friends[n - ONE] = '\0';
        users->numfren--;
    }
    if (users->numfren == 0)
    {
        users->friends[0] = -ONE;
    }
    deleteFriends(key, users->right);
}

// Deleting a node
struct node *deleteNode(struct node *root, int key)
{
    if (root == NULL)
    {
        return root;
    }
    node *cur = root, *prev = NULL, *succ, *n1;
    while (cur != NULL)
    {
        if (key == cur->id)
        {
            break;
        }
        prev = cur;
        if (key < cur->id)
        {
            cur = cur->left;
        }
        else
        {
            cur = cur->right;
        }
    }
    if (cur == NULL)
    {
        return (root);
    }
    if (cur->left == NULL)
    {
        n1 = cur->right;
    }
    else if (cur->right == NULL)
        n1 = cur->left;
    else
    {
        node *n2 = NULL;
        node *succ = cur->right;
        while (succ->left != NULL)
        {
            n2 = succ;
            succ = succ->left;
        }
        if (n2 != NULL)
            n2->left = succ->right;

        else
            cur->right = succ->right;

        cur->id = succ->id;
        cur->numfren = succ->numfren;
        strcpy(cur->name, succ->name);
        cur->friends = succ->friends;

        free(succ);
        return (root);
    }

    if (prev == NULL)
    {
        free(cur);
        return (root);
    }
    if (cur == prev->left)
        prev->left = n1;
    else
        prev->right = n1;
    free(cur);
    return (root);
}

// Print USER's IDs in ascending order
void printInOrder(node *myusers)
{
    if (myusers == NULL)
        return;
    printInOrder(myusers->left);
    printf("%d %s\n", myusers->id, myusers->name);
    printInOrder(myusers->right);
}

int main(int argc, char **argv)
{
    node *users = NULL;
    while (1)
    {

        int opt, id;
        // fflush(stdin);
        scanf("%d", &opt);
        char str[MAX];
        switch (opt)
        {
        case 1:

            scanf("%s", str);
            struct node *tbins = retUser(str);
            tbins = refineUser(tbins, users);
            users = insertUser(users, tbins->id, tbins);
            // printf("i am back");
            // printf(" data before printing is :%d  ",users->id);
            // printInOrder(users) ;

            break;

        case 2:

            scanf("%d", &id);
            // printf("printing leftof eevrything :%d  %d ",users->left,users->left->left);
            deleteFriends(id, users);
            users = deleteNode(users, id);
            break;

        case 3:

            scanf("%d", &id);
            node *result = search(id, users);
            if (result == NULL)
                printf("USER NOT IN TREE.\n");
            else
            {
                printf("%d\n", result->id);
            }
            break;

        case 4:
            scanf("%d", &id);
            friends(id, users);
            break;

        case 5:

            printInOrder(users);
            break;

        case 6:
            exit(0);
            break;

        default:
            printf("Wrong input! \n");
            break;
        }
    }
    return 0;
}