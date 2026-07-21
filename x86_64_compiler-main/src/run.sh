rm -f tokens && cd x86_64_compiler-main/src && gcc *.c && ./a.out && as -o test.o chat.s && ld -o test test.o && ./test && echo $?
echo "Return Value: $?"
