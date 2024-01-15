#ifndef TEST_CLASS_H
#define TEST_CLASS_H


class test_class {
    public:
        test_class * container;
        int b;
        test_class();
        test_class(int, int);
        test_class(int);
        ~test_class();
        int get_b();
        test_class* get_member(int);
};



#endif
