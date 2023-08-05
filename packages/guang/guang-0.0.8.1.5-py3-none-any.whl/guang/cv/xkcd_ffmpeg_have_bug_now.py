import xkcd
from scipy import misc
from imageio import imread
import subprocess as sp
import sys


def main(in_file, out_file, duration, strength, size=32):
    """XKCD_SWEEP renders a animation with the xkcd strnth paramter running over timer
Required xkcd.py source and ffmpeg.exe to be acessable

"""
    img = imread(in_file)
    w, h, c = img.shape
    duration, strength = float(duration), float(strength)
    size = int(size)

    # see here for refrence: http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/
    command = [
        "ffmpeg.exe",
        "-y",
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-s",
        "%dx%d" % (w, h),
        "-pix_fmt",
        "rgba",
        "-r",
        "30",
        "-i",
        "-",
        "-an",
        "-vcodec",
        "h264",  #"libx264",
        "-pix_fmt",
        "yuv420p",
        str(out_file)
    ]

    with sp.Popen(command, stdin=sp.PIPE, stderr=sp.STDOUT) as pipe:
        c = xkcd.Canvas(img, 0.0, size, False)
        for i in range(int(30 * duration)):
            if i % 30 == 0:
                print("compleated: %s%%" % (i / (30 * duration)))
            c.strength = strength * (i / (30 * duration))
            out = c.render_img()
            pipe.stdin.write(out.tostring())


if __name__ == "__main__":
    main(in_file="./pic/hue2.png",
         out_file="./pic/out.mp4",
         duration=10,
         strength=1,
         size=32)
