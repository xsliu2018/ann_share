import imageio

gif_images = []
for i in range(0, 400):
    gif_images.append(imageio.imread("images_classify/"+str(i)+".png"))   # 读取多张图片
imageio.mimsave("classify.gif", gif_images, fps=25)   # 转化为gif动画
