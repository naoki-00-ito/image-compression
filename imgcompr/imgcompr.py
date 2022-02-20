import os
from PIL import Image

# imgcompr モジュール
def imgcompr(input_path):

	"""
	----------------------------
	【圧縮設定】 ここから
	※下記の変数の値を任意のものに変更してください。
	↓↓↓↓↓↓↓↓↓↓
	"""
	# 画像の縮小倍率
	# compr_magnification = 2 の場合は 1/4 のサイズに縮小
	compr_magnification = 1

	# 画像の圧縮クオリティ
	# ex) compr_quality = 85 の場合は 85% のクオリティに変更
	compr_quality = 85
	"""
	↑↑↑↑↑↑↑↑↑↑
	【圧縮設定】 ここまで
	----------------------------
	"""

	# 対象パス
	# CLI入力値をパスとして代入する
	target_path = input_path

	# ファイル配列
	filelist = []

	# 画像ファイル名出力ヘッダー
	print('------ ↓↓ {0} 内の画像 ↓↓ ------'.format(target_path))

	# ファイルのみを抽出して filelist に格納
	for f in os.listdir(target_path):
		if os.path.isfile(os.path.join(target_path, f)):
			filelist.append(f)
			# 画像ファイル名出力
			print(f)

	# 画像ファイル名出力フッター
	print('------ ↑↑ {0} 内の画像 ↑↑ ------'.format(target_path))

	# ファイル配列表示(デバッグ用)
	print('画像配列(デバッグ用): {0}'.format(filelist))


	# 圧縮後画像ファイル名出力ヘッダー
	print('------ ↓↓ {0} 内に圧縮した画像を保存しました!! ↓↓ ------'.format(target_path))

	for i in range(len(filelist)):
		imagefile = os.path.join(target_path, filelist[i])
		imagedata = Image.open(imagefile)
		width, height = imagedata.size
		width2 = width/compr_magnification
		height2 = height/compr_magnification
		imagedata2= imagedata.resize((int(width2),int(height2)))
		newimage = target_path + "compr_" + filelist[i]
		imagedata2.save(newimage, quality=compr_quality,optimize=True)
		# 圧縮画像ファイル名出力
		print(newimage)

	# 圧縮設定関連出力
	print('------ 圧縮設定 ------')
	print('縮小倍率: 1/{0}'.format(compr_magnification))
	print('クオリティ: {0}%'.format(compr_quality))
	print('※ファイル名の頭に「compr_」が付いているものが圧縮後のファイルです。')