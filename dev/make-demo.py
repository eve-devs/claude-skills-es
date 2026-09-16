#!/usr/bin/env python3
"""
Genera assets/demo.gif: una recreacion de una sesion de Claude Code
usando la skill pr-listo.

Uso:       python3 dev/make-demo.py
Requiere:  Pillow  (pip install Pillow)

El contenido es fiel a lo que produce la skill, renderizado cuadro a
cuadro con Pillow. No es una captura de pantalla en vivo.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 545
PAD_X, PAD_TOP, LINE_H, FS = 30, 76, 27, 18

BG     = (26, 27, 33)
BAR    = (34, 35, 43)
BORDER = (48, 50, 60)
FG     = (216, 218, 226)
DIM    = (119, 124, 141)
ACCENT = (217, 119, 87)
YELLOW = (224, 175, 104)
CYAN   = (125, 207, 255)
GREEN  = (158, 206, 106)
CHIPBG = (56, 42, 38)

MENLO = "/System/Library/Fonts/Menlo.ttc"
font  = ImageFont.truetype(MENLO, FS, index=0)
fontb = ImageFont.truetype(MENLO, FS, index=1)
fonts = ImageFont.truetype(MENLO, 14, index=0)
CW = font.getlength("M")

PROMPT = "prepara el PR de esta rama"
SPIN = "◐◓◑◒"

# bloques revelados de uno en uno: (icono, texto, color, sub)
FINDINGS = [
    ("warn", "src/auth/interceptor.ts:44",        YELLOW, "console.log con el token completo"),
    ("warn", "migrations/0012_add_sessions.sql",  YELLOW, "la migración no tiene down"),
    ("ask",  "services/rate-limiter.ts",          CYAN,   "lógica nueva sin ningún test"),
]


def icon_check(d, x, y, col):
    d.line([(x + 1, y + 9), (x + 5, y + 14), (x + 13, y + 3)], fill=col, width=2)


def icon_warn(d, x, y, col):
    d.polygon([(x + 7, y + 2), (x + 14, y + 15), (x, y + 15)], fill=col)
    d.line([(x + 7, y + 7), (x + 7, y + 11)], fill=BG, width=2)


def chrome(d):
    d.rectangle([0, 0, W, H], fill=BG)
    d.rectangle([0, 0, W, 44], fill=BAR)
    d.line([(0, 44), (W, 44)], fill=BORDER)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([22 + i * 21, 16, 34 + i * 21, 28], fill=c)
    t = "~/proyecto-api  ·  claude"
    d.text(((W - fonts.getlength(t)) / 2, 15), t, font=fonts, fill=DIM)


def frame(typed, chip=False, spin=None, done=False, blocks=0, tail=0, cursor=True):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    chrome(d)
    y = PAD_TOP

    d.line([(PAD_X + 2, y + 4), (PAD_X + 8, y + 11), (PAD_X + 2, y + 18)],
           fill=GREEN, width=2)
    d.text((PAD_X + CW * 2, y), typed, font=font, fill=FG)
    if cursor and not chip:
        x = PAD_X + CW * 2 + font.getlength(typed)
        d.rectangle([x + 1, y + 3, x + CW - 1, y + FS + 5], fill=FG)
    y += int(LINE_H * 1.9)

    if chip:                                   # la skill se activo
        label = "skill · pr-listo"
        tw = fontb.getlength(label)
        d.rounded_rectangle([PAD_X, y - 3, PAD_X + tw + 44, y + FS + 8],
                            radius=11, fill=CHIPBG)
        d.ellipse([PAD_X + 14, y + 7, PAD_X + 22, y + 15], fill=ACCENT)
        d.text((PAD_X + 30, y), label, font=fontb, fill=ACCENT)
        y += int(LINE_H * 1.75)

    if spin is not None:
        d.text((PAD_X, y), spin, font=font, fill=ACCENT)
        d.text((PAD_X + CW * 2, y), "Leyendo 8 commits contra origin/main…",
               font=font, fill=DIM)
        return im

    if done:
        icon_check(d, PAD_X + 1, y + 4, GREEN)
        d.text((PAD_X + CW * 2, y), "8 commits leídos contra origin/main",
               font=font, fill=DIM)
        y += int(LINE_H * 1.75)

        d.text((PAD_X, y), "Antes de escribir la descripción, 3 cosas que el",
               font=font, fill=FG)
        y += LINE_H
        d.text((PAD_X, y), "reviewer iba a encontrar:", font=font, fill=FG)
        y += int(LINE_H * 1.5)

        for kind, path, col, sub in FINDINGS[:blocks]:
            if kind == "warn":
                icon_warn(d, PAD_X + 1, y + 3, col)
            else:
                d.text((PAD_X + 2, y), "?", font=fontb, fill=col)
            d.text((PAD_X + CW * 2, y), path, font=font, fill=col)
            y += LINE_H
            d.text((PAD_X + CW * 2, y), sub, font=font, fill=DIM)
            y += int(LINE_H * 1.15)

        if tail:
            y = PAD_TOP + int(LINE_H * 1.9) + int(LINE_H * 1.75) * 2 \
                + LINE_H + int(LINE_H * 1.5) + int(LINE_H * 2.15) * 3 + 8
            d.text((PAD_X, y), "¿Los arreglo antes de abrir el PR, o lo subo",
                   font=font, fill=FG)
            d.text((PAD_X, y + LINE_H), "como draft?", font=font, fill=FG)
    return im


frames, delays = [], []
add = lambda im, ms: (frames.append(im), delays.append(ms))

add(frame(""), 520)
for i in range(2, len(PROMPT) + 1, 2):
    add(frame(PROMPT[:i]), 55)
add(frame(PROMPT), 150)
add(frame(PROMPT, cursor=False), 300)
add(frame(PROMPT, chip=True), 420)                       # la skill enciende
for i in range(12):
    add(frame(PROMPT, chip=True, spin=SPIN[i % len(SPIN)]), 90)
add(frame(PROMPT, chip=True, done=True, blocks=0), 320)
for n in (1, 2, 3):
    add(frame(PROMPT, chip=True, done=True, blocks=n), 300)
add(frame(PROMPT, chip=True, done=True, blocks=3, tail=1), 3800)

pal = frames[-1].quantize(colors=48, method=Image.MEDIANCUT)
qf = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
qf[0].save("assets/demo.gif", save_all=True, append_images=qf[1:],
           duration=delays, loop=0, optimize=True, disposal=1)
print(f"assets/demo.gif: {len(qf)} cuadros, {W}x{H}")
