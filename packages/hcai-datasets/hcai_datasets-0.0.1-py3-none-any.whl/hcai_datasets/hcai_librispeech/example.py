from hcai_librispeech import HcaiLibrispeech
import tensorflow_datasets as tfds
import tensorflow as tf
import pydub
import numpy as np
import soundfile as sf

def pp(x,y):
    file_path = bytes.decode(x.numpy())
    print(file_path)
    ext = file_path.split('.')[-1]

    a = pydub.AudioSegment.from_file(file_path, ext)
    a = a.set_frame_rate(16000)
    a = a.set_channels(1)
    a = np.array(a.get_array_of_samples())
    a = a.astype(np.int16)
    return audio, label

ds, ds_info = tfds.load(
    'hcai_librispeech',
    split='dev-clean',
    with_info=True,
    as_supervised=True,
    decoders={
       'speech': tfds.decode.SkipDecoding()
    }
)

#"speech": tfds.features.Text(),
#"text": tfds.features.Text(),
#"speaker_id": tf.int64,
#"chapter_id": tf.int64,
#"id": tf.string,

ds = ds.map(lambda x,y : (tf.py_function(func=pp, inp=[x, y], Tout=[tf.float32, tf.string])))

print('')
audio, label = next(ds.as_numpy_iterator())

sf.write('test.flac', audio, 16000, format='wav')
