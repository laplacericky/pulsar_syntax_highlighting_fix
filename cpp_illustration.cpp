#include "test_class.h"
#include <cstddef>

test_class::test_class(){
    this->b = 0;
    this->container = NULL;
}

test_class::test_class(int b){
    this->b = b;
    this->container = NULL;
}

test_class::test_class(int b, int n){
    this->b = b;
    if (n > 0){
        this->container = new test_class[n];
        for (int i = 0; i < n; i++) {
            this->container[i].b = i;
        }
    }
}

test_class::~test_class(){
        delete[] this->container;
}
int test_class::get_b(){
    return this->b;
}
test_class* test_class::get_member(int i){
    return &(this->container[i]);
}
