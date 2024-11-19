"""
音声認識する
"""

import whisper

def calc(file):
    calc_device = "cpu"
    # Whisperモデルのロード
    model = whisper.load_model(name="base", device=calc_device)  # 他に "tiny", "small", "medium", "large" も選択可能

    # 音声ファイルの文字起こし
    result = model.transcribe(file)

    # 文字起こし結果を出力
    return result["text"]