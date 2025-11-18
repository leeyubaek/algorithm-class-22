#defined Stack class with push, pop,peek,is_empty, and size method
#Stack ADT
class Arraystack:
    def _init(self,capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if not self.is_full():
            self.top += self.top + 1
            self.array[self.top] = item
            print("Push: {item!r} -> stack is not {self.array[:self.top + 1]}")
        else:
            raise OverflowError("Stack Overflow")

    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print ("POP: {item!r}-> stack is not {self.array[:self.top + 1]}")
            return item
        else:
            raise IndexError("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    
    def size(self):
        return self.top + 1
    
#Test the Stack class
def reverse_string(statement):
    print("\n[1] PUSH 단계---------------------------------------")

    st = Arraystack(len{statement})
    
    for char in statement:
        st.push(char)

    print("\n[2] POP 단계---------------------------------------")
    out = []
    while not st.is_empty():
        out.append(st.pop())
    
    result = ''.join(out)

    print("\n[3] 최종 결과 : {result}")
    return result

if __name__ == "__main__":
    statement = "Hello Word!"
    reverse_string(statement)
