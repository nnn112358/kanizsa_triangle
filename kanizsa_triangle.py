import cv2
import numpy as np
import math


def rotate_point(x: float, y: float, cx: float, cy: float, angle: float) -> tuple[int, int]:
    """点(x,y)を中心(cx,cy)の周りにangle度回転"""
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    # 中心を原点に移動
    dx = x - cx
    dy = y - cy

    # 回転
    new_x = dx * cos_a - dy * sin_a + cx
    new_y = dx * sin_a + dy * cos_a + cy

    return int(new_x), int(new_y)


def create_kanizsa_triangle(size: int = 400, angle: float = 0) -> np.ndarray:
    """カニッツァの三角形を生成する（回転対応）"""
    img = np.ones((size, size, 3), dtype=np.uint8) * 255

    scale = size / 400
    cx, cy = size // 2, size // 2  # 回転中心

    def s(val: float) -> int:
        return int(val * scale)

    # 元の座標（400x400基準）
    radius = s(45)
    circles_orig = [
        (s(68), s(90)),
        (s(332), s(90)),
        (s(200), s(345)),
    ]

    triangle_outline_orig = [
        (s(200), s(52)),
        (s(50), s(260)),
        (s(350), s(260)),
    ]

    # 回転適用
    circles = [rotate_point(x, y, cx, cy, angle) for x, y in circles_orig]
    triangle_outline = [rotate_point(x, y, cx, cy, angle) for x, y in triangle_outline_orig]

    # 1. 黒い円3つ
    for px, py in circles:
        cv2.circle(img, (px, py), radius, (0, 0, 0), -1, cv2.LINE_AA)

    # 2. 黒い線の三角形
    pts_outline = np.array(triangle_outline, dtype=np.int32)
    cv2.polylines(img, [pts_outline], True, (0, 0, 0), s(2.5), cv2.LINE_AA)

    # 3. 白い三角形
    pts_white = np.array(circles, dtype=np.int32)
    cv2.fillPoly(img, [pts_white], (255, 255, 255), cv2.LINE_AA)

    return img


def main():
    size = 400
    fps = 1
    speed = 2  # 回転速度（度/フレーム）
    duration_frames = 360 // speed  # 1回転分のフレーム数

    # AVI動画ファイル作成
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('kanizsa_triangle.avi', fourcc, fps, (size, size))

    print(f"動画を生成中... ({duration_frames}フレーム)")

    for frame in range(duration_frames):
        angle = frame * speed
        img = create_kanizsa_triangle(size, angle)
        out.write(img)

        # プレビュー表示
        cv2.imshow("Kanizsa Triangle", img)
        if cv2.waitKey(1) == 27:  # ESC
            break

    out.release()
    cv2.destroyAllWindows()

    print("kanizsa_triangle.avi を保存しました")

    # 静止画も保存
    img = create_kanizsa_triangle(size, 0)
    cv2.imwrite("kanizsa_triangle_cv.png", img)
    print("kanizsa_triangle_cv.png を保存しました")


if __name__ == "__main__":
    main()
