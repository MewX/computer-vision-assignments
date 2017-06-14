# csh
# $1: image folder name (without slash), containing: tasks.txt and

python predict_on_images.py -r "$1/" checkpoints/flickr8k_cnn_lstm_v1.p
