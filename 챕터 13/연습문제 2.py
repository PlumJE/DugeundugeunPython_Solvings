class TV:
    def __init__(self):
        self.__channel = 1
        self.__volume = 1
        self.__on = False
    
    def turnOn(self):
        self.__on = True
        print("TV를 켰습니다.")
        print("TV의 채널 :", self.__channel, "TV의 음량 :", self.__volume)
    def turnOff(self):
        self.__on = False
        print("TV를 껐습니다.")
    def setChannel(self, channel):
        self.__channel = channel
        print("채널 변경 :", channel)
    def setVolume(self, volume):
        self.__volume = volume
        print("음량 변경 :", volume)

테레비 = TV()
테레비.turnOn()
테레비.setChannel(11)
테레비.setVolume(6)
테레비.turnOn()
테레비.turnOff()
