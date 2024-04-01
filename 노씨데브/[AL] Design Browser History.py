class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current

    # 앞의 페이지 기록은 다 삭제되고 url로 방문
    def visit(self, url):

        return None
    
    # steps 수 만큼 '뒤로 가기'
    # step > x(page) 일 때는 x만큼만 '뒤로 가기'
    def back(self, steps): # O(n)

        return self.current.val
    
    # step 수 만큼 '앞으로 가기'
    # step > x(page) 일 때는 x만큼만 '앞으로 가기'
    # 앞으로 가기가 완료되면 현재 url을 return
    def forward(self, steps): # O(n)

        return self.current.val
    
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")    
browserHistory.visit("facebook.com")   
browserHistory.visit("youtube.com")   
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)