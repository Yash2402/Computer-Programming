#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define data_t int

typedef struct node_t {
  data_t data;
  struct node_t *prev, *next;
} node_t;

typedef struct list_t {
  int size;
  node_t *head, *tail;
} list_t;

list_t *list_init();
bool list_push(data_t data);

int main(void) {
  list_t *my_list = list_init();
  return EXIT_SUCCESS;
}

list_t *list_init() {
  list_t *new_list = (list_t *)malloc(sizeof(list_t));

  if (new_list == NULL) {
    fprintf(stderr, "ERROR: Failed to allocate memory for list\n");
    exit(EXIT_FAILURE);
  }

  new_list->size = 0;
  new_list->head = NULL;
  new_list->tail = NULL;

  return new_list;
}

bool list_push(data_t data) {
  node_t *new_node = (node_t *)malloc(sizeof(node_t));

  if (new_node == NULL) {
    fprintf(stderr, "ERROR: Failed to allocate memory for node\n");
    exit(EXIT_FAILURE);
  }

  new_node->data = data;
}
