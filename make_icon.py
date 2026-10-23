from PIL import Image, ImageDraw
import math

def make_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    s = size

    # 背景: 角丸のトラック赤
    r = s // 5
    draw.rounded_rectangle([0, 0, s-1, s-1], radius=r, fill='#c0392b')

    # グラデーション風に上部を少し明るく
    for i in range(s // 2):
        alpha = int(60 * (1 - i / (s / 2)))
        draw.rectangle([r if i == 0 else 0, i, s - (r if i == 0 else 1), i+1],
                       fill=(255, 255, 255, alpha))

    # トラック楕円（白いレーンライン）
    lw = max(2, int(s * 0.04))
    mx, my = s * 0.12, s * 0.16
    for k in range(3):
        offset = k * s * 0.045
        draw.ellipse(
            [mx + offset, my + offset, s - mx - offset, s - my - offset],
            outline=(255, 255, 255, 200 - k * 50),
            width=max(1, lw - k)
        )

    # ランナーシルエット（躍動感のあるポーズ）
    cx = s * 0.50
    cy = s * 0.48
    fc = '#FFD700'  # ゴールド
    lw2 = max(3, int(s * 0.05))

    # 頭
    hr = s * 0.075
    draw.ellipse([cx - hr, cy - s*0.30 - hr, cx + hr, cy - s*0.30 + hr], fill=fc)

    # 体
    draw.line([(cx, cy - s*0.22), (cx - s*0.03, cy + s*0.04)], fill=fc, width=lw2)

    # 腕（前に大きく振る）
    draw.line([(cx, cy - s*0.16), (cx - s*0.15, cy - s*0.28)], fill=fc, width=lw2)
    draw.line([(cx, cy - s*0.16), (cx + s*0.13, cy - s*0.06)], fill=fc, width=lw2)

    # 脚（大きなストライド）
    # 前足
    draw.line([(cx - s*0.03, cy + s*0.04), (cx - s*0.14, cy + s*0.22)], fill=fc, width=lw2)
    draw.line([(cx - s*0.14, cy + s*0.22), (cx - s*0.04, cy + s*0.35)], fill=fc, width=lw2)
    # 後足（キック）
    draw.line([(cx - s*0.03, cy + s*0.04), (cx + s*0.14, cy + s*0.16)], fill=fc, width=lw2)
    draw.line([(cx + s*0.14, cy + s*0.16), (cx + s*0.22, cy + s*0.05)], fill=fc, width=lw2)

    # 地面ライン
    gw = max(2, int(s * 0.025))
    draw.line([(s*0.1, s*0.82), (s*0.9, s*0.82)], fill=(255,255,255,150), width=gw)

    return img

for size in [192, 512]:
    img = make_icon(size)
    img.save(f'/Users/kondokensuke/track-records/icon-{size}.png')
    print(f'icon-{size}.png saved')

img = make_icon(180)
img.save('/Users/kondokensuke/track-records/apple-touch-icon.png')
print('apple-touch-icon.png saved')
