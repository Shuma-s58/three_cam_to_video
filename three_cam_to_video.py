import cv2

# カメラのデバイスID
camera_ids = [0, 1, 2]  # 使用するカメラのデバイスID
output_files = ["output_cam1.mp4", "output_cam2.mp4", "output_cam3.mp4"]  # 保存するファイル名
frame_width = 640  # フレーム幅
frame_height = 480  # フレーム高さ
fps = 30  # フレームレート
codec = cv2.VideoWriter_fourcc(*'mp4v')

# カメラと動画保存の設定
captures = []
writers = []

# 各カメラの初期化
for i, cam_id in enumerate(camera_ids):
    cap = cv2.VideoCapture(cam_id)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    if not cap.isOpened():
        print(f"カメラ {i+1} (ID: {cam_id}) が認識されていません")
        exit()

    out = cv2.VideoWriter(output_files[i], codec, fps, (frame_width, frame_height))
    captures.append(cap)
    writers.append(out)

print("録画開始。'q'キーで終了します。")

# 録画ループ
while True:
    for i, cap in enumerate(captures):
        ret, frame = cap.read()  # 各カメラからフレームを取得
        if not ret:
            print(f"カメラ {i+1} からフレームを取得できませんでした")
            continue

        writers[i].write(frame)  # 動画ファイルにフレームを書き込む

        # 画面に各カメラのフレームを表示
        cv2.imshow(f"Camera {i+1}", frame)

    # 'q'キーで録画を停止
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
for i, cap in enumerate(captures):
    cap.release()
    writers[i].release()
    cv2.destroyWindow(f"Camera {i+1}")

cv2.destroyAllWindows()

print("録画終了。すべての動画を保存しました。")

