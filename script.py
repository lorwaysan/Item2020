import os
picurl = input("请输入转换图像地址(绝对地址):")
print("1.立体主义\n2.星空\n3.羽毛\n4.镶嵌画\n5.呐喊\n6.立体主义\n7.神奈川冲浪里")
stylenum = int(input("请输入生成图像风格编号:"))

if stylenum == 1:
    style = "cubist.ckpt-done"
elif stylenum == 2:
    style = "denoised_starry.ckpt-done"
elif stylenum == 3:
    style = "feathers.ckpt-done"
elif stylenum == 4:
    style = "mosaic.ckpt-done"
elif stylenum == 5:
    style = "scream.ckpt-done"
elif stylenum == 6:
    style = "udnie.ckpt-done"
elif stylenum == 7:
    style = "wave.ckpt-done"

ml = "python eval.py --model_file " + "./pretraind/" + style + " --image_file " + picurl
print(ml)
os.system(ml)