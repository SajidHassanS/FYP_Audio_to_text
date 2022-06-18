import pickle

import librosa
import torch


def make_prediction_on_file(file):
    tokenizer_path = r"D:\\100%_presentation\\Models\\English_Model\\tokenizer.pickle"
    model_path = r"D:\\100%_presentation\\Models\\English_Model\\model.pickle"
    print('INSIDE ENGLISH MODEL')
    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open(model_path, 'rb') as handle:
        model = pickle.load(handle)

    speech, rate = librosa.load(file, sr=16000)

    input_values = tokenizer(speech, return_tensors='pt').input_values

    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)

    transcriptions = tokenizer.decode(predicted_ids[0])

    print(transcriptions)

    return transcriptions
