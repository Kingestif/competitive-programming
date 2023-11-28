class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius+273.15
        far=(celsius*1.8)+32.00
        new=[]
        new.append(kelvin)
        new.append(far)
        return new