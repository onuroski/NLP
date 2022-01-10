#task 10: A Machine Translation System

# Import the model
import time

from simpletransformers.seq2seq import Seq2SeqModel
# Setting desired arguments
my_args = {    "train_batch_size": 2,
               "num_train_epochs": 10,
               "save_eval_checkpoints": False,
               "save_model_every_epoch": False,
               "evaluate_during_training": True,
               "evaluate_generated_text": True   }
# Instantiating the model
my_model=Seq2SeqModel(encoder_decoder_name="Helsinki-NLP/opus-mt-en-de",encoder_decoder_type="marian",args=my_args,use_cuda=False)
# translating the text

a = my_model.predict(['Our experienced writers travel the world to bring you informative and inspirational features, destination roundups, travel ideas, tips and beautiful photos in order to help you plan your next holiday',
                  'Each part of Germany is different, and there are thousands of memorable places to visit.',
                  "Christmas Markets originated in Germany, and the tradition dates to the Late Middle Ages.",
                  "Garmisch-Partenkirchen is a small town in Bavaria, near Germany’s highest mountain Zugspitze, which rises to 9,718 feet (2,962 meters)",
                  "It’s one of the country’s top alpine destinations, extremely popular during the winter",
                  "In spring, take a road trip through Bavaria and enjoy the view of the dark green Alps and the first alpine wildflowers. "])
time.sleep(1)
for i in a:
    print(i)
