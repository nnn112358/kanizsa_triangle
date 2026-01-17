# Kanizsa Triangle

カニッツァの三角形（錯視図形）をSVGとPython+OpenCVで生成するプロジェクト。
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/f4ba3a88-9521-448b-bb59-bd6c3c588bb8" />

## 概要

カニッツァの三角形は、実際には描かれていない白い三角形が浮かび上がって見える有名な錯視図形です。

### 構造

```
      ●               ← 黒い円（左上）
     /\
    /  \              ← 線の三角形（上向き）
   /    \
  /______\
 ●        ●          ← 黒い円（右上・下）
```

3つの要素をレイヤーで重ねて錯視を実現:
1. 黒い円 × 3
2. 黒い線の三角形（上向き）
3. 白い三角形（下向き、円の中心を結ぶ）

## ファイル

| ファイル | 説明 |
|---------|------|
| `kanizsa_triangle.svg` | SVG版（静止画） |
| `kanizsa_triangle.py` | Python + OpenCV版（回転アニメーション） |
| `kanizsa_triangle_cv.png` | 生成された静止画 |
| `kanizsa_triangle.avi` | 生成された回転アニメーション動画 |

## 実行方法

### 依存関係のインストール

```bash
uv sync
```

### 実行

```bash
uv run python kanizsa_triangle.py
```

### 出力

- `kanizsa_triangle.avi` - 回転アニメーション（6秒、30fps）
- `kanizsa_triangle_cv.png` - 静止画

## 座標パラメータ

400x400キャンバス基準:

| 要素 | 座標 |
|------|------|
| 黒円（左上） | (68, 90), 半径45 |
| 黒円（右上） | (332, 90), 半径45 |
| 黒円（下） | (200, 345), 半径45 |
| 線三角形 | (200,52)-(50,260)-(350,260) |
| 白三角形 | (68,90)-(332,90)-(200,345) |

## 動画設定

| 項目 | 値 |
|------|-----|
| サイズ | 400x400 |
| FPS | 30 |
| 回転速度 | 2度/フレーム |
| フレーム数 | 180 |
| 再生時間 | 6秒 |
| コーデック | XVID |

## 依存関係

- Python >= 3.11
- numpy
- opencv-python
