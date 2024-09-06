#include <stdlib.h>

/**
 * Definition for MyHashMap using a fixed-size array.
 */
typedef struct {
    int *data;  // Array to store the values for the keys
    int size;   // Size of the array
} MyHashMap;

/**
 * Creates a new MyHashMap object with a fixed-size array.
 * @return Pointer to the newly created MyHashMap object.
 */
MyHashMap* myHashMapCreate() {
    MyHashMap *hash = (MyHashMap*)malloc(sizeof(MyHashMap));
    if (hash == NULL) {
        return NULL;  // Memory allocation failed
    }
    hash->data = (int*)calloc(1000001, sizeof(int));
    if (hash->data == NULL) {
        free(hash);  // Free previously allocated memory if this fails
        return NULL;
    }
    hash->size = 1000001;
    for (int i = 0; i < 1000001; i++) {
        hash->data[i] = -1;  // Initialize all values to -1 (indicating empty)
    }
    return hash;
}

/**
 * Inserts or updates the value associated with the key.
 * @param obj Pointer to the MyHashMap object.
 * @param key Integer key to be inserted or updated.
 * @param value Integer value to be associated with the key.
 */
void myHashMapPut(MyHashMap* obj, int key, int value) {
    if (key >= 0 && key < 1000001) {
        obj->data[key] = value;
    }
}

/**
 * Retrieves the value associated with the key.
 * @param obj Pointer to the MyHashMap object.
 * @param key Integer key whose associated value is to be retrieved.
 * @return Integer value associated with the key. Returns -1 if the key does not exist.
 */
int myHashMapGet(MyHashMap* obj, int key) {
    if (key >= 0 && key < 1000001) {
        return obj->data[key];
    }
    return -1;  // Key does not exist
}

/**
 * Removes the key and its associated value if the key exists.
 * @param obj Pointer to the MyHashMap object.
 * @param key Integer key to be removed.
 */
void myHashMapRemove(MyHashMap* obj, int key) {
    if (key >= 0 && key < 1000001) {
        obj->data[key] = -1;  // Set the value to -1 to indicate removal
    }
}

/**
 * Frees the memory allocated for the MyHashMap object.
 * @param obj Pointer to the MyHashMap object to be freed.
 */
void myHashMapFree(MyHashMap* obj) {
    free(obj->data);  // Free the array
    free(obj);        // Free the struct
}

/**
 * Example usage:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);
 * int param_2 = myHashMapGet(obj, key);
 * myHashMapRemove(obj, key);
 * myHashMapFree(obj);
 */
