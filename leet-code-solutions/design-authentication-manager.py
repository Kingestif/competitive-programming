class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.map={}
        self.timeToLive=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map  and self.map[tokenId] + self.timeToLive > currentTime:
            self.map[tokenId] =  currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter=0
        for key,values in self.map.items():
            if values + self.timeToLive > currentTime:
                counter+=1
        return counter
        





# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)