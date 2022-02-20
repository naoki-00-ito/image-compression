import os
from PIL import Image

# imgcompr モジュール
def imgcompr(input_path):

	# 画像の縮小倍率
	magnification = 4

	# 対象パス
	# CLI入力値をパスとして代入する
	target_path = input_path

	# ファイル配列
	filelist = []

	# 画像ファイル名出力ヘッダー
	print('------------- ↓↓ {0} 内の画像 ↓↓ -------------'.format(target_path))

	# ファイルのみを抽出して filelist に格納
	for f in os.listdir(target_path):
		if os.path.isfile(os.path.join(target_path, f)):
			filelist.append(f)
			# 画像ファイル名出力
			print(f)

	# 画像ファイル名出力フッター
	print('------------- ↑↑ {0} 内の画像 ↑↑ -------------'.format(target_path))

	# ファイル配列表示(デバッグ用)
	print('画像配列(デバッグ用): {0}'.format(filelist))

	for i in range(len(filelist)):
		imagefile = os.path.join(target_path, filelist[i])
		imagedata = Image.open(imagefile)
		width, height = imagedata.size
		width2 = width/magnification
		height2 = height/magnification
		imagedata2= imagedata.resize((int(width2),int(height2)))
		newimage = target_path + "new" + filelist[i]
		imagedata2.save(newimage, quality=85,optimize=True)