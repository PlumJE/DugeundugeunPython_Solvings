import time

fhours = int(time.time() // 3600 % 24)
fseconds = int(time.time() // 60 % 60)

print("현재 시간(영국 그리니치 기준):", str(fhours) + "시" + str(fseconds) + "분")
