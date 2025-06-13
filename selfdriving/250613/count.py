

# 이미지에 텍스트로 표시
display_result = result.copy()
cv2.putText(display_result, f"Pixels: {pixel_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Filtered Result", display_result)
