import cv2

# 保存する動画の設定
output_file = "output.mp4"  # 保存先ファイル名
frame_width = 640  # フレーム幅
frame_height = 480  # フレーム高さ
fps = 30  # フレームレート
codec = cv2.VideoWriter_fourcc(*'mp4v')  # MP4用コーデック

# カメラを初期化（デバイスID 0 を使用、複数カメラがある場合はIDを変更）
cap = cv2.VideoCapture(0)

# 解像度設定（必要に応じて調整）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# 動画保存の初期化
out = cv2.VideoWriter(output_file, codec, fps, (frame_width, frame_height))

if not cap.isOpened():
    print("カメラが認識されていません")
    exit()
print("録画開始。'q'キーで終了します。")

while True:
    ret, frame = cap.read()  # カメラからフレームを取得
    if not ret:
        print("フレームの取得に失敗しました")
        break
    out.write(frame)  # 動画ファイルにフレームを書き込む
    # 画面に現在のフレームを表示（省略可能）
    cv2.imshow("Camera", frame)
    # 'q'キーで録画を停止
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
out.release()
cv2.destroyAllWindows()
print("録画終了。動画を保存しました。")
