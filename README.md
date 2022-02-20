# image-compression
画像圧縮ツール


## Python 環境構築
Mac https://prog-8.com/docs/python-env

### `pyenv install 3.6.5` でエラーが出る場合

```
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```  

このエラーが出た場合は下記コマンドで xcode を所定位置にインストール  
```
xcode-select --install
```

```
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```

```
sudo xcodebuild -runFirstLaunch
```

下記コマンドで Python 3.6.5 をインストール
```
CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" \
pyenv install --patch 3.6.5 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
```

参考
- https://qiita.com/nishina555/items/e23d73067a5cac182a63
- https://qiita.com/Butterthon/items/e7d1f379c828b41f3e19
- https://harucharuru.hatenablog.com/entry/2020/11/16/205232
