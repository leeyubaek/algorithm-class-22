class Node:
    def __init__(self, elem, next=None):
        """노드 초기화"""
        self.data = elem    # 노드에 저장할 데이터
        self.link = next    # 다음 노드를 가리키는 링크
    
    def append(self, new):
        """현재 노드 다음에 새 노드를 삽입"""
        if new is not None:
            new.link = self.link    # 새 노드가 현재 노드의 다음 노드를 가리키도록
            self.link = new         # 현재 노드가 새 노드를 가리키도록
    
    def popNext(self):
        """현재 노드 다음의 노드를 삭제하고 반환"""
        deleted_node = self.link
        if deleted_node is not None: 
            self.link = deleted_node.link    # 삭제할 노드 다음을 현재 노드가 가리키도록
        return deleted_node

    
class LinkedList:
    def __init__(self):
        """연결 리스트 초기화"""
        self.head = None    # 첫 번째 노드를 가리키는 포인터

    def isEmpty(self):
        """리스트가 비어있는지 확인"""
        return self.head is None

    def getNode(self, pos):
        """지정된 위치의 노드를 반환"""
        # 음수 위치는 유효하지 않음
        if pos < 0: 
            return None
        
        # 빈 리스트인 경우
        if self.head == None:
            return None
        else:    
            ptr = self.head
            # pos만큼 이동하여 해당 위치의 노드 찾기
            for i in range(pos):
                if ptr == None:
                    return None    # 범위를 벗어난 경우
                ptr = ptr.link
            return ptr

    def insert(self, pos, elem):
        """지정된 위치에 새 요소를 삽입"""
        new = Node(elem)                    # 새 노드 생성
        before = self.getNode(pos - 1)      # 삽입할 위치의 이전 노드 찾기
        
        if before is None:
            if pos == 0:    # 리스트의 맨 앞에 삽입
                new.link = self.head
                self.head = new
            else:           # 범위를 벗어난 위치
                raise IndexError("리스트 범위를 벗어남")
        else:               # 중간 또는 끝에 삽입
            before.append(new)

    def delete(self, pos):
        """지정된 위치의 노드를 삭제하고 반환"""
        if pos < 0:
            raise IndexError("리스트 범위 밖 오류")
        
        before = self.getNode(pos - 1)      # 삭제할 위치의 이전 노드 찾기
        
        if before is None:
            if pos == 0:    # 첫 번째 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else:           # 범위를 벗어난 위치
                raise IndexError("리스트 범위 밖 오류")
        else:               # 중간 또는 끝 노드 삭제
            return before.popNext()
        
    def size(self):
        """리스트의 크기(노드 개수)를 반환"""
        if self.head == None:
            return 0
        else:
            ptr = self.head
            count = 0
            # 모든 노드를 순회하면서 개수 세기
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count
    
    def find_by_title(self, title):
        """제목으로 도서를 찾아서 반환"""
        current = self.head
        while current:
            # 현재 노드의 도서 제목과 일치하는지 확인
            if current.data.title == title:
                return current.data
            current = current.link
        return None    # 찾지 못한 경우

    def find_pos_by_title(self, title):
        """제목으로 도서의 위치(인덱스)를 찾아서 반환"""
        pos = 0
        current = self.head
        while current:
            # 현재 노드의 도서 제목과 일치하는지 확인
            if current.data.title == title:
                return pos
            pos += 1
            current = current.link
        return -1    # 찾지 못한 경우 -1 반환
    
class Book:
    def __init__(self, book_id, title, author, year):
        """도서 객체 초기화"""
        self.book_id = book_id    # 책 고유 번호
        self.title = title        # 책 제목
        self.author = author      # 저자
        self.year = year          # 출판 연도

    def __str__(self):
        """도서 정보 반환"""
        return f"[{self.book_id}] {self.title} / {self.author} / {self.year}"
    
    
class BookManagement:
    def __init__(self):
        """도서 관리 시스템 초기화"""
        self.books = LinkedList()    # 도서를 저장할 연결 리스트

    def add_book(self, book_id, title, author, year):
        """새 도서 추가"""

        # 중복된 책 번호가 있는지 확인
        current = self.books.head
        while current:
            if current.data.book_id == book_id:
                print(f"[오류] 책 번호 {book_id}는 이미 존재합니다.\n")
                return
            current = current.link

        # 새 도서 객체 생성 후 리스트 끝에 추가
        new_book = Book(book_id, title, author, year)
        self.books.insert(self.books.size(), new_book)
        print(f"[등록 완료] '{title}' 도서가 추가되었습니다.\n")

    def remove_book(self, title):
        """제목으로 도서를 삭제"""
        # 제목으로 도서의 위치 찾기
        pos = self.books.find_pos_by_title(title)
        if pos == -1:    # 도서를 찾지 못한 경우
            print(f"[오류] '{title}' 도서를 찾을 수 없습니다.\n")
            return
        
        # 해당 위치의 도서 삭제
        self.books.delete(pos)
        print(f"[삭제 완료] '{title}' 도서를 삭제했습니다.\n")

    def search_book(self, title):
        """제목으로 도서 정보를 출력"""
        result = self.books.find_by_title(title)
        if result:    # 도서를 찾은 경우
            print("\n[도서 조회 결과]")
            print(result)
            print()
        else:         # 도서를 찾지 못한 경우
            print(f"[오류] '{title}' 도서를 찾을 수 없습니다.\n")

    def display_books(self):
        """모든 도서 목록"""
        if self.books.isEmpty():    # 등록된 도서가 없는 경우
            print("현재 등록된 도서가 없습니다.\n")
        else:    # 등록된 도서가 있는 경우
            print("\n[전체 도서 목록]")
            current = self.books.head
            # 모든 노드를 순회하면서 도서 정보 출력
            while current:
                print(current.data)
                current = current.link
            print()

    def run(self):
        """도서 관리 프로그램의 메인 실행 루프"""
        while True:
            # 메뉴 출력
            print("===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목)")
            print("3. 도서 조회 (책 제목)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            
            # 사용자 입력 받기
            num = input("메뉴 선택 (1-5): ")

            # 메뉴별 기능 실행
            if num == '1':      # 도서 추가
                book_id = input("책 번호: ")
                title = input("책 제목: ")
                author = input("저자: ")
                year = input("출판 연도: ")
                self.add_book(book_id, title, author, year)
                
            elif num == '2':    # 도서 삭제
                title = input("삭제할 책 제목: ")
                self.remove_book(title)
                
            elif num == '3':    # 도서 조회
                title = input("조회할 책 제목: ")
                self.search_book(title)
                
            elif num == '4':    # 전체 도서 목록 출력
                self.display_books()
                
            elif num == '5':    # 프로그램 종료
                print("프로그램을 종료합니다.")
                break
                
            else:               # 잘못된 입력
                print("[오류] 1~5 중 하나를 입력하세요.\n")

# ====== 프로그램 실행 부분 ======
if __name__ == "__main__":
    BookManagement().run()                 # 프로그램 실행