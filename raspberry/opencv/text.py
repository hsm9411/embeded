import cv2
import numpy as np
# 캔버스 생성 (배경: 흰색)
img = np.ones((900, 1280, 3), dtype=np.uint8) * 255
font_defs = [# 폰트와 이름
    (cv2.FONT_HERSHEY_SIMPLEX, "FONT_HERSHEY_SIMPLEX"),
    (cv2.FONT_HERSHEY_PLAIN, "FONT_HERSHEY_PLAIN"),
    (cv2.FONT_HERSHEY_DUPLEX, "FONT_HERSHEY_DUPLEX"),
    (cv2.FONT_HERSHEY_COMPLEX, "FONT_HERSHEY_COMPLEX"),
    (cv2.FONT_HERSHEY_TRIPLEX, "FONT_HERSHEY_TRIPLEX"),
    (cv2.FONT_HERSHEY_COMPLEX_SMALL, "FONT_HERSHEY_COMPLEX_SMALL"),
    (cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, "FONT_HERSHEY_SCRIPT_SIMPLEX"),
    (cv2.FONT_HERSHEY_SCRIPT_COMPLEX, "FONT_HERSHEY_SCRIPT_COMPLEX")
]
colors = [ # 폰트 색
    (255, 0, 0), (0, 128, 0), (0, 0, 255), # Blue / Green / Red
    (255, 128, 0), (128, 0, 128), (0, 255, 255), # Orange / Purple / Cyan
    (255, 0, 255), (0, 0, 0) # Magenta / Black
]
y = 60
for i, (font, name) in enumerate(font_defs):
    color = colors[i % len(colors)]
    # 일반 버전
    cv2.putText(img, f"{name}", (50, y), font, 1.0, color, 2, cv2.LINE_AA)
    # 이탤릭 버전 (OR 연산)
    italic_font = font | cv2.FONT_ITALIC
    cv2.putText(img, f"{name} + ITALIC", (650, y), italic_font, 1.0, color, 2, cv2.LINE_AA)
    y += 80
    
cv2.imshow("Font vs Italic Font", img)
cv2.waitKey(0)
cv2.destroyAllWindows()